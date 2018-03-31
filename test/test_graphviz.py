import logging
import os
import subprocess

import pytest

from src.DiagramHelper import DiagramHelper
from src.AutomatonHelper import AutomatonHelper

log = logging.getLogger()

dataDir = 'data'
tempDiagramDir = os.path.join('temp', 'diagram')
tempGraphDir = os.path.join('temp', 'graph')


class Env(object):
    def __init__(self):
        self.diagramService = DiagramHelper()
        self.automatonService = AutomatonHelper()


@pytest.fixture(scope='module')
def env():
    return Env()


def getDataFiles():
    os.makedirs(dataDir, exist_ok=True)
    os.makedirs(tempDiagramDir, exist_ok=True)
    os.makedirs(tempGraphDir, exist_ok=True)

    for path in os.listdir(dataDir):
        if path.endswith('.xstd'):
            yield os.path.join(dataDir, path)


def execDot(dotFile, pdfFile):
    command = ["dot", "-Gsplines=true", "-Goverlap=false", "-Tpdf", dotFile, "-o", pdfFile]

    subprocess.call(command, cwd=os.getcwd()) == 0


def test_generateDiagrams(env: Env):
    for xstdFile in getDataFiles():
        file = os.path.basename(xstdFile)
        diagram = env.diagramService.parseDiagram(xstdFile)
        dotFile = os.path.join(tempDiagramDir, file + ".dot")
        env.diagramService.convertDiagramToDot(diagram, dotFile)
        pdfFile = os.path.join(tempDiagramDir, file + ".pdf")
        execDot(dotFile, pdfFile)


def test_generateAutomatons(env: Env):
    for xstdFile in getDataFiles():
        file = os.path.basename(xstdFile)
        diagram = env.diagramService.parseDiagram(xstdFile)
        graph = env.automatonService.createFromDiagram(diagram)
        dotFile = os.path.join(tempGraphDir, file + ".dot")
        env.automatonService.saveAsDot(graph, dotFile)
        pdfFile = os.path.join(tempGraphDir, file + ".pdf")
        execDot(dotFile, pdfFile)
