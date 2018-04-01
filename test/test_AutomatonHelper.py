import pytest
import logging
import os

from src.model.buchi.Automaton import Automaton
from src.AutomatonHelper import AutomatonHelper
from src.DiagramHelper import DiagramHelper

from src.model.ltl.LTL import LTL

log = logging.getLogger()

output = """never {
T0_init:
\tif
\t:: (w) || (!z && !y) -> goto accept_all
\t:: (!z) -> goto T0_S4
\t:: (!z && !x) -> goto accept_S5
\tfi;
T0_S4:
\tif
\t:: (1) -> goto T0_S4
\t:: (!x) -> goto accept_S5
\tfi;
accept_S5:
\tif
\t:: (!x) -> goto accept_S5
\tfi;
accept_all:
skip
}"""


class Env:
    def __init__(self):
        self.diagramService = DiagramHelper()
        self.automatonService = AutomatonHelper()


@pytest.fixture(scope='module')
def env():
    return Env()


def test_createFromDiagram(env: Env):
    diagram = env.diagramService.parseDiagram(os.path.join("data", "AChart.xstd"))
    automaton = env.automatonService.createFromDiagram(diagram)
    assert 14 == automaton.size()


def test_parse(env: Env):
    states = env.automatonService.parse(output)
    assert 4 == len(states), "States count"


def test_map(env: Env):
    diagram = env.diagramService.parseDiagram(os.path.join("data", "AChart.xstd"))
    automatonA = env.automatonService.createFromDiagram(diagram)
    automatonB = env.automatonService.map_(automatonA, lambda x: str(x))
    assert automatonA.size() == automatonB.size(), "Automaton Size"
    assert automatonA.initialState == automatonB.initialState, "Automaton Initial State"
    assert automatonA.acceptingSet == automatonB.acceptingSet, "Automaton Accepting Set"


def test_createStateListFromLtl(env: Env):
    states = env.automatonService.createStateListFromLtl("([] <> x && y) || z -> w")
    assert 4 == len(states), "States count"


def test_createFromLtl(env: Env):
    automaton = env.automatonService.createFromLtl_str("([] <> x && y) || z -> w")
    assert 4 == automaton.size(), "States count"


def test_emptyTransitions(env: Env):
    states = env.automatonService.createStateListFromLtl("!true")
    assert 1 == len(states), "States count"
    assert 0 == len(states[0].transitions), "Transition count"


def test_createFromLtlFormula(env: Env):
    ltl = LTL.not_(LTL.globally(LTL.future(LTL.var("p"))))
    automaton = env.automatonService.createFromLtl_formula(ltl)
    reference = Automaton()
    reference.addTransition(0, 0, LTL.t())
    notP = LTL.not_(LTL.var("p"))
    reference.addTransition(0, 1, notP)
    reference.addTransition(1, 1, notP)
    reference.setAccepting(1)
    reference.initialState = 0
    assert reference == automaton


class MyIntersector(object):
    def intersect(self, a: int, b: int):
        return a if a == b else None


def test_simpleIntersectionTest(env: Env):
    log.info("intersection test")
    an = 2
    bn = 4
    a = Automaton()
    b = Automaton()
    a.addTransition(0, 1, 0)
    a.addTransition(1, 0, 1)

    curr = 0
    for i in range(bn - 1):
        b.addTransition(i, i + 1, curr)
        curr = 1 - curr

    b.addTransition(3, 0, 1)

    a.setAccepting(0)
    b.setAccepting(1)

    c = env.automatonService.intersect(a, b, MyIntersector())
    path = c.findPath()
    ref = []
    curr = 0
    for i in range(len(path)):
        ref.append(curr)
        curr = 1 - curr
    assert path == ref
