fichero=open("ej1.txt", "r")
num=input("Introduce el numero de lineas que quieres ver: ")
num=int(num)
count=1
linea=fichero.readline()
while linea!="":

    if count<=num:
        print(linea)
    else:
        break
    linea=fichero.readline()
    count+=1
fichero.close()
