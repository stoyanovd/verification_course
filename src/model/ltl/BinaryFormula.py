from src.model.ltl.Formula import Formula
from src.model.ltl.LTLVisitor import LTLVisitor


class BinaryFormula(Formula):
    operation = 1
    left: Formula
    right: Formula

    def __init__(self, operation, left: Formula, right: Formula):
        self.operation = operation
        self.left = left
        self.right = right

    def __str__(self):
        return "(" + str(self.left) + " " + str(self.operation) + " " + str(self.right) + ")"

    def toNormalForm(self, negation: bool) -> 'Formula':
        if negation:
            return self.operation.toNormalForm(self, self.left, self.right)
        else:
            return BinaryFormula(self.operation, self.left.toNormalForm(False), self.right.toNormalForm(False))

    def map_(self, mapper) -> 'Formula':
        return BinaryFormula(self.operation, self.left.map_(mapper), self.right.map_(mapper))

    def accept(self, visitor: LTLVisitor) -> None:
        visitor.visit_BinaryFormula(self)

    def negation(self) -> 'Formula':
        return self
