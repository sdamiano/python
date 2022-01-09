# Ejercicio experimental
# Calcular base de altura nubosa (plafond)
# Fuente fórmulas: http://www.meteorologiafacil.com.ar/foros/index.php?topic=811.0
# IMPORTANTE: Como refiere la fuente, la fórmula se basa en la atmósfera estándar
# es imprecisa y entre las razones se destaca que el descenso de la temperatura
# no es lineal y que puede haber inversiones de temperatura a baja altura, incluso
# en superficie. Usar con mucha cautela.
# Code Python: Sebastián Damiano. 09/01/2022

#Entrada de valor de temperatura
t = float(input("Ingrese temperatura del aire en centígrados: "))

#Entrada de valor de temperatura de punto de rocío
pr = float(input("ingrese temperatura del punto de rocio: "))

#Fórmula para calcular la altura en metros
plafond_m = (t - pr) * (1000 / 6.5)

#Fórmula para calcular la altura en pies
plafond_p =(t - pr) * (3333.3 / 6.5)

#Redondeo valores, sin decimales
base = round(plafond_m)
base2 = round(plafond_p) 

#Muestro el valor por pantalla en metros y en pies
print("La base de la nube más baja en METROS es:", base)
print("La base de la nube más baja en PIES es:", base2)
           
#Posteriormente agregar cifra del plafond según código SYNOP