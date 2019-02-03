import ply.lex as lex
import sys

tokens = (
    #Palabras reservadas y estructuras de control
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
    'NAMEFUNCTION',
    #OPEN Y CLOSE TAG
    'PHPDECLARATION',
    'PHPCLOSING',
    'CHR',
    'VARIABLE', #$VAR
    'COMMENTONELINE',
    'COMMENTMULTIPLELINE',
    'GOTO',
    'FOREACH',
    'CONTINUE',
    'DECLARE',
    'REQUIRE',
    'INCLUDE_ONCE',
    'REQUIRE_ONCE',
    'NEW',
    'EXTENDS',
    'FINAL',
    'IMPLEMENTS',
    'INTERFACE',
    'ABSTRACT',
    'TRAIT',
    'CONSTRUCTOR',
    'DESTRUCTOR',
    'STATIC',
    'CLONE',
    'STRINGWR',
    'STRINGGWR'


    #Simbolos
    'LESS',
    'LESSE',
    'GREAT', 
    'GREATE', 
    'HASHTAG', 
    'SLASH', 
    #'OQUESTION', 
    'CQUESTION', 
    'PERCENTAGE',
    'DEQUAL',
    'EQUAL',
    'EQUALE',
    'IDENTIC',
    'PLUS',
    'POW',

    'UNDERSCORE', #Guion bajo _
    'SCORE',      #Guion medio -
    'POINT', #.
    'COMMA',# ,
    'SEMICOLON',
    'DQUOTATION', #Comillas dobles "
    'SQUOTATION', #Comillas simples '
    'OSBRACKET', #Llave apertura [   OPENING SQUARE
    'CSBRACKET', #Llave cierre ]
    'OCBRACKET', #Llave apertura { OPENING CURLY 
    'CCBRACKET', #Llave cierre }
    'AMPERSAND', #&
    'OPARENTHESIS', #Parentesis apertura (
    'CPARENTHESIS', #Parentesis apertura )
    'TIMES', #Signo de multiplicacion *
    'BOOLAND', # && 
    'BOOLOR', # ||
    'COMMENTO', # //
    'COMMENTMO',  # /*
    'COMMENTMC',  # */
    'DOUBLEPOINTS',# :
    'SPACE',
    'ARRAY_ASSIGNATION', #=>
    'PLUSPLUS', #++
    'MINUSMINUS', #--
    #Otros
    'ID',
    'NUMBER',
)

t_LESS=r'<'
#t_LESSE=r'<='  
t_GREAT=r'>'
#t_GREATE=r'>='
t_HASHTAG=r'\#'
t_SLASH=r'/'
t_CQUESTION=r'\?'
t_PERCENTAGE=r'%'
t_EQUAL=r'='
#t_DEQUAL=r'!='
#t_EQUALE=r'=='
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
t_AMPERSAND=r'&'
t_OPARENTHESIS=r'\('
t_CPARENTHESIS=r'\)'
t_TIMES=r'\*'
t_BOOLAND=r'&&'
t_BOOLOR=r'\|\|'
t_DOUBLEPOINTS=r':'
t_ARRAY_ASSIGNATION=r'=>'
t_PLUSPLUS=r'\+\+'
t_MINUSMINUS=r'--'
t_POW=r'\*\*'
#t_SPACE=r'\ '

#Se omite el espacio el retorno del espacio en el codigo
def t_SPACE(t):
    r'\ '
    #return t
    

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
    r'or|\|\||OR'
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
    r'TRUE|True|true'
    return t   

def t_FALSE(t):
    r'FALSE|False|false'
    return t   

def t_NULL(t):
    r'NULL|Null|null'
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
    r'<\?php|<\?PHP'
    return t

def t_PHPCLOSING(t):
    r'\?>'
    return t

def t_CHR(t):
    r'chr'
    return t

def t_GOTO(t):
    r'goto'
    return t

def t_FOREACH(t):
    r'foreach'
    return t

def t_DECLARE(t):
    r'declare'
    return t

def t_REQUIRE(t):
    r'require'
    return t

def t_REQUIRE_ONCE(t):
    r'require_once'
    return t

def t_INCLUDE_ONCE(t):
    r'include_once'
    return t

def t_NEW(t):
    r'new'
    return t

def t_CLONE(t):
    r'clone'
    return t    

def t_EXTENDS(t):
    r'extends'
    return t

def t_IMPLEMENTS(t):
    r'implements'
    return t

def t_INTERFACE(t):
    r'interface'
    return t

def t_FINAL(t):
    r'final'
    return t

def t_ABSTRACT(t):
    r'abstract'
    return t

def t_TRAIT(t):
    r'trait'
    return t

def t_CONSTRUCTOR(t):
    r'__construct'
    return t

def t_DESTRUCTOR(t):
    r'__destruct'
    return t

def t_STATIC(t):
    r'static'
    return t

def t_LESSE(t):
    r'<='
    return t

def t_GREATE(t):
    r'>='
    return t

def t_DEQUAL(t):
    r'!='
    return t

def t_EQUALE(t):
    r'=='
    return t   

def t_IDENTIC(t):
    r'==='
    return t   

#Definicion de una variable: $NombreVar
def t_VARIABLE(t):
    r'\$[A-Za-z_][\w_\d]*'
    return t

#Definicion de cadena 
def t_STRINGWR(t):
    r'\'[a-zA-Z_0-9\&\.\-\_\+\*\$\%\@\!\xc2\xa1\/\\\#\?\xc2\xbf\(\)\|\=\{\}\[\]\>\<\,\: \t]*\''
    t.value = str(t.value)
    return t

def t_STRINGGWR(t):
    r'\'[a-zA-Z_0-9\&\.\-\_\+\*\$\%\@\!\xc2\xa1\/\\\#\?\xc2\xbf\(\)\|\=\{\}\[\]\>\<\,\: \t]*\''
    t.value = str(t.value)
    return t

#Definicion de comentario de una linea
'''el simbolo . significa cualquier caracter'''
def t_COMMENTONELINE(t):
    r'//.*'
    pass
  

#Definicion de comentario de una linea
#el simbolo / es un delimitador es como para saber hasta donde llega la expresion regular
#Se usa el simbolo . para generar cualquier tipo de simbolo

def t_COMMENTMULTIPLELINE(t):
    r'/\*(.|\n)*?\*/'
    pass

#Definicion de numero, ya sea entero o flotante y de tipo negativo
def t_NUMBER(t):
    r'-?\d+(\.\d+)?'
    t.value = float(t.value)
    return t
#Definciion para ID que se podrá usar en la declaración de funciones
def t_ID(t):
    r'\w+(_\d\w)*'
    return t
#Retorna el nombre de un funcion, incluye numeros y letras
def t_NAMEFUNCTION(t):
    r'[a-zA-Z][a-zA-Z_\-0-9]*'
    return t    
#Retorna el salto de linea
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

 #Funcion principal del sistema
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