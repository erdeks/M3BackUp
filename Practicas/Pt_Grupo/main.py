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
def menu():
    abrirFichero()
    while True:
        print("===============================================")
        print("======== M E N U   P R I N C I P A L ==========")
        print("===============================================")
        print("===      A.- Introduir un millonari.        ===")
        print("===      B.- Guardar milionari a disc.      ===")
        print("===      C.- Mostrar informacio millonaris. ===")
        print("===      D.- Mostrar milionari mes ric.     ===")
        print("===      E.- Modificar un milionari.        ===")
        print("===      X.- Sortir del programa.           ===")
        print("===============================================")
        op=(input("Elige una opcion: "))
        os.system("clear")
        if op=="A" or op=="a":
            intMillonario()
        elif op=="B" or op=="b":
            guardarFichero()
        elif op=="C" or op=="c":
            #mostrarDades()
            print("Estas en la Opcion C")
        elif op=="D" or op=="d":
            #masRico()
            print("Estas en la Opcion D")
        elif op=="E" or op=="e":
            #modificar()
            print("Estas en la Opcion E")
        if op=="X" or op=="x":
            break
        input("Pulsa cualquier tecla para continuar...")
        os.system("clear")
menu()
