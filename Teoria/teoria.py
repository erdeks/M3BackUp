import os, shutil
#Cambiar nombre al archivo
"""os.rename("ej4.txt", "lorem.txt")
print("Nombre cambiado con exito")"""
#Eliminar un archivo
"""os.remove("lorem.txt")
print("Eliminado con exito")"""
#Copiar archivo
#shutil.copy("ej4.txt", "lorem.txt")
"""shutil.copytree("../Practicas", "Teoria")
print("copiado con exito")"""

#shutil.move("../prueba", "../Practicas/prueba")
shutil.rmtree("Teoria")
