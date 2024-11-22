from random import randint

from typer.testing import CliRunner

from cutp.app import app
from cutp.utils.ports import PORTS

runner = CliRunner()


def test_check_less_than_1058():
    result = runner.invoke(app, ['check', '1057'])
    assert result.exit_code == 0
    assert 'You must enter a port between 1058 and 65535!' in result.stdout


def test_check_available_port():
    while True:
        port = randint(1058, 65535)

        if port not in PORTS:
            break

    result = runner.invoke(app, ['check', str(port)])
    assert result.exit_code == 0
    assert f'Port {port} is free.' in result.stdout


def test_check_not_available_port():
    port = 1234
    result = runner.invoke(app, ['check', str(port)])
    assert result.exit_code == 0
    assert (
        f'Port {port} is already used by an Umbrel application.'
        in result.stdout
    )


def test_gen_port():
    result = runner.invoke(app, ['gen'])
    assert result.exit_code == 0
    port = int(result.stdout[:-1])
    assert port >= 1058
    assert port <= 65535
