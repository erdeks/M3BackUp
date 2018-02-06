fichero=open("ejemplos.txt", "r")
lista = f.readlines()
for i in lista:
    print (i)
fichero.close()
