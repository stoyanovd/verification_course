from src.model.ltl.BinaryFormula import BinaryFormula
from src.model.ltl.Formula import Formula


class BinaryOperation(object):
    # Transforms negation of the corresponding formula
    @staticmethod
    def toNormalForm(left: Formula, right: Formula) -> Formula:
        raise Exception('Not Implemented')

    def __str__(self):
        raise Exception('Not Implemented')

    def __eq__(self, other):
        return str(self) == str(other)


class R(BinaryOperation):
    @staticmethod
    def toNormalForm(left: Formula, right: Formula) -> Formula:
        return BinaryFormula(U(), left.toNormalForm(True), right.toNormalForm(True))

    def __str__(self):
        return 'R'


class U(BinaryOperation):
    @staticmethod
    def toNormalForm(left: Formula, right: Formula) -> Formula:
        return BinaryFormula(R(), left.toNormalForm(True), right.toNormalForm(True))

    def __str__(self):
        return 'U'


class OR(BinaryOperation):
    @staticmethod
    def toNormalForm(left: Formula, right: Formula) -> Formula:
        return BinaryFormula(AND(), left.toNormalForm(True), right.toNormalForm(True))

    def __str__(self):
        return "||"


class AND(BinaryOperation):
    @staticmethod
    def toNormalForm(left: Formula, right: Formula) -> Formula:
        return BinaryFormula(OR(), left.toNormalForm(True), right.toNormalForm(True))

    def __str__(self):
        return "&&"
