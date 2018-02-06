lista=[]

def llegirPersona():
	nom=input("NOM: ")
	cognom=input("COGNOM: ")
	nif=input("NIF: ")
	edat=int(input("EDAD: "))
	alt=float(input("ALÇADA: "))
	lista1=[nom,cognom,nif,edat,alt]
	lista.append(lista1)

def escriurePersonaADisc(p):
	f=open("persones.txt","a")
	f.write(p[0]+'-'+p[1]+'-'+p[2]+'-'+str(p[3])+'\t'+str(p[4])+'\n')
	print(p[0]+'-'+p[1]+'-'+p[2]+'\n')
	f.close()

opcio=''
while opcio!='X':
	print("A.-Pedir datos")
	print("B.-Guardar datos")
	print("X.-sortir")
	opcio=input("Escull una opcio: ").upper()
	if opcio=='A':
		llegirPersona()
	elif opcio=='B':
		for i in lista:
			escriurePersonaADisc(i)
	elif opcio=='X':
		print("Adeu")
	else:
		print("Opcio no vàlida")
