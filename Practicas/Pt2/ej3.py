def escribirFichero(lista):
    fichero = open("ej3.txt", "w")
    for i in range (len(lista)):
        fichero.write(lista[i])
    print("Guardado con Exito")
    fichero.close()


delimitador=input("Introduce el delimitador: ")
campos=int(input("Introduce el numero de campos que quieres que tenga la lista: "))
count=1
lista=[]
while count<=campos:
    l=input("Introduce un campo de la lista: ")
    lista.append(l+delimitador+" ")
    count+=1
escribirFichero(lista)
