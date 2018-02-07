def abrirFichero(fichero):
	listaFin=[]
	fichero = open(fichero, "r")
	linea = fichero.readline()
	while linea != '':
		lista = linea.split('\n')
		listaFin.append(lista)
		linea = fichero.readline()
	fichero.close()
	return listaFin
def escribirFichero(lista):
    fichero = open("ej2Copia.txt", "w")
    for i in range (len(lista)):
        for j in range (len(lista[i])):
            fichero.write(lista[i][j])
            if (len(lista[i])-1)>j:
                fichero.write("\n")
    print("Copiado con Exito")
    fichero.close()
a=abrirFichero('ej2.txt')
escribirFichero(a)
