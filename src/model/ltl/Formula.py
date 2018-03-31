import types
from abc import abstractmethod

from src.model.ltl.LTLVisitor import LTLVisitor


class Formula(object):
    def toNormalForm_false(self) -> 'Formula':
        return self.toNormalForm(False)

    # Transforms formulae to the negative normal form
    @abstractmethod
    def toNormalForm(self, negation: bool) -> 'Formula':
        pass

    @abstractmethod
    def map_(self, mapper: types.FunctionType) -> 'Formula':
        pass

    @abstractmethod
    def accept(self, visitor: LTLVisitor) -> None:
        pass

    @abstractmethod
    def negation(self) -> 'Formula':
        pass

    @abstractmethod
    def __str__(self) -> str:
        pass

    def __eq__(self, other):
        return str(self) == str(other)

    def __hash__(self):
        return hash(str(self))
