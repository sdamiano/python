"""
Psicrómetro con Python.Se procesan valores de tabla provista por CENTREINAR
organizados en listas por temperatura del aire, desde +10 a +40 °C.
La diferencia del termómetro seco con el húmedo se ajusta mediante un if
y se utiliza como índice para ingresar a las distintas listas. (luego se adjuntará
la tabla para mostrar como es el uso manual de la misma).
Se hizo verificación de rango ingreso de datos.
Se valida que la temperatura del bulbo seco > bulbo húmedo.
Se terminó de cargar datos en las tablas.
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
t20 = [95,91,86,82,78,74,70,66,62,58,55,51,47,44,40,37,34]
t21 = [95,91,87,83,79,75,71,67,63,59,56,52,49,45,42,39,35]
t22 = [95,91,87,83,79,75,71,68,64,60,57,53,50,47,43,40,37]
t23 = [95,91,87,83,80,76,72,68,65,61,58,54,51,48,46,42,38]
t24 = [95,91,88,84,80,76,73,69,66,62,59,56,52,49,46,43,40]
t25 = [96,92,88,84,80,77,73,70,66,63,60,56,53,50,47,44,41]
t26 = [96,92,88,84,81,77,74,70,67,64,61,57,54,51,48,45,42]
t27 = [96,92,88,85,81,78,74,71,68,64,61,58,55,52,49,46,44]
t28 = [96,92,88,85,82,78,75,72,68,65,62,59,57,53,50,48,45]
t29 = [96,92,89,85,82,79,75,72,69,66,63,60,57,54,51,49,46]
t30 = [96,92,89,86,82,79,76,73,69,66,63,61,58,55,52,49,47]
t31 = [96,92,89,86,82,79,76,73,70,67,64,61,58,56,53,50,48]
t32 = [96,93,89,86,83,80,77,74,71,68,65,62,59,57,54,51,49]
t33 = [96,93,89,86,83,80,77,74,71,68,65,63,60,57,55,52,50]
t34 = [96,93,90,86,83,80,77,74,71,69,66,63,61,58,55,53,50]
t35 = [96,93,90,87,84,81,78,75,72,69,66,64,61,59,56,54,51]
t36 = [96,93,90,87,84,81,78,75,72,70,67,64,62,59,57,54,52]
t37 = [96,93,90,87,84,81,78,76,73,70,67,65,62,60,57,55,53]
t38 = [96,93,90,87,84,81,79,76,73,71,68,65,63,60,58,56,53]
t39 = [96,93,90,87,85,82,79,76,74,71,68,66,63,61,59,56,54]
t40 = [96,93,90,88,85,82,79,77,74,71,69,66,64,62,59,57,55]
t41 = [96,94,91,88,85,82,80,77,74,72,69,67,64,62,60,58,55]
t42 = [97,94,91,88,85,82,80,77,75,72,70,67,65,63,60,58,56]
t43 = [97,94,91,88,85,83,80,77,75,72,70,68,65,63,61,59,56]
t44 = [97,94,91,88,86,83,80,78,75,73,70,68,66,64,61,59,57]
t45 = [97,94,91,88,86,83,81,78,76,73,71,68,66,64,62,60,58]
t46 = [97,94,91,88,86,83,81,78,76,73,71,69,67,64,62,60,58]
t46 = [97,94,91,89,86,83,81,79,76,74,71,69,67,65,63,61,59]
t48 = [97,94,91,89,86,84,81,79,76,74,72,70,67,65,63,61,59]
t49 = [97,94,91,89,86,84,81,79,77,74,72,70,68,66,63,61,59]
t50 = [97,94,92,89,86,84,82,79,77,75,72,70,68,66,64,62,60]

def validar_resta():
    if resta > 8.5:
        print("Error, datos fuera de rango, el valor no puede superar los 8.5")
        quit()
    else:
        print("La depresión psicrométrica es de:", resta)
    return

#input para cargar temperatura del aire como float

tseco = float(input("Ingrese valor numérico -entero- de termómetro seco: "))

#Verificar validez de dato ingresado

while tseco < 10 or tseco > 50:
    print("El valor ingresado no es válido")
    tseco = float(input("Ingrese temperatura de bulbo seco en enteros (entre 10 y 50 grados): "))

#input para cargar temperatura del bulbo humedecido como float

thumedo = float(input("Ingrese temperatura de bulbo humedo, puede tener decimal .5: "))

#Verificar validez de dato ingresado
while thumedo > tseco:
    print("Valor incorrecto, el húmedo no puede ser superior al seco")
    humedo = float(input("Ingrese temperatura de bulbo humedo, puede tener decimal .5: "))

#Obtengo la depresión psicrométrica restando ambos valores y los muestro en pantalla
resta = (tseco - thumedo)

validar_resta()

#Declaro un valor inicial de índice

indice = 0

#Ajuste del valor de la resta para que busque en el índice correcto en la lista correspondiente

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
     print("Valor no válido")

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
    
elif tseco == 23:
    print("La humedad relativa es del:",t23[indice],"%")

elif tseco == 24:
    print("La humedad relativa es del:",t24[indice],"%")

elif tseco == 25:
    print("La humedad relativa es del:",t25[indice],"%")

elif tseco == 26:
    print("La humedad relativa es del:",t26[indice],"%")

elif tseco == 27:
    print("La humedad relativa es del:",t27[indice],"%")

elif tseco == 28:
    print("La humedad relativa es del:",t28[indice],"%")

elif tseco == 29:
    print("La humedad relativa es del:",t29[indice],"%")

elif tseco == 30:
    print("La humedad relativa es del:",t30[indice],"%")

elif tseco == 31:
    print("La humedad relativa es del:",t31[indice],"%")

elif tseco == 32:
    print("La humedad relativa es del:",t32[indice],"%")
    
elif tseco == 33:
    print("La humedad relativa es del:",t33[indice],"%")

elif tseco == 34:
    print("La humedad relativa es del:",t34[indice],"%")

elif tseco == 35:
    print("La humedad relativa es del:",t35[indice],"%")

elif tseco == 36:
    print("La humedad relativa es del:",t36[indice],"%")

elif tseco == 37:
    print("La humedad relativa es del:",t37[indice],"%")

elif tseco == 38:
    print("La humedad relativa es del:",t38[indice],"%")

elif tseco == 39:
    print("La humedad relativa es del:",t39[indice],"%")

elif tseco == 40:
    print("La humedad relativa es del:",t40[indice],"%")

else:
    quit()
    
    