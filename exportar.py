#Ejemplo simple de cómo exportar datos a un archivo txt con Python (02/01/2022)

#Se crea un archivo de texto, al que se le escriben los inputs de nombre
#y apellido, separado por un espacio. Luego se cierra el archivo.
#El .txt aparecerá en la misma carpeta donde está el archivo .py
# He aplicado esto para la creación de un index.html y funciona perfecto para
#correrlo desde un servidor Apache. Será motivo del próximo artículo.

separador = " " #Opcional, se crea un espacio para mostrar las cadenas.

data = open("exportar.txt", "w") # Se crea un archivo en modo write

nombre = input("Ingrese su nombre: ") # Se crean las cadenas de datos
apellido = input("Ingrese su apellido: ") # Se crea segunda cadena

data.write(nombre)    #Se escribe el primer dato 
data.write(separador) #Se le aplica un espacio
data.write(apellido)  #Se escribe un segundo dato
data.close()          #Se cierra el archivo

    