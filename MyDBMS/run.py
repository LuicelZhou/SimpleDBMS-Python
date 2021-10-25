import nodes
from lexer import lexer as lex
from yaccer import yaccer as yacc
from execute import Execute

if __name__ == '__main__':
    print("|--------------------DBMS by python--------------------|")
    print("|------------------------------------------------------|")
    print("|-----------author : 周雨杨-id ：17030140008----------|")
    while True:
        command = input ('SQL>')
        result = yacc.parse(command,lexer=lex)
        #print(type(result))

        if not result:continue
        Execute(result)
