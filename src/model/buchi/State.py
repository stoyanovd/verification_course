class State:
    ORDINARY = 0
    INITIAL = 1
    FINAL = 2
    name: str
    transitions: list

    def __init__(self, name: str, transitions: list):
        self.name = name
        self.transitions = transitions
