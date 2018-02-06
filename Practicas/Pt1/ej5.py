fichero=open('arxiu1.txt', 'r')
fichero2=open('arxiu2.txt', 'r')
lineas=fichero2.readlines()
#print(lineas)
count=1
lineas=list(map(int, lineas)) #convierte lista a una lista de ints
#print(lineas)
mostrar=fichero.readline()
while mostrar!="":

    #print(mostrar)
    if (count in lineas):
        print(mostrar)
    mostrar=fichero.readline()
    count+=1

fichero.close()
fichero2.close()
