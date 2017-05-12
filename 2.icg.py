stack = []

symbol=[]
test={}
keyVal=[]
carry=[]
st=open("Symbol-Table","w")
icg=open("ICG.dot","w")
n=1

test['name']="root"
test['num']=0
test['children']=[]
test['attributes']={}
test['data']=''
test['parent']=-1
symbol.append(test)

with open("temp_xml_generated", 'r') as parse_file:
	for line in parse_file:
		ltag = line.find('<')
		if ltag > -1:
			rtag = line.find('>')
			if rtag > -1:
				test={}
				node = line[ltag+1: rtag]
				hold = node.split()
				tagName=hold[0]
				open_tag = tagName[0] != '/'
				if open_tag:
					if(len(hold)>0):
						for i in range(len(hold)):
							if i==0 :
								if stack == []:
									test['parent']="root"
									symbol[0]['children'].append(n)
								else:
									parent_id=carry[-1]['num']
									test['parent']=parent_id
									symbol[parent_id]['children'].append(n)
								stack.append(tagName)
								test['name']=tagName
								test['children']=[]
							else:
								temp = hold[i].split("=")
								pair=(temp[0],temp[1].replace('"',''))
								keyVal.append(pair)
					test['attributes']=keyVal
					test['num']=n
					test['data']=''
					test['children'].extend(keyVal)		
					keyVal=[]
					carry.append(test)
					symbol.append(test)
					n=n+1
				else:
					tagName = tagName[1:]
					if len(stack) == 0:
						print("No blocks are open; tried to close", tagName)
					else:
						if stack[-1] == tagName:
							stack.pop()
							carry.pop()
						else:
							break
		else:
			if stack != []:
				holding = carry[-1]['data']
				holding = holding + line
				carry[-1]['data']=holding.strip("\n")
				symbol[carry[-1]['num']]['children'].append(carry[-1]['data'])


	   
if len(stack):
	print ("Blocks still open at EOF:", stack)

icg.write("graph taxonomic_graph{\n ")
for row in  symbol:
	if row['name']!="root":
		node=str(row['num'])+":"+row['name']+" "
		for a,b in row['attributes']:
			icg.write('"'+node+'"--"'+str(row['num'])+":"+a+" = "+b+'" [style=dotted] \n')
		parent=row['parent']
		if(parent!='root'):
			index=int(parent)
			parent=symbol[index]['name']+" "
			parent=str(symbol[index]['num'])+":"+parent
		
		icg.write('"'+parent+'"--"'+node+'"\n')
		if(len(row['data'])!=0):
			icg.write('"'+node+'"-- "'+row['data']+'"\n')
icg.write('}')

for x in symbol:
	st.write(str(x))
	st.write("\n")
