import logging
from src.model.buchi.Automaton import Automaton

log = logging.getLogger('automationTest')


def test_loop_path():
    a = Automaton()
    a.addTransition(0, 0, ord('a'))
    assert not a.findPath()

    a.setAccepting(0)
    assert [ord('a')] == a.findPath()


def test_tailed_path():
    log.info('lasso test')
    n = 10
    a = Automaton()
    for i in range(n - 1):
        a.addTransition(i, i + 1, i)

    a.addTransition(n - 1, n / 2, n - 1)
    a.setAccepting(n / 2 - 1)
    assert not a.findPath()

    a.setAccepting(n / 2 + 1)
    act = a.findPath()
    assert list(range(n)) == act
