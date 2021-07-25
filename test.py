import json
from tests.cli import commands
from click.testing import CliRunner


def test_get_not_found():
    """
    Executes the kv get <key> command. The key does not exist yet so it
    returns the Key Doesn't exist message and status_code. It validates
    the output.
    """
    runner = CliRunner()
    result = runner.invoke(commands, ['get', 'lamsbda'])
    expected_value = '{"status_code": 404, "error": "Key Doesn\'t exist"}\n\n'
    assert result.exit_code == 0
    assert result.output == expected_value


def test_put_value():
    """
    Executes the kv put <key> <value> command. This puts the pair in the
    key value store. Then we check the output as it should return a json
    of the key-value pair.
    """
    runner = CliRunner()
    testPut = runner.invoke(commands, ['put', 'key1', 'value1'])
    assert testPut.exit_code == 0
    assert testPut.output == '{"key1": "value1"}\n\n'


def test_get_value():
    """
    Executes kv get <key> command again but this time we check for the
    key which we have added in above step. This validates the put
    sub command as well.
    """
    runner = CliRunner()
    testGet = runner.invoke(commands, ['get', 'key1'])
    assert testGet.exit_code == 0
    assert testGet.output == '{"value": "value1"}\n\n'
    verify_from_file()


def verify_from_file():
    """
    This function verifies if key exist in storage as well. It directly
    pulls the value of key which we added in test_put_value() function.
    Then we validate it.
    """
    with open('store.json', 'r') as file:
        data = file.read()

    # Converts file data into a json
    KVSTORE = json.loads(data)

    # Check for given key in the object and fetches value
    value = KVSTORE.get('key1')

    assert value == 'value1'
