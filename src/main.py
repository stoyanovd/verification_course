import sys
from optparse import OptionParser

from src.ltlParser import ltlParse
from src.AutomatonHelper import AutomatonHelper
from src.DiagramHelper import DiagramHelper
from src.VerifierHelper import VerifierHelper


def parse():
    parser = OptionParser()
    parser.add_option('-f', "--file", dest="file", help='File with LTL formulae to check(one at line)', default="")
    parser.add_option('-l', "--ltl", dest="ltl", help='LTL formula as command line argument', default="")
    parser.add_option('-m', "--model", dest="model", help='Filename of a model file(Harel automaton in XSTD format)')

    (options, args) = parser.parse_args()

    if not options.file and not options.ltl:
        print("Either --file or --ltl must be specified")
        parser.print_help()
        sys.exit(-1)

    return options


class Validator(object):
    def __init__(self, modelFilename):
        self.diagramService = DiagramHelper()
        self.automatonService = AutomatonHelper()
        self.verifierService = VerifierHelper(self.automatonService)
        self.diagram = self.diagramService.parseDiagram(modelFilename)
        self.automaton = self.automatonService.createFromDiagram(self.diagram)

    def validate(self, formula: str):
        ltl = ltlParse(formula)
        if ltl:
            counterexample = self.verifierService.verify(self.automaton, ltl)
            if counterexample:
                print('Counterexample for the formula: ' + formula + ":")
                print(self.verifierService.exampleToString(counterexample))
            else:
                print('The ltl formula is correct for the automaton.')
        else:
            print('"Errors occurred while parsing ltl formula: ' + formula)


def main():
    options = parse()

    validator = Validator(options.model)

    if options.ltl:  # one formula from arguments
        validator.validate(options.ltl)
    else:  # one formula per line from file
        with open(options.file) as f:
            for formula in f.readlines():
                validator.validate(formula.rstrip())


if __name__ == "__main__":
    main()
