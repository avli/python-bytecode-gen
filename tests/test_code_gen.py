import pytest

from calc import gencode


@pytest.mark.parametrize('expected,source', [
    (4, '2 + 2'),
    (0, '0 - 0'),
    (-1, '100 - 99 - 2'),
    (-50, '1 + 2 + 3 - 42 + 0 - 14'),
])
def test_code_gen(expected, source):
    assert expected == eval(gencode(source))


@pytest.mark.parametrize('expected,source', [
    (2, '2 + 2'),
    (2, '0 - 0'),
    (2, '100 - 99 - 2'),
    (2, '1 + 2 + 3 - 42 + 0 - 14'),
    (1, '19')
])
def test_stack_size(expected, source):
    codeobj = gencode(source)
    assert expected == codeobj.co_stacksize

