def cargarDatos(fichero):
    fichero=open(fichero, "r")
    linea=fichero.readline()
    diccionario={}
    while linea != "":
        lista=linea.split)(":")
