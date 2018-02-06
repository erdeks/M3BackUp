#!/usr/bin/python
# -*- coding: latin-1 -*-
"""def escribirFicheros():
    #abrirFicheros()
    fp=open("parells.txt", "w")
    fs=open("senars.txt", "w")
    for i in range (1, 101):
        if i%2==0:
            fp.write(str(i))
        else:
            print(i);
            fs.write(str(i))
    fp.close()
    fs.close()
    #cerrarFicheros()

escribirFicheros()"""
fitxer1=open("parells.txt","w")
fitxer2=open("senars.txt","w")

for i in range(2,101,2):
	fitxer1.write(str(i)+'\n')

for i in range(1,100,2):
	fitxer2.write(str(i)+'\n')

fitxer1.close()
fitxer2.close()
