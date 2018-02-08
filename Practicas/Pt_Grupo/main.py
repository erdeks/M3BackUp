import funciones
from funciones import abrirFichero, intMillonario, guardarFichero, modificar
import os, sys
global acciones
global nomEmpresa
acciones=[]
nomEmpresa={}

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
            modificar()
            print("Estas en la Opcion E")
        if op=="X" or op=="x":
            break
        input("Pulsa cualquier tecla para continuar...")
        os.system("clear")
menu()
