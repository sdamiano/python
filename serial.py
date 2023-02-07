"""
0702023-Este código lee un módulo Raspberry Pi Pico que tiene conectado un sensor BME280
Se reciben los datos por puerto serial, se agregan a una lista, se exportan
en datalogger.txt y se muestran en pantalla, cada un minuto.
Siguendo la tendencia barométrica, se muestran las últimas tres horas en la gráfica
Y se exporta la gráfica de las últimas tres horas.
"""

import serial, time # Se importan las librerías serial, time, matplotlib y datetime
import matplotlib.pyplot as plt
from datetime import datetime

#plt.ion() # Activa el modo interactivo
fig, ax = plt.subplots() # Crea una figura y un eje
#plt.xlim(0,10)
#plt.ylim(995, 1020)
plt.xlabel("Tiempo (minutos)") #etiqueta eje x
plt.ylabel("Presión (hPa)") #etiqueta eje y
plt.suptitle("Barómetro BME280. Valor actual: ") #título general de la ventana

presion_values = [] #Creo lista vacías para gardar los valores de presión
tiempo = []         #Creo lista para guardar valores generados por datetime()

def DataLogger():   #Esta función convierte en cadena el dato de presión en str y lo guarda en el txt
    current_time = datos.strftime("%Y-%m-%d,%H:%M:%S")
    doc = open("datalogger.txt", "a") # Se crea un archivo en modo a (append)
    doc.write(current_time)
    doc.write(", ")
    doc.write(pressure_str)
    doc.write("\n")
    doc.close()

while True:
    ### Apertura y captura de datos 
    puertoSerial = serial.Serial('COM10', 9600)  # Configuro puerto (desde CMD: python -m serial.tools.list_ports para ver puertos)
    time.sleep(2) #Espera 2 segundos para conectarse al puerto serial
    datos = puertoSerial.readline() #Guardo la lectura en la variable DATOS
    
    cadena = str(datos) #Los convierto a valores de tipo cadena (string)
    presion = cadena[2:8] # Delimito la información al valor de la presión
    
    pressure = float(presion) # Convierto el valor de str a float para agregar a la lista
    presion_values.append(pressure) #Agrego valor de presión a la lista
    
    pressure_str = str(pressure) #casteo la lista y la convierto a str
    puertoSerial.close() #Cierro el puerto
    
    datos = datetime.now()
    current_time = datos.strftime("%Y-%m-%d,%H:%M:%S")
   
    print("La presión es de {} hPa, registro de {} horas".format(presion,current_time)) #Estado por consola
    
    tiempo.append(datos) #Agrego dato del tiempo a la lista
    
    if len(presion_values) == 180: # Chequeo condición para actualización de gráfica 
        plt.savefig("tendencia.png", dpi=600) # Cuando se cumple la condición, capturo la gráfica, en la misma ruta del .py
        del presion_values[:180] # Cuando actualizo cada un minuto -plt.pause(60)-
        del tiempo[:180] # son 180 lecturas correspondientes a las 3 últimas horas (tendencia bárica)
        plt.cla() #Limpio los 180 registros mas viejos de las listas de presión y tiempo. Y limpio gráfica.
           
    DataLogger()
    print(len(presion_values))
    ax.plot(tiempo, presion_values) # Dibujo el gráfico
    plt.title(pressure,color='red',fontsize=15) #Agrego en ventana el texto del valor actual de la presión, en rojo y en tamaño 15
    fig.canvas.draw() # Actualiza el gráfico
    plt.pause(60) #Cada 1 minutos actualiza valores de presión
