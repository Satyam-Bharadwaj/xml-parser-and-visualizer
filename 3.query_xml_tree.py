import ast
import sys

with open("Symbol-Table") as f:
  symbol = f.read().splitlines()

for i in range(len(symbol)):
    symbol[i]=ast.literal_eval(symbol[i])


def getNextNode(curnode,sub_query,pos_of_curnode,parent_node):
    l = []
    if sub_query == "firstChild":
        if len(symbol[curnode]['children'])>0:
            l.append(symbol[curnode]['children'][0])
            l.append(0)
            l.append(symbol[curnode]['num'])
        else:
            print("Invalid query");
            sys.exit()

    elif sub_query == "lastChild":
        if len(symbol[curnode]['children'])>0:
            length=len(symbol[curnode]['children'])
            l.append(symbol[curnode]['children'][length-1])
            l.append(length-1)
            l.append(symbol[curnode]['num'])
        else:
            print("Invalid query");
            sys.exit()

    elif sub_query == "nextSibling":
        if curnode !=0:
            parent_child_list=symbol[parent_node]['children']
            if int(pos_of_curnode)+1 < len(parent_child_list):
                l.append(parent_child_list[int(pos_of_curnode)+1])
                l.append(int(pos_of_curnode)+1)
                l.append(parent_node)
            else:
                print("Invalid query");
                sys.exit()
        else:
            print("Invalid query");
            sys.exit()


    elif sub_query == "previousSibling":
        if curnode !=0:
            parent_child_list=symbol[parent_node]['children']
            if int(pos_of_curnode)-1 >= 0:
                l.append(parent_child_list[int(pos_of_curnode)-1])
                l.append(int(pos_of_curnode)-1)
                l.append(parent_node)
            else:
                print("Invalid query");
                sys.exit()
        else:
            print("Invalid query");
            sys.exit()

    return l      

def getValue(node,sub_query):
    if type(node) is int:
        if sub_query == "nodeName":
            return symbol[node]['name']
        if sub_query == "nodeValue":
            return "null"
        if sub_query == "nodeType":
            return 1
    elif type(node) is tuple:
        if sub_query == "nodeName":
            return node[0]
        if sub_query == "nodeValue":
            return node[1]
        if sub_query == "nodeType":
            return 2

    elif type(node) is str:
        if sub_query == "nodeName":
            return "#text"
        if sub_query == "nodeValue":
            return node
        if sub_query == "nodeType":
            return 3

while 1:
    query = input("Enter your query : " )
    query_chunks = query.split(".")
    if query_chunks[0]=="documentElement":
        if query_chunks[1]=="nodeName":
            print("root\n");
        elif query_chunks[1]=="nodeValue":
            print("null\n")
        elif query_chunks[1]=="nodeType":
            print(1);
        continue
    if query_chunks[0]=="root":
        l=[0,0,-1]
        for i in range(1,len(query_chunks)-1):
            l=getNextNode(l[0],query_chunks[i],l[1],l[2])
            #print(l)
    else:
        print("Query should start from root node");
        sys.exit()

    print(getValue(l[0],query_chunks[len(query_chunks)-1]))





