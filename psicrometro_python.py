"""
Psicrómetro con Python.Se procesan valores de tabla provista por CENTREINAR
organizados en listas por temperatura del aire, desde +10 a +40 °C.
La diferencia del termómetro seco con el húmedo se ajusta mediante un if
y se utiliza como índice para ingresar a las distintas listas. (luego se adjuntará
la tabla para mostrar como es el uso manual de la misma).
Este primer bosquejo está funcional. Devuelve los valores correctos.
Falta: hacer verificación de ingreso de datos, validarlos para poder
operar correctamente. Por física, por ejemplo, la temperatura del bulbo húmedo
jamás puede ser mayor a la del bulbo seco.
Terminar de cargar datos en las tablas, se hizo copy&paste para probar
Hacer eficiente el código con uso de funciones, introducir algún concepto de
POO, mostrar valores en una ventana, hacer que el usuario interactúe con el programa
Sebastián Damiano. 04/01/22
"""
#Tablas de los valores de temperatura del aire (bulbo seco)

t10 = [94,88,82,76,71,65,60,54,49,44,39,34,29,24,19,14,10]
t11 = [94,88,82,77,72,66,61,56,51,46,41,36,31,27,22,17,13]
t12 = [94,88,83,78,72,67,62,57,52,48,43,38,34,29,25,20,16]
t13 = [94,89,84,78,73,68,63,59,54,49,45,40,36,31,27,23,19]
t14 = [94,89,84,79,74,69,65,60,55,51,46,42,38,34,29,25,21]
t15 = [94,89,84,80,75,70,66,61,57,52,48,44,40,36,32,28,24]
t16 = [95,90,85,80,76,71,67,62,58,54,50,45,41,37,34,30,26]
t17 = [95,90,85,81,76,72,68,63,59,55,51,47,43,39,35,32,28]
t18 = [95,90,86,81,77,73,68,64,60,56,52,48,45,41,37,34,30]
t19 = [95,90,86,82,77,73,69,65,61,57,54,50,46,42,39,35,32]
#hasta acá valores correctos cargados.
t20 = [94,88,82,77,72,66,61,56,51,46,41,36,31,27,22,17,13]
t21 = [94,88,82,77,72,66,61,56,51,46,41,36,31,27,22,17,13]
t22 = [95,91,87,77,72,66,61,56,51,46,41,36,31,27,22,17,13]
t23 = [94,88,82,77,72,66,61,56,51,46,41,36,31,27,22,17,13]
t24 = [94,88,82,77,72,66,61,56,51,46,41,36,31,27,22,17,13]
t25 = [94,88,82,77,72,66,61,56,51,46,41,36,31,27,22,17,13]
t26 = [94,88,82,77,72,66,61,56,51,46,41,36,31,27,22,17,13]
t27 = [94,88,82,77,72,66,61,56,51,46,41,36,31,27,22,17,13]
t28 = [94,88,82,77,72,66,61,56,51,46,41,36,31,27,22,17,13]
t29 = [94,88,82,77,72,66,61,56,51,46,41,36,31,27,22,17,13]
t30 = [94,88,82,77,72,66,61,56,51,46,41,36,31,27,22,17,13]
t31 = [94,88,82,77,72,66,61,56,51,46,41,36,31,27,22,17,13]
t32 = [94,88,82,77,72,66,61,56,51,46,41,36,31,27,22,17,13]
t33 = [94,88,82,77,72,66,61,56,51,46,41,36,31,27,22,17,13]
t34 = [94,88,82,77,72,66,61,56,51,46,41,36,31,27,22,17,13]
t35 = [94,88,82,77,72,66,61,56,51,46,41,36,31,27,22,17,13]
t36 = [94,88,82,77,72,66,61,56,51,46,41,36,31,27,22,17,13]
t37 = [94,88,82,77,72,66,61,56,51,46,41,36,31,27,22,17,13]
t38 = [94,88,82,77,72,66,61,56,51,46,41,36,31,27,22,17,13]
t39 = [94,88,82,77,72,66,61,56,51,46,41,36,31,27,22,17,13]
t40 = [94,88,82,77,72,66,61,56,51,46,41,36,31,27,22,17,13]

#input para cargar temperatura del aire
seco = input("Ingrese temperatura de bulbo seco en enteros: ")

#input para cargar temperatura del bulbo humedecido
humedo = input("Ingrese temperatura de bulbo humedo, puede tener decimal .5: ")

#conversion a float para poder restar valores
tseco = float(seco)
thumedo = float(humedo)

#verificación para chequear luego
if thumedo > tseco:
    pass
    print("ERROR: verifique datos ingresados, Seco siempre es mayor que Húmedo") # Comprobación de datos válidos. Seco siempre es igual o superior al húmedo
else:
    resta = float(tseco - thumedo)
    
print("La depresión psicrométrica es de: ",resta)

indice = 0

if resta < 1:
    indice = 0

elif resta == 1:
    indice = 1

elif resta == 1.5:
    indice = 2

elif resta == 2:
    indice = 3  

elif resta == 2.5:
    indice = 4

elif resta == 3:
    indice = 5

elif resta == 3.5:
    indice = 6  

elif resta == 4:
    indice = 7

elif resta == 4.5:
    indice = 8  

elif resta == 5:
    indice = 9

elif resta == 5.5:
    indice = 10

elif resta == 6:
    indice = 11 

elif resta == 6.5:
    indice = 12

elif resta == 7:
    indice = 13

elif resta == 7.5:
    indice = 14

elif resta == 8:
    indice = 15 

elif resta == 8.5:
    indice = 16
     
else:
     print("El valor obtenido no es válido")

# Muestra del valor de la humedad relativa, se llama a la tabla correspondiente
#a la temperatura de bulbo seco y se apunta al indice ajustado en el ciclo de IF anterior 
if tseco == 10:
    print("La humedad relativa es del:",t10[indice], "%")

elif tseco == 11:
    print("La humedad relativa es del:",t11[indice], "%")

elif tseco == 12:
    print("La humedad relativa es del:",t12[indice], "%")

elif tseco == 13:
    print("La humedad relativa es del:",t13[indice],"%")

elif tseco == 14:
    print("La humedad relativa es del:",t14[indice],"%")

elif tseco == 15:
    print("La humedad relativa es del:",t15[indice],"%")

elif tseco == 16:
    print("La humedad relativa es del:",t16[indice],"%")

elif tseco == 17:
    print("La humedad relativa es del:",t17[indice],"%")

elif tseco == 18:
    print("La humedad relativa es del:",t18[indice],"%")

elif tseco == 19:
    print("La humedad relativa es del:",t19[indice],"%")

elif tseco == 20:
    print("La humedad relativa es del:",t20[indice],"%")

elif tseco == 21:
    print("La humedad relativa es del:",t21[indice],"%")

elif tseco == 22:
    print("La humedad relativa es del:",t22[indice],"%")
else:
    pass
    