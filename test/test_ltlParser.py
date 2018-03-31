from src.ltlParser import ltlParse


def test_simple_1():
    assert ltlParse("'a' & 'b'") == ltlParse("('a' & 'b')")


def test_simple_2():
    assert ltlParse("'b' & 'a'") != ltlParse("('a' & 'b')")


def test_parse_1():
    ref = ltlParse("('a' | ('b' R 'c'))")
    test = ltlParse("'a' | 'b' R 'c'")
    assert ref == test


def test_parse_2():
    ref = ltlParse("('a' && (X 'b') U ((F 'a') & 'b'))")
    test = ltlParse("'a' && X 'b' U (F 'a' & 'b')")
    assert ref == test
