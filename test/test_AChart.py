from src.ltlParser import ltlParse
from src.AutomatonHelper import AutomatonHelper
from src.DiagramHelper import DiagramHelper
from src.VerifierHelper import VerifierHelper

expected1 = """S(state0)
E(id)
S(ID)
E(number)
A(SetID)
S(state0)
E(id)
S(ID)
E(number)
A(SetID)
S(state0)
E(id)
S(ID)
E(number)
A(SetID)
S(state0)
E(id)
S(ID)
E(number)
A(SetID)
S(state0)""".split('\n')

expected2 = """S(state0)
E(id)
S(ID)
E(number)
A(SetID)
S(state0)
E(id)
S(ID)
E(number)
A(SetID)
S(state0)
E(id)
S(ID)
E(number)""".split('\n')


def test_AChart():
    diagramService = DiagramHelper()
    automatonService = AutomatonHelper()
    verifierService = VerifierHelper(automatonService)
    diagram = diagramService.parseDiagram("./data/AChart.xstd")
    automaton = automatonService.createFromDiagram(diagram)

    formula = "G'a'"
    ltl = ltlParse(formula)
    counterexample1 = verifierService.verify(automaton, ltl)

    formula = "F 'E(name)' R !'S(ID)'"
    ltl = ltlParse(formula)
    counterexample2 = verifierService.verify(automaton, ltl)

    assert counterexample1 == expected1
    assert counterexample2 == expected2
