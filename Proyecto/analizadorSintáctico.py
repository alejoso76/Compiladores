import ply.yacc as yacc
import os
import sys
from analizadorLexico import tokens

VERBOSE = 1
'''
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
'''

val=False
#<?PHP Lista de declaracion de sentencias ?>
def p_program(p):
    'program : PHPDECLARATION declaracion_sentencias PHPCLOSING'
    pass


#def p_inicio(p):
 #   '''inicio : import declaracion_sentencias
  #              | import
   #             | declaracion_sentencias'''
    #pass


#Todas las posibles combinaciones
def p_declaracion_sentencias(p):
    '''declaracion_sentencias : sentencias declaracion_sentencias
                                | sentencias'''
    pass

#Todas las sentencias dentro de un programa de php
def p_sentencias(p):
    '''sentencias : sentassign
                    | call_function SEMICOLON
                    | sentif
                    | sentecho
                    | sentfunc
                    | sentreturn
                    | sentfor
                    | sentwhile
                    | sentdowhile
                    '''
    pass

#Sentencia return
def p_sentreturn(p):
    '''sentreturn : RETURN type SEMICOLON
                    | RETURN cond SEMICOLON'''

#Sentencia echo
def p_sentecho(p):
    '''sentecho : ECHO typevar SEMICOLON
                | ECHO exp SEMICOLON
                | ECHO cond SEMICOLON'''
    pass

#Sentencia if
def p_sentif(p):
    '''sentif : IF genif auxsentif'''
    pass

#Sentencia else if, else
def p_auxsentif(p):
    '''auxsentif : ELSE IF genif auxsentif
                    | ELSE OCBRACKET declaracion_sentencias CCBRACKET
                    | empty'''
    pass

#Sentencia para generar el condicional del if
def p_generatorif(p):

    '''genif : OPARENTHESIS cond CPARENTHESIS OCBRACKET declaracion_sentencias CCBRACKET'''
    pass

#Sentencias de asignaciones
def p_sentassign(p):
    '''sentassign :  ID EQUAL exp SEMICOLON
                    | ID PLUSPLUS SEMICOLON
                    | ID MINUSMINUS SEMICOLON'''
    pass


#Sentencias para expresiones logicas
#True y false
def p_booleanos(p):
    '''bool : TRUE
            | FALSE '''
    pass

#And, or, xor, not
def p_operadoreslogicos(p):
    '''oplogicos : AND
                    | OR
                    | XOR
                    | NOT '''
    pass

#Sentencias para expresiones de comparacion entre elementos
def p_exp(p):
    '''exp : expsimple  opcomparacion  expsimple
            | OPARENTHESIS expsimple  opcomparacion  expsimple CPARENTHESIS
            | expsimple'''
    pass

#Comparadores
def p_opcomparacion(p):
    '''opcomparacion : EQUALE
                        | DEQUAL
                        | IDENTIC
                        | GREAT
                        | GREATE
                        | LESS
                        | LESSE'''
    pass                        

#Expresiones matematicas
def p_expression_simple(p):
    '''expsimple :  expsimple  opsuma term
                | term'''
    pass

#Multiplicacion o division o potencia
def p_term(p):
    '''term : term opmult factor
            | factor'''
    pass

#Factor
def p_factor(p):
    '''factor : NUMBER
                | ID
                | call_function
                | OPARENTHESIS expsimple CPARENTHESIS'''
    pass

#Tipo de variable
def p_typevar(p):
    '''typevar : NUMBER
                | STRINGWR
                | STRINGGWR
                | TRUE
                | FALSE'''
    pass

#Operacion suma o resta
def p_opsuma(p):
    '''opsuma : PLUS
                | SCORE '''
    pass

#/, *, %, **
def p_opmult(p):
    '''opmult : TIMES
                | SLASH
                | PERCENTAGE
                | POW '''
    pass

#Comparaciones, operaciones logicas
def p_cond(p):
    '''cond : type
            | cond opcomparacion cond
            | cond oplogicos cond
            | OPARENTHESIS type CPARENTHESIS
            | OPARENTHESIS cond CPARENTHESIS'''
    pass

#Declaracion tipo variable
def p_type(p):
	'''type : typevar
				| var_declaration_gen'''
	pass

#Generacion de declaracion de variables
def p_var_declaration_gen(p):
	'''var_declaration_gen : ID
    						| ID PLUSPLUS
                            | ID MINUSMINUS
    						| MINUSMINUS  ID
                            | PLUSPLUS ID
    						| typevar
                            | exp '''
	pass

#Argumentos
def p_arg(p):
	'''arg : var_declaration_gen
			| type
			| expsimple
			| type COMMA arg
			| STRINGWR
            | STRINGGWR
			| var_declaration_gen COMMA arg
			| STRINGWR COMMA arg
            | STRINGGWR COMMA arg
            |'''
	pass

#Argumentos 2
def p_arg2(p):
	'''argfunc : ID
			| ID COMMA argfunc
            |'''
	pass

#Declaracion funcionees
def p_sentfunc(p):
    '''sentfunc : FUNCTION NAMEFUNCTION OPARENTHESIS argfunc CPARENTHESIS OCBRACKET declaracion_sentencias CCBRACKET'''
    pass

#Llamado funciones
def p_call_function(p):
	'''call_function : NAMEFUNCTION
						| NAMEFUNCTION OPARENTHESIS arg CPARENTHESIS'''
	pass

#Ciclos
#For
def p_sentfor(p):
    '''sentfor : FOR OPARENTHESIS ID EQUAL expsimple SEMICOLON cond SEMICOLON expsimple  CPARENTHESIS OCBRACKET  declaracion_sentencias CCBRACKET
                | FOR OPARENTHESIS ID EQUAL expsimple SEMICOLON cond SEMICOLON ID PLUSPLUS  CPARENTHESIS OCBRACKET  declaracion_sentencias CCBRACKET
                | FOR OPARENTHESIS ID EQUAL expsimple SEMICOLON cond SEMICOLON ID MINUSMINUS  CPARENTHESIS OCBRACKET  declaracion_sentencias CCBRACKET'''
    pass

#While
def p_sentwhile(p):
    '''sentwhile : WHILE OPARENTHESIS cond CPARENTHESIS OCBRACKET declaracion_sentencias CCBRACKET '''
    pass

#Do while
def p_sentdowhile(p):
    '''sentdowhile : DO OCBRACKET  declaracion_sentencias CCBRACKET WHILE OPARENTHESIS cond CPARENTHESIS SEMICOLON'''
    pass

#Importaciones
#def p_import(p):
  #  '''import : INCLUDE STRINGGWR SEMICOLON'''
   # pass

#Vacio
def p_empty(p):
    'empty : '
    pass

#Regla para error de sintaxis
def p_error(p):
    global val
    val = True
    if p is None:
        print('Error de sintaxis')
    else:
        print('ERROR DE SINTAXIS en la linea')

# Build the parser
parser = yacc.yacc()

if __name__ == '__main__':

	if (len(sys.argv) > 1):
		fin = sys.argv[1]
	else:
		fin = 'pruebaPHP.php'

	f = open(fin, 'r')
	data = f.read()
	#print (data)
	parser.parse(data, tracking=True)
	if not val :
		print("Analisis sintactico completado sin errores.")
	#input()