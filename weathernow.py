#Exportando datos para leer con el software de automatización de radios
#ZaraRadio.
#Éste código es la base para cargar datos de temperatura y humedad
#para ser locutados por el mencionado software.
#Aquí se harcodean los datos para probar que el archivo .html es reconocido
#por el software.
#Ideas, usar Raspberry Pico con sensor de TH y conectar con el Zara
#Sebastián Damiano 26/1/2022. 23.43 horas.

TEMP = input("Ingrese temperatura: ") #Ingresar números enteros

HUMIDITY = input("Ingrese humedad: ")
               
doc = open("datos.html", "w") # Se crea un archivo en modo write

doc.write("<HTML>\n")
doc.write(f"Temperature:{TEMP}</ BR>\n")
doc.write(f"Humidity:{HUMIDITY}</ BR>\n")
doc.write("</HTML>")
doc.close()

