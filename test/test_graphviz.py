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


def check_antiDima():
    expected = """digraph AChart {
\trankdir = LR;
\ts0 [label="state0"]
\ts4 -> s0;
\ts13 -> s0;
\ts0 -> s3;
\ts0 -> s5;
\ts4 [shape="none", label=<<table><tr><td>Event</td><td>number</td></tr><tr><td colspan="2"></td></tr><tr><td colspan="2">Actions:</td></tr><tr><td>1.</td><td>SetID</td></tr></table>>]
\ts13 [shape="none", label=<<table><tr><td>Event</td><td>quote</td></tr><tr><td colspan="2">We see quotation symbol</td></tr><tr><td colspan="2">Actions:</td></tr><tr><td>1.</td><td>SetName</td></tr></table>>]
\ts3 [shape="none", label=<<table><tr><td>Event</td><td>id</td></tr><tr><td colspan="2">We see the word "id"</td></tr></table>>]
\ts5 [shape="none", label=<<table><tr><td>Event</td><td>name</td></tr><tr><td colspan="2">We see the word "name"</td></tr></table>>]
\ts1 [label="ID"]
\ts3 -> s1;
\ts1 -> s4;
\ts2 [label="SName"]
\ts5 -> s2;
\ts2 -> s8;
\ts8 [shape="none", label=<<table><tr><td>Event</td><td>quote</td></tr><tr><td colspan="2">We see quotation symbol</td></tr></table>>]
\ts7 [label="SText"]
\ts8 -> s7;
\ts12 -> s7;
\ts7 -> s12;
\ts7 -> s13;
\ts12 [shape="none", label=<<table><tr><td>Event</td><td>*</td></tr><tr><td colspan="2">No event</td></tr><tr><td colspan="2">Actions:</td></tr><tr><td>1.</td><td>AddToken</td></tr></table>>]
}
"""

    with open('./temp/diagram/AChart.xstd.dot') as f:
        lines = f.readlines()

    assert ''.join(lines) == expected


def test_generateDiagrams(env: Env):
    for xstdFile in getDataFiles():
        file = os.path.basename(xstdFile)
        diagram = env.diagramService.parseDiagram(xstdFile)
        dotFile = os.path.join(tempDiagramDir, file + ".dot")
        env.diagramService.convertDiagramToDot(diagram, dotFile)
        pdfFile = os.path.join(tempDiagramDir, file + ".pdf")
        execDot(dotFile, pdfFile)

    check_antiDima()


def test_generateAutomatons(env: Env):
    for xstdFile in getDataFiles():
        file = os.path.basename(xstdFile)
        diagram = env.diagramService.parseDiagram(xstdFile)
        graph = env.automatonService.createFromDiagram(diagram)
        dotFile = os.path.join(tempGraphDir, file + ".dot")
        env.automatonService.saveAsDot(graph, dotFile)
        pdfFile = os.path.join(tempGraphDir, file + ".pdf")
        execDot(dotFile, pdfFile)
