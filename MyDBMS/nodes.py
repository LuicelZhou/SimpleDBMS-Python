# -*- coding: utf-8 -*-
"""
@author: Luciel Waterhouse
"""
class NodeType:
    select = 'SELECT'
    insert = 'INSERT'
    delete = 'DELETE'
    update = 'UPDATE'
    create_database = 'CREATEDATABASE'
    create_table = 'CREATETABLE'
    use_database = 'USEDATABASE'
    drop_table = 'DROPTABLE'
    drop_database = 'DROPDATABASE'
    exit = 'EXIT'
    show_tables = 'SHOWTABLES'
    show_databases = 'SHOWDATABASES'
    value = 'VALUE'
    condition = 'CONDITION'
    relation_attr = 'RELATTR'
    attr_type = 'ATTRTYPE'
    into_type = 'INTOTYPE'
    start_type = 'START'

class StartNode:
    def __init__(self,command_node,start_node):
        self.type = NodeType.start_type
        self.start_node = start_node
        self.command_node = command_node

class QueryNode:
    def __init__(self,select_lists,from_lists,where_lists):
        self.type = NodeType.select
        self.select_lists = select_lists
        self.from_lists = from_lists
        self.where_lists = where_lists
class RelaAttr:
    def __init__(self,attr_name,table_name=None):
        self.type = NodeType.relation_attr
        self.attr_name = attr_name
        self.table_name = table_name

    def __str__(self):
        if self.table_name:
            return self.table_name + "." +self.attr_name
        else:
            return self.attr_name

class Cond:
    def __init__(self,L_cond,op,R_cond):
        self.type = NodeType.condition
        self.op = op.upper()
        self.L_cond = L_cond
        self.R_cond = R_cond

    def __str__(self):
        return "(" + str(self.L_cond) + "," + str(self.R_cond) + "," + self.op + ")"

class Value:
    def __init__(self,value_type,value):
        self.type = NodeType.value
        self.value_type = value_type
        self.value = value

    def __str__(self):
        #return str(self.value) + '[' +  self.value_type + ']'
        return  str(self.value)

class InsertNode:
    def __init__(self,into_lists,value_lists):
        self.type = NodeType.insert
        self.into_lists = into_lists
        self.value_lists = value_lists

class IntoNode:
    def __init__(self,table_name,colum_lists='all'):
        self.type = NodeType.into_type
        self.table_name = table_name
        self.colum_lists = colum_lists

class DeleteNode:
    def __init__(self,table_name,where_lists):
        self.type = NodeType.delete
        self.table_name = table_name
        self.where_lists = where_lists

class UpdateNode:
    def __init__(self,table_name,set_lists,where_lists):
        self.type = NodeType.update
        self.table_name = table_name
        self.set_lists = set_lists
        self.where_lists = where_lists

class AttrType:
    def __init__(self,attr_name,attr_type,type_len=-1):
        self.type = NodeType.attr_type
        self.attr_name = attr_name
        self.attr_type = attr_type
        self.type_len = type_len

    def __str__(self):
        if self.type_len == -1:
            return self.attr_name + " " +self.attr_type
        else:
            return self.attr_name + " " +self.attr_type + " " + str(self.type_len)

class CreateDatabaseNode:
    def __init__(self,database_name):
        self.type = NodeType.create_database
        self.database_name = database_name

class ShowDatabasesNode:
    def __init__(self):
        self.type = NodeType.show_databases

class CreateTableNode:
    def __init__(self, table_name, attr_list):
        self.type = NodeType.create_table
        self.table_name = table_name
        self.attr_list = attr_list

class ShowTablesNode:
    def __init__(self):
        self.type = NodeType.show_tables

class DropTableNode:
    def __init__(self,table_name):
        self.type = NodeType.drop_table
        self.table_name = table_name

class DropDatabaseNode:
    def __init__(self,database_name):
        self.type = NodeType.drop_database
        self.database_name = database_name

class UseDatabaseNode:
    def __init__(self,database_name):
        self.type = NodeType.use_database
        self.database_name = database_name

class ExitNode:
    def __init__(self):
        self.type = NodeType.exit
