import pytest

from src.LTLIntersector import LTLIntersector
from src.model.ltl.LTL import LTL


@pytest.fixture(scope='module')
def ltlIntersector():
    return LTLIntersector()


def test_Intersection(ltlIntersector):
    common = "E(machine_type)"
    a = LTL.var(common)
    b = LTL.and_(LTL.not_(LTL.var("S(Dot")), LTL.var(common))
    expected = LTL.var(common)
    actual = ltlIntersector.intersect(a, b)
    assert expected == actual
