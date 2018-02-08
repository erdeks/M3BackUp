import os, sys
global acciones
global nomEmpresa
acciones=[]
nomEmpresa={}
def abrirFichero():
	precioAcciones=[]
	fichero = open("txt/acciones.txt", "r")
	linea = fichero.readline()
	while linea != '':
		lista = linea.split('|')
		precioAcciones.append(lista)
		linea = fichero.readline()
	for i in range(len(precioAcciones)):
		nomEmpresa.setdefault(precioAcciones[i][0],float(precioAcciones[i][1]))
	if acciones==[]:
		fichero2=open("txt/millonarios.txt","r")
		linea=fichero2.readline()
		while linea!="":
			lista=linea.split("|")
			acciones.append(lista)
			linea=fichero2.readline()
		fichero2.close()
	fichero.close()
	return fichero

def intMillonario():
    print("===============================================")
    print("=============== NUEVO MILLONARIO ==============")
    print("===============================================")
    nombre=input("Introduce el nombre: ")
    edad=input("Introduce la edad: ")
    a=[]
    a.append(nombre)
    a.append(edad)
    for i in nomEmpresa:
        print(i, ": ")
        accio=float(input())
        a.append(accio)
    a.append(str(a[len(nomEmpresa)-1])+"\n")
    acciones.append(a)
    return acciones
def guardarFichero():
    print("===============================================")
    print("============== GUARDAR EN FICHERO =============")
    print("===============================================")
    fichero=open("txt/millonarios.txt", "w")
    for k in range(len(acciones)):
        for j in range(len(acciones[k])):
            fichero.write(str(acciones[k][j]))
            if j<len(acciones[k])-1:
                fichero.write(";")
    fichero.close()
    p="."
    for r in range(0,73):
        print("\n\n\n")
        print("LOADING",p)
        os.system("clear")
        p+="."
    print("\n\n\n\t\t Guardado correctamente")
def modificar():
	encontrado=0
	print("===============================================")
	print("================ MODIFICAR RICO ===============")
	print("===============================================")
	nombre=input("Introduce el nombre: ")
	nombre=nombre.upper()
	for i in range(len(acciones)):
		if nombre==acciones[i][0].upper():
			nombre=input("Introduce nombre: ")
			edad=int(input("Introduce la edad: "))
			print("Introduce las acciones de cada empresa")
			a=[]
			a.append(nombre)
			a.append(edad)
			for j in nomEmpresa:
				print(j, ": ")
				accion=float(input())
				a.append(accion)
			a.append(str(a[len(nomEmpresa)-1])+"\n")
			acciones[i]=a
			encontrado=0
			break
		else:
			encontrado=1
	if encontrado==1:
		print("No se ha encontrado al millonario.")
	fichero=open("txt/millonarios.txt", "w")
	for k in range(len(acciones)):
		for j in range(len(acciones[k])):
			fichero.write(str(acciones[k][j]))
			if j<len(acciones[k])-1:
				fichero.write(";")
	fichero.close()
