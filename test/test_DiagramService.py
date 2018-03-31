import pytest

from src.DiagramHelper import DiagramHelper


@pytest.fixture(scope='module')
def diagramService():
    return DiagramHelper()


def test_readFromFile(diagramService):
    diagram = diagramService.parseDiagram("data/VarParser.xstd")
    assert 21 == len(diagram.widget), "Widget number"
