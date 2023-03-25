import subprocess
import pytest

from IPgen.const import PATH


def run_module(args: list[str] = None):
    path = f'python {PATH}'
    if args:
        path = path + ' ' + ' '.join(args)

    process = subprocess.run(path, capture_output=True, text=True)
    print(process.stdout)
    return process.returncode


def test_run_via_console():
    exit_code = run_module()
    assert exit_code == 0


@pytest.mark.parametrize('args, expected', [
    (['n a'], (1,2)),
    (['-n a'], (1,2)),
    (['-n a'], (1,2)),
    (['-ja 1'], (1,2)),
    (['-j 1'], (1,2)),
])
def test_run_via_console_with_invalid_args(args: list[str], expected: int):
    exit_code = run_module(['-n a'])
    assert exit_code in expected


def test_console_output(capsys):
    default_out = r"{'amount': 1, 'version': 4, 'info': False, 'txt': None, 'json': None}"
    run_module()
    captured = capsys.readouterr().out
    captured = captured.replace("\n", "")

    assert captured.startswith(default_out)  # Necessary because the generated IP Addresses will always differ
