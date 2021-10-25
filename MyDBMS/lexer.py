# -*- coding: utf-8 -*-
"""
@author: Luciel Waterhouse
"""
import ply.lex as lex

#token names
reversed = (
    #Main
    'CREATE','TABLE','DROP','SHOW','SELECT','FROM','WHERE',
    'INSERT','DELETE','UPDATE','SET','INTO','VALUES','TABLES',
    'DATABASE','DATABASES','USE',
    'NULL',
    #Command
    'EXIT',
    #Operator
    'AND','OR','NOT',
    #Type
    'INT','CHAR'
)

tokens = reversed + (
    #Symbol
    'ID','NUMBER','STRING',
    #Operator
    'EQ','LT','LE','GT','GE','NE'
)

#Regular rules
t_EQ = r'='
t_LT = r'<'
t_LE = r'<='
t_GT = r'>'
t_GE = r'>='
t_NE = r'!='

literals = ['(',')',',',';','.','+','-','*','/']

#Ignore spaces and tabs
t_ignore = r' '
#Ignore notes
t_ignore_notes_mul = r'\/\*.*?\*\/'
t_ignore_notes_sigle = r'\/\/.*?$'

#ID or Main Identifier
def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    if t.value.upper() not in reversed:
        t.type = 'ID'
    else:
        t.type = t.value.upper()
    return t

#NUMBER
def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

#get the string between "" or ''
def t_STRING(t):
    r'(\'|").*?(\'|")'
    t.value = t.value[1:-1]
    return t

#\n
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

#error infomation
def t_error(t):
    print("LEX ERROR [%s,%s]:Illegal word '%s'."%(t.lexer.lineno,t.lexer.lexpos,t.value[0]))

lexer = lex.lex()
