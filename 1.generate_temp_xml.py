f=open("xml_file_input.xml","r")
w=open("temp_xml_generated","w")
l=f.readlines()
i=0
while(i<len(l)):
	l[i]=l[i].strip()
	l[i]=l[i].strip('\n')
	i+=1

x="".join(l)

i=0
y=""
while i<len(x)-1:
	y=y+x[i]
	if(x[i+1]==">" and i!=len(x)-2):
		y=y+x[i+1]+"\n"
		i+=1
	if(x[i+1]=="<"and x[i]!=">"):
		y=y+"\n"
	i+=1
y=y+">"
w.write(y)