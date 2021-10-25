# -*- coding: utf-8 -*-
"""
@author: Luciel Waterhosue
"""
import nodes
import os
import itertools

#supported function
def make_dict(colum_list,line):
    line_list = line.split()
    dict = {}
    i = 0
    for c in colum_list:
        if line_list[i] == "NULL":
            dict[c[0]] = None
            i = i+1
            continue
        if c[1] == "INT":
            dict[c[0]] = int(line_list[i])
            i = i+1
        elif c[1] == "CHAR":
            dict[c[0]] = str(line_list[i])
            i = i+1
        else:
            raise RuntimeError("Error!! line_list type error!")
    return dict

def __get_value(line_dict,Node):
    if Node.type == nodes.NodeType.relation_attr:
        if Node.table_name == None:
            return line_dict[Node.attr_name]
        else:
            return line_dict[Node.table_name+"."+Node.attr_name]
    else:
        if Node.value_type == "STRING":
            return str(Node.value)
        elif Node.value_type == "NUMBER":
            return int(Node.value)
        elif Node.value_type == "NULL":
            return None
        else:
            raise RuntimeError("Error!! Value type error!")
def judge_where(line_dict,Node):
    assert (Node.type == nodes.NodeType.condition)
    where_list = Node
    L_cond = where_list.L_cond
    R_cond = where_list.R_cond
    op = where_list.op
    if op == "AND":
        return judge_where(line_dict,L_cond) and judge_where(line_dict,R_cond)
    elif op == "OR":
        return  judge_where(line_dict,L_cond) or judge_where(line_dict,R_cond)
    elif op == ">=":
        return  __get_value(line_dict,L_cond) >= __get_value(line_dict,R_cond)
    elif op == "<=":
        return __get_value(line_dict, L_cond) <= __get_value(line_dict, R_cond)
    elif op == ">":
        return __get_value(line_dict, L_cond) > __get_value(line_dict, R_cond)
    elif op == "<":
        return __get_value(line_dict, L_cond) < __get_value(line_dict, R_cond)
    elif op == "=":
        return __get_value(line_dict, L_cond) == __get_value(line_dict, R_cond)
    elif op == "!=":
        return __get_value(line_dict, L_cond) != __get_value(line_dict, R_cond)
    else:
        raise RuntimeError("Error!! op type error!!")

def tables_joint(tables):
    all_tb_list = []
    for tb in tables:
        with open(current_database_path+tb.upper()+".txt","r") as f:
            tb_list = []
            for line in f:
                tb_list = tb_list + [line.split()]
        all_tb_list = all_tb_list + [tb_list] #[ [ [t1.r1] [t1.r2] ]  [  []  [] ]  [  []  [] ] ]
    p = all_tb_list[0]
    all_tb_list = all_tb_list[1:]
    for abl in all_tb_list:
        p = list(itertools.product(p,abl))
        if isinstance(p[0][0],tuple):
            for i in range(len(p)):
                p[i] = tuple(list(p[i][0]) + p[i][1])

    with open(current_database_path+"tables_joint.txt",'w') as f:
        #[  ([]  []  [])   ()   ()  ]
        for p_item in p:
            for t_item in p_item:
                for li in t_item:
                    f.write(li+" ")
            f.write("\n")
###############################
src_path = "D:/Waterhouse/编译原理/DB/"
current_database_path = "D:/Waterhouse/编译原理/DB/"

def exe_start(Node):
    if Node.command_node == None:
        pass
    elif Node.command_node.type != nodes.NodeType.start_type:
        Execute(Node.command_node)
    else:
        exe_start(Node.command_node)
    if Node.start_node == None:
        pass
    elif Node.start_node != nodes.NodeType.start_type:
        Execute(Node.start_node)
    else:
        exe_start(Node.start_node)
def exe_create_database(Node):
    db_name = Node.database_name
    try:
        os.mkdir(src_path+db_name)
    except FileExistsError:
        print("Error:Database "+Node.database_name+" has existed")
    else:
        f = open(src_path+"sys.dat",mode='a+')
        ff = open(src_path+Node.database_name+"/sys.dat",mode='w')
        ff.close()
        f.write(Node.database_name+"\n")
        f.close()

def exe_show_databases(Node):
    current_database_name = os.listdir(src_path)
    if len(current_database_name) == 1:
        print("There are no databases now!")
    else:
        current_database_name.remove("sys.dat")
        print(current_database_name)

def exe_drop_database(Node):
    try:
        find = False
        f = open(src_path+"sys.dat",mode='r')
        f_new = open(src_path+"sys.dat.t",mode='w')
        for line in f:
            if Node.database_name in line:
                find = True
                os.remove(src_path+Node.database_name+"sys.dat")
                os.rmdir(src_path + Node.database_name)
            else:
                f_new.write(line)
        f.close()
        f_new.close()
        os.remove(src_path+"sys.dat")
        os.rename(src_path+"sys.dat.t",src_path+"sys.dat")
        if not find:
            print("Error:Database "+Node.database_name+" doesn't exist")
    except OSError:
        print("Error: Cannot drop the database:"+Node.database_name+"\n")

def exe_use_database(Node):
    if Node.database_name in os.listdir(src_path):
        global current_database_path
        current_database_path = src_path + Node.database_name +"/"
    else:
        print("Error: Database "+Node.database_name+" not exists")
    print(Node.database_name+"--"+current_database_path)

def exe_create_table(Node):
    tb_name = Node.table_name
    tb_attr_list = Node.attr_list
    if os.path.exists(current_database_path+tb_name+".txt"):
        raise RuntimeError("Error: Table "+tb_name+" exists!")
    f = open(current_database_path+"sys.dat",mode='a+')
    i = 1
    for attr in tb_attr_list:
        f.write(tb_name + " " +str(i)+" "+attr.__str__()+"\n")
        i += 1
    f.close()
    f = open(current_database_path+tb_name+".txt",mode='w')

def exe_show_tables(Node):
    current_table_file = os.listdir(current_database_path)
    current_table_name = []
    if len(current_table_file) == 1:
        print("There are no tables now!")
    else:
        for tne in current_table_file:
            if tne != "sys.dat":
                current_table_name.append(tne[:-4])
        print(current_table_name)

def exe_drop_table(Node):
    #print(current_database_path)
    if Node.table_name+".txt" in os.listdir(current_database_path):
        os.remove(current_database_path + Node.table_name+".txt")
        with open(current_database_path+"sys.dat",'r') as f:
            f_new = open(current_database_path+"sys.dat.t",'w')
            for line in f:
                if line.split()[0] != Node.table_name:
                    f_new.write(line)
                else:
                    continue
            f_new.close()
        os.remove(current_database_path+"sys.dat")
        os.rename(current_database_path+"sys.dat.t",current_database_path+"sys.dat")
    else:
        print("Error: "+Node.table_name+" doesn't exist!")

def exe_select(Node):
    select_lists = Node.select_lists
    from_lists = Node.from_lists
    where_lists = Node.where_lists
    colum_lists = []

    #################################################################
    # select from a single table
    if len(from_lists) == 1:
        table_name = from_lists[0]
        with open(current_database_path+"sys.dat",'r') as f:
            for line in f:
                if table_name == line.split()[0]:
                    colum_lists =colum_lists + [[line.split()[2]]+[line.split()[3]]] ##[[sname char][sage int]]

        if isinstance(select_lists[0],str): #Condition * （select all lines）
            assert (select_lists[0] == "*")
            ##print the table head
            for cc in colum_lists:
                print(cc[0] + "          ", end='')
            print('')
            ##
            if not where_lists == None: # where_lists exist:
                with open(current_database_path + table_name + ".txt", 'r') as f:
                    for line in f:
                        line_dict = make_dict(colum_lists, line)
                        if judge_where(line_dict, where_lists):
                            for i in line.split():
                                print(i + "        ", end='')
                            print('')
            else:
                with open(current_database_path+table_name+".txt",'r') as f:
                    for line in f:
                        line_split = line.split()
                        for s in line_split:
                            print(s+"        ",end='')
                        print('')
        else: #Normal Condition
            assert (select_lists[i].type == nodes.NodeType.relation_attr for i in select_lists)
            show_colum_num = []
            for rr in select_lists:
                ##print the table head
                print(rr.attr_name+"          ",end='')
                ##
                for c in colum_lists:
                    if rr.attr_name == c[0]:
                        show_colum_num = show_colum_num + [colum_lists.index(c)]
                        break
            print('')
            if not where_lists == None:
                with open(current_database_path + table_name + ".txt",'r') as f:
                    for line in f:
                        line_dict = make_dict(colum_lists,line)
                        if judge_where(line_dict,where_lists):
                            for num in show_colum_num:
                                print(line.split()[num]+"        ",end='')
                            print('')
            else:
                with open(current_database_path + table_name + ".txt",'r') as f:
                    for line in f:
                        line_dict = make_dict(colum_lists,line)
                        for num in show_colum_num:
                            print(line.split()[num]+"        ",end='')
                        print('')
    #
    ##################################################################

    ##################################################################
    #select from tables
    else:
        #### joint the tables
        table_name = from_lists
        with open(current_database_path+"sys.dat",'r') as f:
            for tb in table_name:
                tb = tb.upper()
                f.seek(0)
                for line in f:
                    if tb == line.split()[0]:
                        temp_str = line.split()[2]
                        colum_lists = colum_lists + [[temp_str] + [line.split()[3]] + [tb]]  ##[[sname char tb][tb.sage int tb]]
                    else:
                        continue
        for it in colum_lists:
            for it_t in colum_lists:
                if (it[0] == it_t[0] or (len(it_t[0].split(".")) == 2 and it[0] == it_t[0].split(".")[1])) and it[2] != it_t[2]:
                    it[0] = it[2]+"."+it[0]
                    it_t[0] = it_t[2]+"."+it_t[0]
        tables_joint(table_name)
        if isinstance(select_lists[0],str): #Condition * （select all lines）
            assert (select_lists[0] == "*")
            ##print the table head
            for cc in colum_lists:
                print(cc[0] + "      ", end='')
            print('')
            if not where_lists == None:
                with open(current_database_path +"tables_joint.txt",'r') as f:
                    for line in f:
                        line_dict = make_dict(colum_lists,line)
                        if judge_where(line_dict,where_lists):
                            for s in line.split():
                               print(s + "        ", end='')
                            print('')
            else:
                with open(current_database_path +"tables_joint.txt",'r') as f:
                    for line in f:
                        for s in line.split():
                           print(s + "        ", end='')
                        print('')
        else:
            # Normal Condition
            assert (select_lists[i].type == nodes.NodeType.relation_attr for i in select_lists)
            show_colum_num = []
            for rr in select_lists:
                ##print the table head
                if rr.table_name == None:
                    print(rr.attr_name + "          ", end='')
                    for c in colum_lists:
                        if rr.attr_name == c[0]:
                            show_colum_num = show_colum_num + [colum_lists.index(c)]
                            break
                else:
                    print(rr.table_name+"."+rr.attr_name + "          ", end='')
                    for c in colum_lists:
                        if (rr.table_name+"."+rr.attr_name) == c[0]:
                            show_colum_num = show_colum_num + [colum_lists.index(c)]
                            break
                ##
            print('')
            if not where_lists == None:
                with open(current_database_path+"tables_joint.txt",'r') as f:
                    for line in f:
                        line_dict = make_dict(colum_lists,line)
                        if judge_where(line_dict,where_lists):
                            for num in show_colum_num:
                                print(line.split()[num]+"        ",end='')
                            print('')
            else:
                with open(current_database_path+"tables_joint.txt",'r') as f:
                    for line in f:
                        for num in show_colum_num:
                            print(line.split()[num]+"        ",end='')
                        print('')
            ##os.remove(current_database_path+"tables_joint.txt")
    #
    ##################################################################

def exe_insert(Node):
    tb_name = Node.into_lists.table_name
    colum_lists = Node.into_lists.colum_lists
    value_lists = Node.value_lists
    max_colum_num = -1
    with open(current_database_path+"sys.dat",'r') as f:
        for line in f:
            if tb_name == line.split()[0]:
                max_colum_num = int(line.split()[1])
        if max_colum_num == -1:
            raise RuntimeError("Table "+tb_name+" doesn't exist")
    with open(current_database_path+tb_name+".txt",'a') as f:
        if colum_lists == 'all':
            for li in value_lists:
                f.write(li.__str__()+" ")
            f.write("\n")
        else:
            for li in value_lists:
                f.write(li.__str__()+" ")
            max_colum_num -= len(value_lists)
            for i in range(max_colum_num):
                f.write("NULL ")
            f.write("\n")

def exe_delete(Node):
    table_name = Node.table_name
    where_lists = Node.where_lists
    colum_lists = []
    with open(current_database_path+"sys.dat",'r') as f:
        for line in f:
            if table_name == line.split()[0]:
                colum_lists =colum_lists + [[line.split()[2]]+[line.split()[3]]] ##[[sname char][sage int]]
    with open(current_database_path+table_name+".txt",'r') as f:
        with open(current_database_path+table_name+".txt.t",'w') as f_new:
            for line in f:
                line_dic = make_dict(colum_lists,line)
                if not judge_where(line_dic,where_lists):
                    f_new.write(line)
                else:  continue
    os.remove(current_database_path+table_name+".txt")
    os.rename(current_database_path+table_name+".txt.t",current_database_path+table_name+".txt")

def exe_update(Node):
    table_name = Node.table_name
    set_list = Node.set_lists
    where_list = Node.where_lists
    colum_lists = []
    with open(current_database_path+"sys.dat",'r') as f:
        for line in f:
            if table_name == line.split()[0]:
                colum_lists = colum_lists + [[line.split()[2]] + [line.split()[3]]]  ##[[sname char][sage int]] 的形式
    with open(current_database_path+table_name+".txt",'r') as f:
        with open(current_database_path+table_name+".txt.t",'w') as f_new:
            for line in f:
                line_dict = make_dict(colum_lists,line)
                if judge_where(line_dict,where_list):
                    new_line_split = line.split()
                    for tt in set_list:
                        for c in colum_lists:
                            if tt[0].attr_name == c[0]:
                                num = colum_lists.index(c)
                                new_line_split[num] = str(tt[1].value)
                                break
                    for s in new_line_split:
                        f_new.write(s+" ")
                    f_new.write("\n")
                else:
                    f_new.write(line)
    os.remove(current_database_path+table_name+".txt")
    os.rename(current_database_path+table_name+".txt.t",current_database_path+table_name+".txt")

def exe_exit(Node):
    print("The Program is exiting...")
    os._exit(0)

def Execute(result):
    if result.type == nodes.NodeType.start_type:
        exe_start(result)
    elif result.type == nodes.NodeType.create_database:
        exe_create_database(result)
    elif result.type == nodes.NodeType.show_databases:
        exe_show_databases(result)
    elif result.type == nodes.NodeType.drop_database:
        exe_drop_database(result)
    elif result.type == nodes.NodeType.use_database:
        exe_use_database(result)
    elif result.type == nodes.NodeType.create_table:
        exe_create_table(result)
    elif result.type == nodes.NodeType.show_tables:
        exe_show_tables(result)
    elif result.type == nodes.NodeType.drop_table:
        exe_drop_table(result)
    elif result.type == nodes.NodeType.select:
        exe_select(result)
    elif result.type == nodes.NodeType.insert:
        exe_insert(result)
    elif result.type == nodes.NodeType.delete:
        exe_delete(result)
    elif result.type == nodes.NodeType.update:
        exe_update(result)
    elif result.type == nodes.NodeType.exit:
        exe_exit(result)
    else: raise RuntimeError('Result Node Type Error')
