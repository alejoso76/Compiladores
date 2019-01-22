import ply.yacc as yacc
import os
import analizadorLexico.py import tokens


precendence = {
    ('left', 'INCLUDE', 'REQUIRE'),
    ('left', 'COMMA'),
    ('left', 'EQUAL', 'PLUSEQUAL', 'MINUSEQUAL'),
    ('left', 'SEMI'),
    ('left', 'OR'),
    ('left', 'XOR'),
    ('left', 'AND'),
    ('nonassoc', 'ISEQUAL', 'DEQUAL'),
    ('nonassoc', 'LESS', 'LESSEQUAL', 'GREATER', 'GREATEREQUAL'),
    ('left', 'PLUS', 'MINUS'),
    ('right', 'LBRACKET'),
    ('nonassoc', 'NEW', 'CLONE'),
    ('left', 'ELSEIF'),
    ('left', 'ELSE'),
    ('right', 'PRIVATE', 'PROTECTED', 'PUBLIC'),
}