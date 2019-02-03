import sys
import ply.yacc as yacc
from phpLEXER import tokens

VERBOSE = 1
val = False
#Esta lista de precedencia evita warnings por no usar tokens
precedence = (
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
)

#<?php Programa ?>
def p_program(p):
    'program : OPENTAG declaration_list CLOSETAG'
    pass

#Declaracion de todo el programa php
def p_declaration_list(p):
   '''declaration_list : declaration_list  declaration
   					   | declaration
   '''
   pass

#Distintas declaraciones dentro del programa
def p_declaration(p):
	'''declaration : var_declaration
				   | fun_declaration
				   | area fun_declaration
				   | header_declaration
				   | class_declaration
				   | echo_stmt
				   | selection_stmt
			       | iteration_stmt
				   | typeclass
	'''
	pass

#Impresiones echo
def p_echo_stmt(p):
	'''echo_stmt : echo_stmt ECHO STRING SEMI
				 | echo_stmt ECHO IDVAR SEMI
				 | empty
				 | echo_stmt ECHO NUM SEMI
				 | echo_stmt ECHO boolean SEMI
				 | echo_stmt ECHO fun_declaration SEMI
	'''
	pass

#Require e include
def p_header_declaration(p):
	'''header_declaration : REQUIRE LPAREN STRING RPAREN SEMI
                          | INCLUDE LPAREN STRING RPAREN SEMI
    '''
	pass

#Declaracion de clases
def p_class_declaration(p):
	'''class_declaration : area CLASS ID LBLOCK attribute RBLOCK
						 | CLASS ID LBLOCK attribute RBLOCK
	'''
	pass

#Declaracion de atributos
def p_attribute1(p):
	'''attribute : attribute area var_declaration
				 | area var_declaration
				 | attribute area fun_declaration
				 | area fun_declaration
	'''
	pass

#Encapsulamiento de clases
def p_area(p):
	'''area : PRIVATE
			| PUBLIC
			| PROTECTED
	'''
	pass

#Declaracion de variables
def p_var_declaration(p):
	'''var_declaration : IDVAR SEMI var_declaration
                       | IDVAR SEMI
                       | TIMESTIMES IDVAR SEMI
                       | TIMESTIMES IDVAR SEMI var_declaration
                       | IDVAR EQUAL NUM SEMI var_declaration
                       | IDVAR EQUAL NUM SEMI
                       | IDVAR EQUAL boolean SEMI var_declaration
                       | IDVAR EQUAL boolean SEMI
                       | IDVAR EQUAL IDVAR SEMI var_declaration
                       | IDVAR EQUAL IDVAR SEMI
                       | AMPERSANT IDVAR SEMI var_declaration
                       | AMPERSANT IDVAR EQUAL IDVAR SEMI  selection_stmt
                       | AMPERSANT IDVAR SEMI
                       | IDVAR EQUAL simple_expression SEMI
	'''
	pass

#Declaracion de funciones
def p_fun_declaration(p):
	'''fun_declaration : FUNCTION ID LPAREN params RPAREN
					   | FUNCTION ID LPAREN params RPAREN compount_stmt
	'''
	pass

#Parametros
def p_params(p):
	'''params : param_list
			  | empty
	'''
	pass

#Lista de parametros
def p_param_list(p):
	'''param_list : param_list COMMA param_list
				  | param
	'''
	pass

#Parametros solos
def p_param(p):
	'''param : IDVAR
             | IDVAR LBRACKET RBRACKET
    '''
	pass

#Formatos compuestos
def p_compount_stmt(p):
	'compount_stmt : LBLOCK echo_stmt local_declarations echo_stmt statement_list echo_stmt RBLOCK'
	pass

#Declaraciones locales
def p_local_declarations(p):
	'''local_declarations : local_declarations var_declaration
						  | empty
	'''
	pass

#Lista de declaraciones
def p_statement_list(p):
	'''statement_list : statement_list statement
					  | empty
	'''
	pass

#Declaraciones
def p_statement(p):
	'''statement : expression_stmt
				 | compount_stmt
				 | selection_stmt
				 | iteration_stmt
			     | return_stmt
			     | class_declaration
				 | echo_stmt
	'''
	pass

#Semi
def p_expression_stmt(p):
	'expression_stmt : expression SEMI'
	pass

#Condicional if
def p_selection_stmt_1(p):
	'''selection_stmt : IF LPAREN expression RPAREN statement
					  | IF LPAREN expression RPAREN statement selection
	'''
	pass

#Else y elseif
def p_selection(p):
	'''selection : ELSE statement
				 | ELSEIF statement selection
	 '''
	pass

#Switch, case, default
def p_selection_stmt_2(p):
	'''selection_stmt : SWITCH LPAREN var RPAREN statement
					  | CASE NUM COLON statement BREAK SEMI
					  | DEFAULT COLON statement BREAK SEMI
	'''
	pass

#For
def p_iteration_stmt_1(p):
	'iteration_stmt : FOR LPAREN var_declaration SEMI expression SEMI additive_expression RPAREN statement '
	pass

#While    
def p_iteration_stmt_2(p):
	'iteration_stmt : WHILE LPAREN expression RPAREN statement'
	pass

#Do while
def p_iteration_stmt_3(p):
	'iteration_stmt : DO LBLOCK statement SEMI RBLOCK WHILE LPAREN expression RPAREN'
	pass

#Return
def p_return_stmt(p):
	'''return_stmt : RETURN SEMI
				   | RETURN expression SEMI
	'''
	pass

#Operaciones logicas e igualdades
def p_expression(p):
	'''expression : var EQUAL expression
				  | simple_expression
				  | var EQUAL AMPERSANT IDVAR
			      | expression AND expression
				  | expression OR expression
	'''
	pass

#Idvar
def p_var(p):
	'''var : IDVAR
		   | IDVAR LBRACKET expression RBRACKET
	'''
	pass

#Expresion simple
def p_simple_expression(p):
	'''simple_expression : additive_expression relop additive_expression
						 | additive_expression
	'''
	pass

#Comparadores
def p_relop(p):
	'''relop : LESS
			 | LESSEQUAL
			 | GREATER
			 | GREATEREQUAL
			 | DEQUAL
			 | DISTINT
			 | ISEQUAL
	'''
	pass

#Suma y resta 1
def p_additive_expression(p):
	'''additive_expression : additive_expression addop term
    					   | term
    					   | term MINUSMINUS
    				       | term PLUSPLUS
	'''
	pass

#Suma y resta
def p_addop(p):
	'''addop : PLUS
			 | MINUS
	'''
	pass

#Definicion operacion *, /
def p_term(p):
	'''term : term mulop factor
			| factor
	'''
	pass

#Multiplicacion y division
def p_mulop(p):
	'''mulop : TIMES
			 | DIVIDE
	'''
	pass

#Factor
def p_factor(p):
	'''factor : LPAREN expression RPAREN
			  | var
			  | NUM
			  | boolean
			  | IDVAR LPAREN args RPAREN
	'''
	pass

#Argumentos
def p_args(p):
	'''args : args_list
			| empty
			| VOID
	'''
	pass

#Lista de argumentos
def p_args_list(p):
	'''args_list : args_list COMMA expression
				 | expression
	'''
	pass

#Valores booleanos
def p_boolean(p):
	'''boolean : TRUE
			   | FALSE
	'''
	pass

#Tipo de clase
def p_tclass(p):
	'typeclass : ID IDVAR EQUAL NEW constructor SEMI'
	pass

#Constructor
def p_costructor(p):
	'''constructor : ID LPAREN RPAREN
				   | ID LPAREN args RPAREN
	'''
	pass

#Vacio
def p_empty(p):
	'empty :'
	pass

#Error
def p_error(p):
    if VERBOSE:
        val = True
        if p is not None:
            print "\t ERROR de sintaxis - Token inesperado."
            print "\tLinea: "+str(p.lexer.lineno)+"\t=> "+str(p.value)
        else:
            print "\t ERROR de sintaxis."
            print "\tLinea:  "+str(php_lexer.lexer.lineno)

    else:
        raise Exception('syntax', 'error')

parser = yacc.yacc()


if __name__ == '__main__':

    if (len(sys.argv) > 1):
 	    fin = sys.argv[1]
    else:
 	    fin = 'pruebaPHP.php'

    f = open(fin, 'r')
    data = f.read()
    parser.parse(data, tracking=True)
    if not val :
 	    print("Analisis sintactico correcto.")