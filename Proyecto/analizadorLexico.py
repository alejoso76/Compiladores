import ply.lex as lex
import sys

tokens = {
    #Palabras reservadas
    'IF',
    'ELSE',
    'ELSEIF',
    'ENDIF',
    'FOR',
    'WHILE',
    'DO',
    'CLASS',
    'PUBLIC',
    'PRIVATE',
    'PROTECTED',
    'RETURN',
    'AND',
    'OR',
    'NOT',
    'PRINT',
    'VAR',
    'BREAK',
    'CASE',
    'INCLUDE',
    'GLOBAL',
    'ENDWHILE',
    'XOR',
    'ECHO',
    'INT',
    'FLOAT',
    'BOOL',
    'STRING',
    'TRUE',
    'FALSE',
    'NULL',
    'VOID',

    #Simbolos
    'LESS', # <
    'GREAT', # >
    'HASHTAG', 
    'SLASH', 
    'OQUESTION', # ¿
    'CQUESTION', # ?
    'PERCENTAGE',
    'EQUAL',
    'PLUS',

    'UNDERSCORE', #Guion bajo _
    'SCORE',      #Guion medio -
    'POINT',
    'COMMA',
    'SEMICOLON',
    'DQUOTATION', #Comillas dobles "
    'SQUOTATION', #Comillas simples '
    'OSBRACKET', #Llave apertura [
    'CSBRACKET', #Llave cierre ]
    'OSBRACKET', #Llave apertura {
    'CSBRACKET', #Llave cierre }
    'DOLLAR', #Simbolo de peso $
    'AMPERSAND', 
    'OPARENTHESIS', #Parentesis apertura (
    'CPARENTHESIS', #Parentesis apertura )
    'TIMES', #Signo de multiplicacion *




    #Otros
    'ID',
    'NUMBER',
    

}


def t_NUMBER(t):
    r'\d+(\.\d+)?'
    t.value = float(t.value)
    return t

def t_ID(t):
    r'\w+(_\d\w)*'
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)
    
def t_error(t):
    print ("Lexical error: " + str(t.value[0]))
    t.lexer.skip(1)
    
def test(data, lexer):
	lexer.input(data)
	while True:
		tok = lexer.token()
		if not tok:
			break
		print (tok)

lexer = lex.lex()

 
if __name__ == '__main__':
	if (len(sys.argv) > 1):
		fin = sys.argv[1]
	else:
		fin = 'calc.c'
	f = open(fin, 'r')
	data = f.read()
	print (data)
	lexer.input(data)
	test(data, lexer)
	input()