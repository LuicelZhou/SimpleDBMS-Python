# -*- coding: utf-8 -*-
"""
Created on Mon Apr 30 22:44:29 2019

@author: Luciel Waterhouse
"""
"""
SQL includes DML and DDL
DML:
    SELECT
    UPDATE
    INSERT INTO
    DELETE
DDL:
    CREATE DATABASE
    CREATE TABLE
    DROP TABLE
    SHOW DATABASES
    SHOW TABLES
    USE DATABASE
UTILITY:
    EXIT
"""

import ply.yacc as yacc
import lexer
import nodes

tokens = lexer.tokens

precedence = (
    ('left','OR'),
    ('left','AND'),
    ('nonassoc','LT','LE','GT','GE','EQ','NE')
)

#All commands in DBMS ends with ';'
def p_start(p):
    """ start : command ';' start
             | empty """
    if p[1] == None:
        p[0] = p[1]
    else:
        p[0] = nodes.StartNode(p[1], p[3])

def p_command(p):
    """ command : ddl
                | dml
                | utility
                | empty """
    p[0] = p[1]

def p_ddl(p):
    """ ddl : createdatabase
            | createtable
            | droptable
            | dropdatabase
            | showdatabases
            | showtables
            | usedatabase """
    p[0] = p[1]

def p_dml(p):
    """ dml : query
            | update
            | insert
            | delete """
    p[0] = p[1]

def p_utility(p):
    """ utility : exit """
    p[0] = p[1]

def p_exit(p):
    """ exit : EXIT """
    p[0] = nodes.ExitNode()

def p_empty(p):
    """ empty : """
    p[0] = None

def p_createdatabase(p):
    """ createdatabase : CREATE DATABASE ID """
    p[0] = nodes.CreateDatabaseNode(p[3])

def p_showdatabases(p):
    """ showdatabases : SHOW DATABASES """
    p[0] = nodes.ShowDatabasesNode()

def p_usedatabase(p):
    """ usedatabase : USE ID """
    p[0] = nodes.UseDatabaseNode(p[2])

def p_dropdatabase(p):
    """ dropdatabase : DROP DATABASE ID """
    p[0] = nodes.DropDatabaseNode(p[3])

def p_showtables(p):
    """ showtables : SHOW TABLES """
    p[0] = nodes.ShowTablesNode()

def p_droptable(p):
    """ droptable : DROP TABLE ID """
    p[0] = nodes.DropTableNode(p[3])

def p_createtable(p):
    """ createtable : CREATE TABLE ID '(' create_list ')' """
    p[0] = nodes.CreateTableNode(p[3],p[5])

def p_query(p):
    """ query : SELECT select_list FROM from_list where_list """
    p[0] = nodes.QueryNode(p[2],p[4],p[5])

def p_update(p):
    """ update : UPDATE ID SET set_list where_list """
    p[0] = nodes.UpdateNode(p[2],p[4],p[5])

def p_insert(p):
    """ insert : INSERT INTO into_list VALUES insertvalue_list """
    p[0] = nodes.InsertNode(p[3],p[5])

def p_delete(p):
    """ delete : DELETE FROM ID where_list """
    p[0] = nodes.DeleteNode(p[3],p[4])

def p_insertvalue_list(p):
    """ insertvalue_list : '(' mvalue_list ')' """
    p[0] = p[2]

def p_create_list(p):
    """ create_list : attrtype ',' create_list
                    | attrtype """
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = [p[1]] + p[3]

def p_attrtype(p):
    """ attrtype : ID type
                 | ID type '(' NUMBER ')' """
    if len(p) == 3:
        p[0] = nodes.AttrType(p[1],p[2])
    else:
        p[0] = nodes.AttrType(p[1],p[2],p[4])

def p_type(p):
    """ type : INT
             | CHAR """
    p[0] = p[1].upper()

def p_select_list(p):
    """ select_list : relaattr_list
                    | '*' """
    p[0] = p[1]

def p_relaattr_list(p):
    """ relaattr_list : relaattr ',' relaattr_list
                      | relaattr """
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = [p[1]] + p[3]

def p_from_list(p):
    """ from_list : ID ',' from_list
                  | ID """
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = [p[1]] + p[3]

def p_where_list(p):
    """ where_list : WHERE mcond_list
                   | empty """
    if len(p) == 3:
        p[0] = p[2]
    else:
        p[0] = p[1]

def p_mcond_list(p):
    """ mcond_list : mcond_list AND mcond_list
                   | mcond_list OR mcond_list
                   | '(' mcond_list ')'
                   | condition """
    if len(p) == 2:
        p[0] = p[1]
    elif p[1] == '(':
        p[0] = p[2]
    else:
        p[0] = nodes.Cond(p[1],p[2],p[3])

def p_condtion(p):
    """ condition : relaattr op relaattr_or_value
                  | relaattr EQ null_value
                  | relaattr NE null_value """
    p[0] = nodes.Cond(p[1],p[2],p[3])

def p_relaattr_or_value(p):
    """ relaattr_or_value : relaattr
                          | value """
    p[0] = p[1]

def p_mvalue_list(p):
    """ mvalue_list : value ',' mvalue_list
                    | value
                    | null_value ',' mvalue_list
                    | null_value """
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = [p[1]] + p[3]

def p_value_string(p):
    """ value : STRING """
    p[0] = nodes.Value('STRING',p[1])

def p_value_number(p):
    """ value : NUMBER """
    p[0] = nodes.Value('NUMBER',p[1])

def p_null_value(p):
    """ null_value : NULL """
    p[0] = nodes.Value('NULL',None)

def p_op(p):
    """ op : LT
           | LE
           | GT
           | GE
           | EQ
           | NE """
    p[0] = p[1]

def p_set_list(p):
    """ set_list : relaattr EQ value ',' set_list
                 | relaattr EQ value """
    if len(p) > 4:
        p[0] = [(p[1],p[3])] + p[5]
    else:
        p[0] = [(p[1],p[3])]

def p_into_list(p):
    """ into_list : ID '(' colum_list ')'
                  | ID """
    if len(p) > 2:
        p[0] = nodes.IntoNode(p[1],p[3])
    else:
        p[0] = nodes.IntoNode(p[1])

def p_colum_list(p):
    """ colum_list : ID ',' colum_list
                   | ID """
    if len(p) > 2:
        p[0] = [p[1]] + p[3]
    else:
        p[0] = [p[1]]

def p_relaattr(p):
    """ relaattr : ID '.' ID
                 | ID """
    if len(p) == 2:
        p[0] = nodes.RelaAttr(p[1])
    else:
        p[0] = nodes.RelaAttr(p[3],p[1])

#Error Notes
def p_error(p):
    if not p:
        print("Syntax Error! Maybe Missing ';' at the end of the command!")
    else:
        print("Syntax Error at token '%s'(%s)"%(p.value,p.type))

from lexer import lexer as lex
yaccer = yacc.yacc()
