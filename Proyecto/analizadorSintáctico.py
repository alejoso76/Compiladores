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

#
def p_program(p):
    'program : PHPDECLARATION lista_declaraciones PHPCLOSING'
    pass

def p_lista_declaraciones(p):
   '''lista_declaracion : lista_declaraciones  declaracion
   					   | declaracion
   '''
   pass    

def p_declaracion(p):
	'''declaracion : var_declaracion
				   | fun_declaracion
				   | area fun_declaracion
				   | header_declaracion
				   | class_declaracion
				   | echo_stmt
				   | selection_stmt
			       | iteration_stmt
				   | typeclass
	'''
	pass    

