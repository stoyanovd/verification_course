grammar Buchi;

@header {
from src.model.buchi.State import State
from src.model.buchi.Transition import Transition
from src.model.ltl.LTL import LTL
}

compilationUnit returns [list<State> states_list]
@init
{$states_list = []}:
'never' '{' (((stateDefinition {$states_list.append($stateDefinition.s);})* | empty) '}' ) EOF;

stateDefinition returns [State s]
@init
{transitions_list = []}:
    stateName ':' ('skip' | empty | ('if' (transition {transitions_list.append($transition.t);})+ 'fi' ';'))
    {name_str = $stateName.text;$s = State(name_str, transitions_list);}
    ;

stateName: StringLiteral;

transition returns [Transition t]:
    '::' expression '->' 'goto' stateName
    {$t = Transition($expression.f, $stateName.text);}
    ;

expression returns [Formula<String> f]:
        |   '(' expression ')'
        {$f = $expression.f;}
        |   literal
        {$f = LTL.var($literal.text);}
        |   unaryOperator='!' expression
        {$f = LTL.not_($expression.f);}
        |   left=expression binaryOperator='&&' right=expression
        {$f = LTL.and_($left.f, $right.f);}
        |   left=expression binaryOperator='||' right=expression
        {$f = LTL.or_($left.f, $right.f);}
        |   unit
        {$f = LTL.t();}
        ;

empty
    : false;

unit
    : Unit;

literal
    : StringLiteral;

WS  :	[ \t\r\n\f] -> skip;

BlockComment
    :   '/*' .*? '*/'
        -> skip
    ;

false
    :   'false;'
    ;

StringLiteral
	:	[a-zA-Z][a-zA-Z0-9_]*
	;

Unit
    :   '1'
    ;


