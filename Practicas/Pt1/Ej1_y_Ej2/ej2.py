f1=open("parells.txt","r")
f2=open("senars.txt","r")
f3=open("1a100.txt","w")

i=0

while i<50:
	num=f2.readline()
	f3.write(num)
    #print(num)
	num=f1.readline()
	f3.write(num)
	i+=1
print('fichero escrito')
f1.close()
f2.close()
f3.close()
