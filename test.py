import json
from tests.cli import commands
from click.testing import CliRunner

def test_get_not_found():
    runner = CliRunner()
    result = runner.invoke(commands, ['get', 'lamsbda'])
    assert result.exit_code == 0
    assert result.output == '{"status_code": 404, "error": "Key Doesn\'t exist"}\n\n'

def test_put_value():
    runner = CliRunner()
    testPut = runner.invoke(commands, ['put', 'key1', 'value1'])
    assert testPut.exit_code == 0
    assert testPut.output == '{"key1": "value1"}\n\n'

def test_get_value():
    runner = CliRunner()
    testGet = runner.invoke(commands, ['get', 'key1'])
    assert testGet.exit_code == 0
    assert testGet.output == '{"value": "value1"}\n\n'

def verify_from_file():
    with open('store.json', 'r') as file:
        data = file.read()

    # Converts file data into a json
    KVSTORE = json.loads(data)

    # Check for given key in the object and fetches value
    value = KVSTORE.get('key1')

    assert value == 'value1'

verify_from_file()