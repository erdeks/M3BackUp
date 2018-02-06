f=open("persones.txt",'r')
informacio=f.readline()
while informacio!='':
	lista=informacio.split('-')

	if int(lista[3])>18:
		print(lista[0],'\t',lista[1]," es mayor de edad")
	informacio=f.readline()
