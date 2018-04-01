import os
import subprocess
import types
import typing
from collections import defaultdict

import bidict

import itertools

from antlr4 import IllegalStateException
from antlr4 import InputStream

from model.buchi.BuchiLexer import BuchiLexer, CommonTokenStream
from model.buchi.BuchiParser import BuchiParser
from src.model.buchi.Automaton import Automaton
from src.model.buchi.State import State
from src.model.ltl.Formula import Formula
from src.model.ltl.LTL import LTL
from src.Labels import L


class AutomatonHelper:
    def __init__(self):
        pass

    def createFromLtl_formula(self, ltl: Formula) -> Automaton:
        variable_map = defaultdict(lambda: "v" + str(len(variable_map)))
        lowercase_ltl = ltl.map_(lambda k: variable_map[k])
        spin = str(lowercase_ltl).replace("R", "V")
        old_names = bidict.bidict(variable_map).inv
        automaton = self.createFromLtl_str(spin)
        return self.map_(automaton, lambda t: t.map_(old_names.get))

    def createFromLtl_str(self, ltl: str) -> Automaton:
        states = self.createStateListFromLtl(ltl)
        ids = itertools.count()
        idMap = defaultdict(lambda: next(ids))
        automaton = Automaton()
        for state in states:
            nodeId = idMap[state.name]
            if self.isAcceptance(state.name):
                automaton.setAccepting(nodeId)
            if self.isInit(state.name):
                automaton.initialState = nodeId

            for transition in state.transitions:
                nextId = idMap[transition.stateName]
                formula = transition.expression
                automaton.addTransition(nodeId, nextId, formula)
                if self.isAcceptance(transition.stateName):
                    automaton.setAccepting(nextId)
                if self.isInit(transition.stateName):
                    automaton.initialState = nextId

        for nodeId in automaton.nodes:
            if len(automaton.get(nodeId)) == 0:
                automaton.addTransition(nodeId, nodeId, LTL.t())
        return automaton

    def parse(self, str_: str) -> list:
        inputStream = InputStream(str_)

        lexer = BuchiLexer(inputStream)
        tokens = CommonTokenStream(lexer)
        parser = BuchiParser(tokens)
        result = parser.compilationUnit()
        return result.states_list

    def createStateListFromLtl(self, ltl: str) -> typing.List[State]:
        ltl2ba_path = os.path.join("ltl2ba", "ltl2ba")
        if os.name == 'nt':  # is windows
            ltl2ba_path += '.exe'

        command = [ltl2ba_path, "-f", ltl]

        output = subprocess.check_output(command, cwd=os.getcwd()).decode('utf-8')
        return self.parse(output)

    def isAcceptance(self, name: str) -> bool:
        return name.startswith("accept_")

    def isInit(self, name: str) -> bool:
        return name.endswith("_init")

    def map_(self, input_: Automaton, mapper: types.FunctionType) -> Automaton:
        output_ = Automaton()
        for nodeId, successors in input_.automaton.items():
            for a, v in successors.items():
                b = mapper(a)
                for nextId in v:
                    output_.addTransition(nodeId, nextId, b)

        for nodeId in input_.acceptingSet:
            output_.setAccepting(nodeId)

        output_.initialState = input_.initialState
        return output_

    def createFromDiagram(self, diagram) -> Automaton:
        widgetMap = {w['id']: w for w in diagram.widget}
        successors = dict()
        for widget in diagram.widget:
            if widget['type'] == L.L_WIDGET_STATE:
                if not hasattr(widget.attributes, 'incoming'):
                    continue
                for incoming in widget.attributes.incoming:
                    prev = widgetMap.get(incoming['id'])
                    if prev['type'] == L.L_WIDGET_TRANSITION:
                        successors.update({incoming['id']: widget['id']})
                    else:
                        raise IllegalStateException('IllegalStateException')

        automaton = Automaton()
        ids = itertools.count(10000)
        initId = None
        for widget in diagram.widget:
            if widget['type'] == L.L_WIDGET_STATE:
                stateNode = int(widget['id'])
                if State.INITIAL == int(widget.attributes.type.cdata):
                    if initId is None:
                        initId = next(ids)
                        automaton.initialState = initId
                    stateEdge = self.createFormulaFromState(widget)
                    automaton.addTransition(initId, stateNode, stateEdge)

                if not hasattr(widget.attributes, 'outgoing'):
                    continue

                for outgoing in widget.attributes.outgoing:
                    next_ = widgetMap.get(outgoing['id'])
                    if next_['type'] == L.L_WIDGET_TRANSITION:
                        # event
                        eventEdge = self.createFormulaFromEvent(next_.attributes.event)
                        eventNodeId = next(ids)
                        automaton.addTransition(stateNode, eventNodeId, eventEdge)

                        lastNodeId = eventNodeId
                        # actions
                        if hasattr(next_.attributes, 'action'):
                            for action in next_.attributes.action:
                                actionEdge = self.createFormulaFromActions_action(action)
                                actionNodeId = next(ids)
                                automaton.addTransition(lastNodeId, actionNodeId, actionEdge)
                                lastNodeId = actionNodeId

                        # next state
                        successorId = successors.get(outgoing['id'])
                        nextState = widgetMap.get(successorId)
                        nextNode = int(nextState['id'])
                        nextEdge = self.createFormulaFromState(nextState)
                        automaton.addTransition(lastNodeId, nextNode, nextEdge)
                    else:
                        raise IllegalStateException('IllegalStateException2')

        for nodeId in automaton.nodes:
            automaton.setAccepting(nodeId)
            if len(automaton.get(nodeId)) == 0:
                automaton.addTransition(nodeId, nodeId, LTL.t())

        return automaton

    def createFormulaFromState(self, state) -> Formula:
        return LTL.var("S(" + state.attributes.name.cdata + ")")

    def createFormulaFromEvent(self, event) -> Formula:
        return LTL.var("E(" + event['name'] + ")")

    def createFormulaFromActions_action(self, action) -> Formula:
        return LTL.var("A(" + action['name'] + ")")

    def createFormulaFromActions_list(self, actions: list) -> Formula:
        if not actions:
            return LTL.t()

        # be accurate
        strings = list(map(self.createFormulaFromActions_action, actions))

        current = strings[0]
        for i in range(1, len(strings)):
            current = LTL.and_(current, strings[i])
        return current

    def saveAsDot(self, graph: Automaton, file_str: str) -> None:
        with open(file_str, 'w') as writer:
            print("digraph G {", file=writer)
            print("\trankdir = LR;", file=writer)
            for k, v in graph.automaton.items():
                nodeId = k
                succesors = v
                shape = ""
                if graph.isAccepting(nodeId):
                    shape = "doublecircle"
                else:
                    shape = "circle"

                print("\t" + L.PREFIX + str(nodeId) + "[shape=\"" + shape + "\"];", file=writer)
                for k, v in succesors.items():
                    symbol = k
                    next_ = v
                    for nextId in next_:
                        print(
                            "\t" + L.PREFIX + str(nodeId) + " -> " + L.PREFIX + str(nextId) + "[label=\"" + str(
                                symbol) + "\"]",
                            file=writer)

            print("}", file=writer)

    def intersect(self, a: Automaton, b: Automaton, intersector) -> Automaton:
        c = Automaton()
        tr = dict()
        # Build all transitions
        for i, iState in a.automaton.items():
            for j, jState in b.automaton.items():
                for iSymbol in iState.keys():
                    for jSymbol in jState.keys():
                        t = intersector.intersect(iSymbol, jSymbol)
                        if t is None:
                            continue

                        for is_ in iState.get(iSymbol):
                            for js in jState.get(jSymbol):
                                c.addTransition(self.convert(i, j, 0, tr),
                                                self.convert(is_, js, 1 if a.isAccepting(i) else 0, tr), t)
                                c.addTransition(self.convert(i, j, 1, tr),
                                                self.convert(is_, js, 0 if a.isAccepting(j) else 1, tr), t)

        # Accepting set of the new automaton
        for accB in b.acceptingSet:
            for i in a.automaton.keys():
                c.setAccepting(self.convert(i, accB, 1, tr))

        c.initialState = self.convert(a.initialState, b.initialState, 0, tr)
        return c

    def convert(self, stateA: int, stateB: int, flag: int, tr: dict) -> int:
        p = (stateA, stateB, flag)
        if p not in tr:
            tr[p] = len(tr)

        return tr[p]
