from collections import defaultdict

# constants for dfs
WHITE = None
GRAY = 1
BLACK = 2


class Automaton(object):
    def __init__(self):
        self.acceptingSet = set()
        self.nodes = set()
        self.automaton = defaultdict(lambda: defaultdict(list))

        self.initialState = 0

    def __eq__(self, other):
        return self.acceptingSet == other.acceptingSet and \
               self.nodes == other.nodes and \
               self.automaton == other.automaton and \
               self.initialState == other.initialState

    def addTransition(self, stateA: int, stateB: int, symbol: 'T') -> None:
        self.checkState(stateA)
        self.checkState(stateB)
        self.nodes.add(stateA)
        self.nodes.add(stateB)
        outgoings = self.get(stateA)

        outgoings[symbol].append(stateB)

    def setAccepting(self, state: int) -> None:
        self.checkState(state)
        self.nodes.add(state)
        self.acceptingSet.add(state)

    def isAccepting(self, state: int) -> bool:
        return state in self.acceptingSet

    def checkState(self, state: int) -> None:
        pass

    def get(self, stateId: int) -> dict:
        return self.automaton[stateId]

    def size(self) -> int:
        return len(self.nodes)

    def findPath(self) -> list:
        color1 = dict()
        color2 = dict()
        path = list()
        self.dfs(self.initialState, color1, color2, path)
        return path

    def dfs(self, v: int, color1: dict, color2: dict, path: list):
        color1[v] = GRAY
        for symbol, values in self.get(v).items():
            for u in values:
                # is WHITE from JAVA
                if color1.get(u) == WHITE:
                    path.append(symbol)
                    if self.dfs(u, color1, color2, path):
                        return True
                    path.pop()

        if self.isAccepting(v):
            if self.dfs_internal(v, color1, color2, path):
                return True

        color1[v] = BLACK
        return False

    def dfs_internal(self, v: int, color1: dict, color2: dict, path: list):
        color2[v] = GRAY

        for symbol, values in self.get(v).items():
            for u in values:
                if color1.get(u) == GRAY:
                    path.append(symbol)
                    return True

                if color2.get(u) == WHITE:
                    path.append(symbol)
                    if self.dfs_internal(u, color1, color2, path):
                        return True
                    path.pop()
        color2[v] = BLACK
        return False
