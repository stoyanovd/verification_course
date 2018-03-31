from src.model.ltl.Formula import Formula


class Transition:
    expression: Formula
    stateName: str

    def __init__(self, expression: Formula, stateName: str):
        self.expression = expression
        self.stateName = stateName
