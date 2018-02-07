fichero=open("ej4.txt","r")
fichero.read()
posicion=fichero.tell()
posicion=int(posicion)
print("El archivo tiene ",posicion," caracteres.")
fichero.seek(0)
linea=fichero.readline()
count=0
while linea!="":
    linea=fichero.readline()
    count+=1
print("El archivo tine ",count," lineas.")
fichero.seek(0)

cuentaPal=0
count=0;
while cuentaPal<=posicion:
    palabra=fichero.read(1)
    cuentaPal+=1
    if palabra==" " or palabra=="\n":
        count+=1
print("El archivo tiene ",count," palabras.")
