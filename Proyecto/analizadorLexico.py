import ply.lex as lex
import sys

tokens = (
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
    'AS',
    'SWITCH',
    'ENDSWITCH',
    'FUNCTION',
    'PHPDECLARATION',
    'CHR',
    'VARIABLE', # $VAR
    'COMMENTONELINE',
    'COMMENTMULTIPLELINE',

    #Simbolos
    'LESS', # <
    'LESSE', # <=  #SI VA
    'GREAT', # >
    'GREATE', # >=  #SI VA
    'HASHTAG', 
    'SLASH', 
    #'OQUESTION', 
    'CQUESTION', 
    'PERCENTAGE',
    'EQUAL',
    'EQUALE', # ==  #SI VA
    'PLUS',

    'UNDERSCORE', #Guion bajo _
    'SCORE',      #Guion medio -
    'POINT',
    'COMMA',
    'SEMICOLON',
    'DQUOTATION', #Comillas dobles "
    'SQUOTATION', #Comillas simples '
    'OSBRACKET', #Llave apertura [   OPENING SQUARE
    'CSBRACKET', #Llave cierre ]
    'OCBRACKET', #Llave apertura { OPENING CURLY 
    'CCBRACKET', #Llave cierre }
    'DOLLAR', #Simbolo de peso $
    'AMPERSAND', 
    'OPARENTHESIS', #Parentesis apertura (
    'CPARENTHESIS', #Parentesis apertura )
    'TIMES', #Signo de multiplicacion *
    'BOOLAND', # &&  SI VA
    'BOOLOR', # || SI VA
    'COMMENTO', # // SI VA
    'COMMENTMO',  #/* SI VA
    'COMMENTMC',  #*/   SI VA
    'DOUBLEPOINTS',
    'SPACE',

    #Otros
    'ID',
    'NUMBER',
)

t_LESS=r'<'
t_LESSE=r'<='  
t_GREAT=r'>'
t_GREATE=r'>='
t_HASHTAG=r'\#'
t_SLASH=r'/'
t_CQUESTION=r'\?'
t_PERCENTAGE=r'%'
t_EQUAL=r'='
t_EQUALE=r'==' #NO SE SI VAYA
t_PLUS=r'\+'
t_UNDERSCORE=r'_'
t_SCORE=r'-'
t_POINT=r'\.'
t_COMMA=r','
t_SEMICOLON=r';'
t_DQUOTATION=r'"'
t_SQUOTATION=r'\''
t_OSBRACKET=r'\['
t_CSBRACKET=r'\]'
t_OCBRACKET=r'\{'
t_CCBRACKET=r'\}'
t_DOLLAR=r'\$'
t_AMPERSAND=r'&'
t_OPARENTHESIS=r'\('
t_CPARENTHESIS=r'\)'
t_TIMES=r'\*'
t_BOOLAND=r'&&'
t_BOOLOR=r'\|\|'
t_DOUBLEPOINTS=r':'
t_SPACE=r'\ '

#----------------------------------------------------------------------------------
def t_IF(t):
    r'if'
    return t

def t_ELSE(t):
    r'else'
    return t

def t_ELSEIF(t):
    r'elseif'
    return t    

def t_ENDIF(t):
    r'endif'
    return t

def t_FOR(t):
    r'for'
    return t

def t_WHILE(t):
    r'while'
    return t

def t_DO(t):
    r'do'
    return t

def t_CLASS(t):
    r'class'
    return t

def t_PUBLIC(t):
    r'public'
    return t

def t_PRIVATE(t):
    r'private'
    return t

def t_PROTECTED(t):
    r'protected'
    return t   

def t_RETURN(t):
    r'return'
    return t

def t_AND(t):
    r'and'
    return t   

def t_OR(t):
    r'or'
    return t   
 
def t_NOT(t):
    r'not'
    return t   

def t_PRINT(t):
    r'print'
    return t

def t_VAR(t):
    r'var'
    return t

def t_BREAK(t):
    r'break'
    return t

def t_CASE(t):
    r'case'
    return t   

def t_INCLUDE(t):
    r'include'
    return t 

def t_GLOBAL(t):
    r'global'
    return t   

def t_ENDWHILE(t):
    r'endwhile'
    return t  

def t_XOR(t):
    r'xor'
    return t   

def t_ECHO(t):
    r'echo'
    return t

def t_INT(t):
    r'int'
    return t   

def t_FLOAT(t):
    r'float'
    return t

def t_BOOL(t):
    r'bool'
    return t   

def t_STRING(t):
    r'string'
    return t   

def t_TRUE(t):
    r'true'
    return t   

def t_FALSE(t):
    r'false'
    return t   

def t_NULL(t):
    r'null'
    return t 

def t_VOID(t):
    r'void'
    return t   

def t_AS(t):
    r'as'
    return t

def t_SWITCH(t):
    r'switch'
    return t

def t_ENDSWITCH(t):
    r'endswitch'
    return t

def t_FUNCTION(t):
    r'function'
    return t

def t_PHPDECLARATION(t):
    r'<\?php'
    return t

def t_CHR(t):
    r'chr'
    return t
  
#Definicion de una variable: $NombreVar
def t_VARIABLE(t):
    r'\$w+(_\d\w)*'
    return t

#Definicion de comentario de una linea
def t_COMMENTONELINE(t):
    r'\//(d\w\ \.\-\_\+\*\#\?)*\n'  #FALTA AGREGAR SIMBOLOS
    return t

#Definicion de comentario de una linea
def t_COMMENTMULTIPLELINE(t):
    r'\*(d\w\ \.\-\_\+\*\#\?)*/*'  #FALTA AGREGAR SIMBOLOS
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
		fin = 'pruebaPHP.php'
	f = open(fin, 'r')
	data = f.read()
	print (data)
	lexer.input(data)
	test(data, lexer)
	input()