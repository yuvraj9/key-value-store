from click.testing import CliRunner
from tests.cli import commands

def test_get_not_found():
    runner = CliRunner()
    result = runner.invoke(commands, ['get', 'lamsbda'])
    assert result.exit_code == 0
    assert result.output == '{"status_code": 404, "error": "Key Doesn\'t exist"}\n\n'

def test_put_value():
    runner = CliRunner()
    testPut = runner.invoke(commands, ['put', 'key1', 'value1'])
    assert testPut.exit_code == 0
    assert testPut.output == '{"key1": "value13"}\n\n'

def test_get_value():
    runner = CliRunner()
    testGet = runner.invoke(commands, ['get', 'key1'])
    assert testGet.exit_code == 0
    assert testGet.output == '{"value": "value1"}\n\n'

# File test