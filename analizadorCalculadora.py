import ply.lex as lex
import sys

tokens = (
    #Palabras reservadas
    'SIN', 'COS', 'TAN', 'LOG', 
    #Simbolos
    'PLUS', 'MINUS', 'TIMES', 'DIVIDE', 'LPAREN', 'RPAREN', 'EQUAL', 'DOT',
    'POT',
    #Otros
    'ID', 'NUMBER',
)

# Regular expressions rules for a simple tokens 
t_PLUS   = r'\+'
t_MINUS  = r'-'
t_TIMES  = r'\*'
t_DIVIDE = r'/'
t_EQUAL  = r'='
t_LPAREN = r'\('
t_RPAREN  = r'\)'
t_DOT = r'\.'
t_POT = r'\e'

def t_SIN(t):
    r'sin'
    return t

def t_COS(t):
    r'cos'
    return t

def t_TAN(t):
    r'tan'
    return t

def t_LOG(t):
    r'log'
    return t

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