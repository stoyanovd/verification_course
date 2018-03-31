from src.LTLIntersector import LTLIntersector
from src.model.buchi.Automaton import Automaton
from src.model.ltl.Formula import Formula
from src.model.ltl.LTL import LTL
from src.AutomatonHelper import AutomatonHelper


class VerifierHelper(object):
    def __init__(self, automatonService: AutomatonHelper):
        self.automatonService = automatonService

    def verify(self, automaton: Automaton, ltl: Formula) -> list:
        ltlAutomaton = self.automatonService.createFromLtl_formula(LTL.not_(ltl))
        intersector = LTLIntersector()
        c = self.automatonService.intersect(automaton, ltlAutomaton, intersector)
        example = c.findPath()
        return example

    def exampleToString(self, example: list) -> str:
        return '\n'.join([str(s) for s in example])
