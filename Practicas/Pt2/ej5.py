fichero1=open("ej5Origen.txt","r")
fichero2=open("ej5Destino.txt", "w")
fichero1.read()
posicion=fichero1.tell()
count=0
fichero1.seek(0)

while count<=posicion:
    lCodificar=fichero1.read(1)
    count+=1
    for i in range(128):
        if lCodificar==chr(i) and lCodificar>="a" and lCodificar<="z":
            lCodificar=chr((i+13)%26)
            fichero2.write(lCodificar+"\n")
print("Texto copiado y codificado con exito")
fichero1.close()
fichero2.close()
