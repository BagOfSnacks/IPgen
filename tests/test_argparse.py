import pytest

from IPgen.ArgParser import ArgParser

@pytest.mark.parametrize('args, key, expected', [
    (["-n 5"], 'amount', 5),
    ([], 'amount', 1),
    (["-v 6"], 'version', 6),
    (["-v 4"], 'version', 4),
    ([], 'json', None),
    ([], 'txt', None),
])
def test_arg_parsing(args: list[str], key: str, expected: str):
    parser = ArgParser(args)
    assert parser.get_setting(key) is expected


@pytest.mark.parametrize('args', [
    ["-n a"],
    ["-v 5"],
    ["-j"],
])
def test_parser_raises_exception_when_invalid_args(args: list[str]):
    with pytest.raises(BaseException):
        ArgParser(args)