import ply.yacc as yacc
import os
import sys
from analizadorLexico.py import tokens

VERBOSE = 1

precendence = {
    ('left', 'INCLUDE', 'REQUIRE'),
    ('left', 'COMMA'),
    ('left', 'EQUAL',),
    ('left', 'SEMICOLON'),
    ('left', 'OR'),
    ('left', 'XOR'),
    ('left', 'AND'),
    ('nonassoc', 'EQUAL', 'DEQUAL'),
    ('nonassoc', 'LESS', 'LESSE', 'GREAT', 'GREATERE'),
    ('left', 'PLUS', 'SCORE'),
    ('right', 'OSBRACKET'),
    ('nonassoc', 'NEW', 'CLONE'),
    ('left', 'ELSEIF'),
    ('left', 'ELSE'),
    ('right', 'PRIVATE', 'PROTECTED', 'PUBLIC'),
}
