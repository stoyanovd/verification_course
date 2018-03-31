import logging
import os

import pytest

from src.ltlParser import ltlParse
from src.model.ltl.LTL import LTL
from src.AutomatonHelper import AutomatonHelper
from src.DiagramHelper import DiagramHelper
from src.VerifierHelper import VerifierHelper

log = logging.getLogger()

dataDir = 'data'


class Env(object):
    def __init__(self):
        self.automatonService = AutomatonHelper()
        self.diagramService = DiagramHelper()
        self.verifierService = VerifierHelper(self.automatonService)


@pytest.fixture(scope="module")
def env():
    return Env()


def getModelNames():
    for path in os.listdir(dataDir):
        filename, extension = os.path.splitext(os.path.basename(path))
        if extension == '.xstd':
            yield filename


def resolve(model: str, extension: str):
    return os.path.join(dataDir, model + extension)


# a: Automaton<Formula<String>>, ltl: str(File),
def check(env: Env, a, ltl, iscorrect: bool) -> None:
    if not os.path.exists(ltl):
        return

    with open(ltl) as f:
        formula = f.readline()
        log.info("Checking " + ("correct" if iscorrect else "incorrect") + " formula: " + formula)

        f = ltlParse(formula)
        ex = env.verifierService.verify(a, f)

        if iscorrect:
            assert not ex
        else:
            assert ex


def test_verify(env: Env):
    for model in getModelNames():
        log.info('Testing model ' + model)
        modelFile = resolve(model, '.xstd')
        diagram = env.diagramService.parseDiagram(modelFile)

        automaton = env.automatonService.createFromDiagram(diagram)

        correct = resolve(model, '.ltl.correct')
        incorrect = resolve(model, '.ltl.incorrect')

        check(env, automaton, correct, True)
        check(env, automaton, incorrect, False)


def test_verifyExample(env: Env):
    ltl = LTL.future(LTL.var('S(Dot)'))
    diagram = env.diagramService.parseDiagram("data/VarParser.xstd")
    automaton = env.automatonService.createFromDiagram(diagram)
    iterable = env.verifierService.verify(automaton, ltl)

    if not iterable:
        for f in iterable:
            log.info(str(f))
