import pytest
import mock
from io import StringIO


@pytest.mark.unit
def test_toplevel_cli():
    from tomb_cli.main import TombApp
    stdout = StringIO()

    app = TombApp()
    with pytest.raises(SystemExit):
        with mock.patch('sys.stdout', stdout):
            app.run(['--version'])

    assert stdout.getvalue() == 'py.test 0.0.1\n'


@pytest.mark.unit
def test_main_func():
    from tomb_cli.main import main
    stdout = StringIO()

    with pytest.raises(SystemExit):
        with mock.patch('sys.stdout', stdout):
            main(argv=['--version'])

    assert stdout.getvalue() == 'py.test 0.0.1\n'
