import os
fichero=open('lorem.txt', 'w')
texto='All paid jobs absorb and degrade the mind. If Beethoven had been killed in a plane crash at the age of 22, it would have changed the history of music... and of aviation. I do not have a psychiatrist and I do not want one, for the simple reason that if he listened to me long enough, he might become disturbed.'
#Escribimos el fichero
fichero.writelines(texto)
fichero.close()
fichero=open('lorem.txt', 'r')
lineas=fichero.readlines()
#volvemos a la posicion inicial del fichero
fichero.seek(0,0)
print(fichero.tell())
#buscamos la palabra mind
for linea in lineas:
    palabras=linea.split(' ')
    for palabra in palabras:
        print(fichero.tell())
        if palabra.strip('.') == 'mind':
            print(palabra)
            break
for linea in lineas:
    palabras=linea.split(' ')
    for palabra in palabras:
        print(fichero.tell())
        if palabra.strip('.') == 'Beethoven':
            print(palabra)
            break
tamano=os.path.getsize ("lorem.txt")
tamanok=tamano/1024
print("El fichero pesa: "+str(tamano)+" bytes y "+str(tamanok)+" KBytes")

fichero.close()
