
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = "leftORleftANDnonassocLTLEGTGEEQNEAND CHAR CREATE DATABASE DATABASES DELETE DROP EQ EXIT FROM GE GT ID INSERT INT INTO LE LT NE NOT NULL NUMBER OR SELECT SET SHOW STRING TABLE TABLES UPDATE USE VALUES WHERE start : command ';' start\n             | empty  command : ddl\n                | dml\n                | utility\n                | empty  ddl : createdatabase\n            | createtable\n            | droptable\n            | dropdatabase\n            | showdatabases\n            | showtables\n            | usedatabase  dml : query\n            | update\n            | insert\n            | delete  utility : exit  exit : EXIT  empty :  createdatabase : CREATE DATABASE ID  showdatabases : SHOW DATABASES  usedatabase : USE ID  dropdatabase : DROP DATABASE ID  showtables : SHOW TABLES  droptable : DROP TABLE ID  createtable : CREATE TABLE ID '(' create_list ')'  query : SELECT select_list FROM from_list where_list  update : UPDATE ID SET set_list where_list  insert : INSERT INTO into_list VALUES insertvalue_list  delete : DELETE FROM ID where_list  insertvalue_list : '(' mvalue_list ')'  create_list : attrtype ',' create_list\n                    | attrtype  attrtype : ID type\n                 | ID type '(' NUMBER ')'  type : INT\n             | CHAR  select_list : relaattr_list\n                    | '*'  relaattr_list : relaattr ',' relaattr_list\n                      | relaattr  from_list : ID ',' from_list\n                  | ID  where_list : WHERE mcond_list\n                   | empty  mcond_list : mcond_list AND mcond_list\n                   | mcond_list OR mcond_list\n                   | '(' mcond_list ')'\n                   | condition  condition : relaattr op relaattr_or_value\n                  | relaattr EQ null_value\n                  | relaattr NE null_value  relaattr_or_value : relaattr\n                          | value  mvalue_list : value ',' mvalue_list\n                    | value\n                    | null_value ',' mvalue_list\n                    | null_value  value : STRING  value : NUMBER  null_value : NULL  op : LT\n           | LE\n           | GT\n           | GE\n           | EQ\n           | NE  set_list : relaattr EQ value ',' set_list\n                 | relaattr EQ value  into_list : ID '(' colum_list ')'\n                  | ID  colum_list : ID ',' colum_list\n                   | ID  relaattr : ID '.' ID\n                 | ID "
    
_lr_action_items = {'$end':([0,1,3,28,44,],[-20,0,-2,-20,-1,]),';':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,27,28,33,34,35,40,45,47,48,55,57,58,60,61,65,67,71,73,75,79,81,86,88,89,90,91,95,111,115,116,117,118,119,120,121,122,124,],[-20,28,-6,-3,-4,-5,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-22,-25,-23,-76,-21,-26,-24,-20,-20,-44,-75,-20,-31,-46,-28,-29,-30,-45,-50,-27,-43,-70,-60,-61,-62,-32,-47,-48,-49,-54,-51,-55,-52,-53,-69,]),'CREATE':([0,28,],[19,19,]),'DROP':([0,28,],[20,20,]),'SHOW':([0,28,],[21,21,]),'USE':([0,28,],[22,22,]),'SELECT':([0,28,],[23,23,]),'UPDATE':([0,28,],[24,24,]),'INSERT':([0,28,],[25,25,]),'DELETE':([0,28,],[26,26,]),'EXIT':([0,28,],[27,27,]),'DATABASE':([19,20,],[29,32,]),'TABLE':([19,20,],[30,31,]),'DATABASES':([21,],[33,]),'TABLES':([21,],[34,]),'ID':([22,23,24,29,30,31,32,42,43,49,50,51,52,56,64,66,72,80,87,96,98,99,101,102,103,104,105,106,107,110,],[35,40,41,45,46,47,48,54,55,58,40,60,40,68,77,40,58,40,68,77,40,40,40,-67,-68,-63,-64,-65,-66,40,]),'*':([23,],[38,]),'INTO':([25,],[42,]),'FROM':([26,36,37,38,39,40,59,60,],[43,49,-39,-40,-42,-76,-41,-75,]),',':([39,40,58,60,70,77,83,84,85,89,90,91,93,94,95,127,],[50,-76,72,-75,87,96,-35,-37,-38,110,-60,-61,112,113,-62,-36,]),'.':([40,],[51,]),'EQ':([40,60,62,82,],[-76,-75,74,102,]),'NE':([40,60,82,],[-76,-75,103,]),'LT':([40,60,82,],[-76,-75,104,]),'LE':([40,60,82,],[-76,-75,105,]),'GT':([40,60,82,],[-76,-75,106,]),'GE':([40,60,82,],[-76,-75,107,]),'AND':([40,60,79,81,90,91,95,100,115,116,117,118,119,120,121,122,],[-76,-75,98,-50,-60,-61,-62,98,-47,98,-49,-54,-51,-55,-52,-53,]),'OR':([40,60,79,81,90,91,95,100,115,116,117,118,119,120,121,122,],[-76,-75,99,-50,-60,-61,-62,99,-47,-48,-49,-54,-51,-55,-52,-53,]),')':([40,60,69,70,77,78,81,83,84,85,90,91,92,93,94,95,100,109,114,115,116,117,118,119,120,121,122,123,125,126,127,],[-76,-75,86,-34,-74,97,-50,-35,-37,-38,-60,-61,111,-57,-59,-62,117,-33,-73,-47,-48,-49,-54,-51,-55,-52,-53,127,-56,-58,-36,]),'SET':([41,],[52,]),'(':([46,54,63,66,80,83,84,85,98,99,],[56,64,76,80,80,108,-37,-38,80,80,]),'VALUES':([53,54,97,],[63,-72,-71,]),'WHERE':([55,57,58,61,88,89,90,91,124,],[66,66,-44,66,-43,-70,-60,-61,-69,]),'INT':([68,],[84,]),'CHAR':([68,],[85,]),'STRING':([74,76,101,102,103,104,105,106,107,112,113,],[90,90,90,-67,-68,-63,-64,-65,-66,90,90,]),'NUMBER':([74,76,101,102,103,104,105,106,107,108,112,113,],[91,91,91,-67,-68,-63,-64,-65,-66,123,91,91,]),'NULL':([76,102,103,112,113,],[95,95,95,95,95,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'start':([0,28,],[1,44,]),'command':([0,28,],[2,2,]),'empty':([0,28,55,57,61,],[3,3,67,67,67,]),'ddl':([0,28,],[4,4,]),'dml':([0,28,],[5,5,]),'utility':([0,28,],[6,6,]),'createdatabase':([0,28,],[7,7,]),'createtable':([0,28,],[8,8,]),'droptable':([0,28,],[9,9,]),'dropdatabase':([0,28,],[10,10,]),'showdatabases':([0,28,],[11,11,]),'showtables':([0,28,],[12,12,]),'usedatabase':([0,28,],[13,13,]),'query':([0,28,],[14,14,]),'update':([0,28,],[15,15,]),'insert':([0,28,],[16,16,]),'delete':([0,28,],[17,17,]),'exit':([0,28,],[18,18,]),'select_list':([23,],[36,]),'relaattr_list':([23,50,],[37,59,]),'relaattr':([23,50,52,66,80,98,99,101,110,],[39,39,62,82,82,82,82,118,62,]),'into_list':([42,],[53,]),'from_list':([49,72,],[57,88,]),'set_list':([52,110,],[61,124,]),'where_list':([55,57,61,],[65,71,73,]),'create_list':([56,87,],[69,109,]),'attrtype':([56,87,],[70,70,]),'insertvalue_list':([63,],[75,]),'colum_list':([64,96,],[78,114,]),'mcond_list':([66,80,98,99,],[79,100,115,116,]),'condition':([66,80,98,99,],[81,81,81,81,]),'type':([68,],[83,]),'value':([74,76,101,112,113,],[89,93,120,93,93,]),'mvalue_list':([76,112,113,],[92,125,126,]),'null_value':([76,102,103,112,113,],[94,121,122,94,94,]),'op':([82,],[101,]),'relaattr_or_value':([101,],[119,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> start","S'",1,None,None,None),
  ('start -> command ; start','start',3,'p_start','yaccer.py',39),
  ('start -> empty','start',1,'p_start','yaccer.py',40),
  ('command -> ddl','command',1,'p_command','yaccer.py',47),
  ('command -> dml','command',1,'p_command','yaccer.py',48),
  ('command -> utility','command',1,'p_command','yaccer.py',49),
  ('command -> empty','command',1,'p_command','yaccer.py',50),
  ('ddl -> createdatabase','ddl',1,'p_ddl','yaccer.py',54),
  ('ddl -> createtable','ddl',1,'p_ddl','yaccer.py',55),
  ('ddl -> droptable','ddl',1,'p_ddl','yaccer.py',56),
  ('ddl -> dropdatabase','ddl',1,'p_ddl','yaccer.py',57),
  ('ddl -> showdatabases','ddl',1,'p_ddl','yaccer.py',58),
  ('ddl -> showtables','ddl',1,'p_ddl','yaccer.py',59),
  ('ddl -> usedatabase','ddl',1,'p_ddl','yaccer.py',60),
  ('dml -> query','dml',1,'p_dml','yaccer.py',64),
  ('dml -> update','dml',1,'p_dml','yaccer.py',65),
  ('dml -> insert','dml',1,'p_dml','yaccer.py',66),
  ('dml -> delete','dml',1,'p_dml','yaccer.py',67),
  ('utility -> exit','utility',1,'p_utility','yaccer.py',71),
  ('exit -> EXIT','exit',1,'p_exit','yaccer.py',75),
  ('empty -> <empty>','empty',0,'p_empty','yaccer.py',79),
  ('createdatabase -> CREATE DATABASE ID','createdatabase',3,'p_createdatabase','yaccer.py',83),
  ('showdatabases -> SHOW DATABASES','showdatabases',2,'p_showdatabases','yaccer.py',87),
  ('usedatabase -> USE ID','usedatabase',2,'p_usedatabase','yaccer.py',91),
  ('dropdatabase -> DROP DATABASE ID','dropdatabase',3,'p_dropdatabase','yaccer.py',95),
  ('showtables -> SHOW TABLES','showtables',2,'p_showtables','yaccer.py',99),
  ('droptable -> DROP TABLE ID','droptable',3,'p_droptable','yaccer.py',103),
  ('createtable -> CREATE TABLE ID ( create_list )','createtable',6,'p_createtable','yaccer.py',107),
  ('query -> SELECT select_list FROM from_list where_list','query',5,'p_query','yaccer.py',111),
  ('update -> UPDATE ID SET set_list where_list','update',5,'p_update','yaccer.py',115),
  ('insert -> INSERT INTO into_list VALUES insertvalue_list','insert',5,'p_insert','yaccer.py',119),
  ('delete -> DELETE FROM ID where_list','delete',4,'p_delete','yaccer.py',123),
  ('insertvalue_list -> ( mvalue_list )','insertvalue_list',3,'p_insertvalue_list','yaccer.py',127),
  ('create_list -> attrtype , create_list','create_list',3,'p_create_list','yaccer.py',131),
  ('create_list -> attrtype','create_list',1,'p_create_list','yaccer.py',132),
  ('attrtype -> ID type','attrtype',2,'p_attrtype','yaccer.py',139),
  ('attrtype -> ID type ( NUMBER )','attrtype',5,'p_attrtype','yaccer.py',140),
  ('type -> INT','type',1,'p_type','yaccer.py',147),
  ('type -> CHAR','type',1,'p_type','yaccer.py',148),
  ('select_list -> relaattr_list','select_list',1,'p_select_list','yaccer.py',152),
  ('select_list -> *','select_list',1,'p_select_list','yaccer.py',153),
  ('relaattr_list -> relaattr , relaattr_list','relaattr_list',3,'p_relaattr_list','yaccer.py',157),
  ('relaattr_list -> relaattr','relaattr_list',1,'p_relaattr_list','yaccer.py',158),
  ('from_list -> ID , from_list','from_list',3,'p_from_list','yaccer.py',165),
  ('from_list -> ID','from_list',1,'p_from_list','yaccer.py',166),
  ('where_list -> WHERE mcond_list','where_list',2,'p_where_list','yaccer.py',173),
  ('where_list -> empty','where_list',1,'p_where_list','yaccer.py',174),
  ('mcond_list -> mcond_list AND mcond_list','mcond_list',3,'p_mcond_list','yaccer.py',181),
  ('mcond_list -> mcond_list OR mcond_list','mcond_list',3,'p_mcond_list','yaccer.py',182),
  ('mcond_list -> ( mcond_list )','mcond_list',3,'p_mcond_list','yaccer.py',183),
  ('mcond_list -> condition','mcond_list',1,'p_mcond_list','yaccer.py',184),
  ('condition -> relaattr op relaattr_or_value','condition',3,'p_condtion','yaccer.py',193),
  ('condition -> relaattr EQ null_value','condition',3,'p_condtion','yaccer.py',194),
  ('condition -> relaattr NE null_value','condition',3,'p_condtion','yaccer.py',195),
  ('relaattr_or_value -> relaattr','relaattr_or_value',1,'p_relaattr_or_value','yaccer.py',199),
  ('relaattr_or_value -> value','relaattr_or_value',1,'p_relaattr_or_value','yaccer.py',200),
  ('mvalue_list -> value , mvalue_list','mvalue_list',3,'p_mvalue_list','yaccer.py',204),
  ('mvalue_list -> value','mvalue_list',1,'p_mvalue_list','yaccer.py',205),
  ('mvalue_list -> null_value , mvalue_list','mvalue_list',3,'p_mvalue_list','yaccer.py',206),
  ('mvalue_list -> null_value','mvalue_list',1,'p_mvalue_list','yaccer.py',207),
  ('value -> STRING','value',1,'p_value_string','yaccer.py',214),
  ('value -> NUMBER','value',1,'p_value_number','yaccer.py',218),
  ('null_value -> NULL','null_value',1,'p_null_value','yaccer.py',222),
  ('op -> LT','op',1,'p_op','yaccer.py',226),
  ('op -> LE','op',1,'p_op','yaccer.py',227),
  ('op -> GT','op',1,'p_op','yaccer.py',228),
  ('op -> GE','op',1,'p_op','yaccer.py',229),
  ('op -> EQ','op',1,'p_op','yaccer.py',230),
  ('op -> NE','op',1,'p_op','yaccer.py',231),
  ('set_list -> relaattr EQ value , set_list','set_list',5,'p_set_list','yaccer.py',235),
  ('set_list -> relaattr EQ value','set_list',3,'p_set_list','yaccer.py',236),
  ('into_list -> ID ( colum_list )','into_list',4,'p_into_list','yaccer.py',243),
  ('into_list -> ID','into_list',1,'p_into_list','yaccer.py',244),
  ('colum_list -> ID , colum_list','colum_list',3,'p_colum_list','yaccer.py',251),
  ('colum_list -> ID','colum_list',1,'p_colum_list','yaccer.py',252),
  ('relaattr -> ID . ID','relaattr',3,'p_relaattr','yaccer.py',259),
  ('relaattr -> ID','relaattr',1,'p_relaattr','yaccer.py',260),
]
