from abc import abstractmethod

class LTLVisitor(object):

    @abstractmethod
    def visit_BinaryFormula(self, binary: 'BinaryFormula') -> None:
        pass

    @abstractmethod
    def visit_Const(self, c: 'Const') -> None:
        pass

    @abstractmethod
    def visit_Not(self, formula: 'Not') -> None:
        pass

    @abstractmethod
    def visit_Next(self, formula: 'Next') -> None:
        pass

    @abstractmethod
    def visit_Variable(self, variable: 'Variable') -> None:
        pass
