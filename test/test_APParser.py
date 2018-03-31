from src.ltlParser import ltlParse
from src.AutomatonHelper import AutomatonHelper
from src.DiagramHelper import DiagramHelper
from src.VerifierHelper import VerifierHelper

expected1 = """S(state0)
E(machine_type)
A(WriteDefine)
A(SaveMachineType)
S(MachineType)
E(machine_name)
A(WriteToken)
S(MachineName)
E(vertical_line)
S(Vert)
E(vertical_line)
S(Fork)
E(machine_type)
S(Fork)
E(machine_type)
S(Fork)
E(machine_name)
A(WriteEndForkProp)
S(ForkMachine)
true""".split('\n')

expected2 = """S(state0)
E(machine_type)
A(WriteDefine)
A(SaveMachineType)
S(MachineType)
E(machine_name)
A(WriteToken)
S(MachineName)
E(dot)
A(WriteToken)
S(NameWithDot)
E(function_name)
A(WriteFunctionProposition)
S(FunctionFound)
true
true""".split('\n')

expected3 = """S(state0)
E(machine_type)
A(WriteDefine)
A(SaveMachineType)
S(MachineType)
E(machine_name)
A(WriteToken)
S(MachineName)
E(dot)
A(WriteToken)
S(NameWithDot)
E(function_name)
A(WriteFunctionProposition)
S(FunctionFound)
true
true""".split('\n')


def test_APParser():
    diagramService = DiagramHelper()
    automatonService = AutomatonHelper()
    verifierService = VerifierHelper(automatonService)
    diagram = diagramService.parseDiagram("./data/APParser.xstd")
    automaton = automatonService.createFromDiagram(diagram)

    formula = "G ('E(machine_type)' -> X G('E(machine_type)' -> X 'S(NameWithArrow)'))"
    ltl = ltlParse(formula)
    counterexample1 = verifierService.verify(automaton, ltl)

    formula = "G('S(FunctionFound)' -> F('A(WriteFunctionProposition)'))"
    ltl = ltlParse(formula)
    counterexample2 = verifierService.verify(automaton, ltl)

    formula = "'S(FunctionFound)' R !'S(FunctionFound)'"
    ltl = ltlParse(formula)
    counterexample3 = verifierService.verify(automaton, ltl)

    assert counterexample1 == expected1
    assert counterexample2 == expected2
    assert counterexample3 == expected3
