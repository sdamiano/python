# python

Exportar HMTL para ser leído por ZaraRadio

Exportando datos para leer con el software de automatización de radios
ZaraRadio.
Éste código es la base para cargar datos de temperatura y humedad
para ser locutados por el mencionado software.
Aquí se harcodean los datos para probar que el archivo .html es reconocido
por el software.
Ideas, usar Raspberry Pico con sensor de TH y conectar con el Zara para datos locales
Sebastián Damiano 26/1/2022. 23.43 horas.

----------------------------------------------------------------------------------
Conversión de grados CELSIUS A FAHRENHEIT mediante el llamado de una función.
Sebastián Damiano. 12/1/2022 23:08 horas.
----------------------------------------------------------------------------------

Ejercicio experimental,
Calcular base de altura nubosa (plafond),
Fuente fórmulas: http://www.meteorologiafacil.com.ar/foros/index.php?topic=811.0
IMPORTANTE: Como refiere la fuente, la fórmula se basa en la atmósfera estándar,
es imprecisa y entre las razones, se destaca que el descenso de la temperatura
no es lineal y que puede haber inversiones de temperatura a baja altura, incluso
en superficie. < Usar con mucha cautela >.
Code Python: Sebastián Damiano. 09/01/2022

----------------------------------------------------------------------------------

Cálculo de humedad relativa partiendo de la temperatura del aire
y del punto de rocío, usando tablas I y II.
Fuente tablas SMN: www.youtube.com/watch?v=FdKqiPnqDCg&ab_channel=DtoCapacitacionSMN

Versión funcional.
Faltan cargar valores de temperatura inferiores a 10 grados y todas las negativas.
Completar código (pass y completar if). 
Eliminar redundancias.
Ver factibilidad de usar más funciones.
Revisar índices de tablas.
Hacer verificación de acceso de datos.
Verificar funcionalidad de rangos de humedad mínimos.
Correción de impresión doble de valores a tabla II.
Sebastián Damiano 09/01/2022 03.45 hs.

--------------------------------------------------------------------------------

Psicrómetro con Python. Se procesan valores de tabla provista por CENTREINAR
organizados en listas por temperatura del aire, desde +10 a +40 °C.
La diferencia del termómetro seco con el húmedo se ajusta mediante un if
y se utiliza como índice para ingresar a las distintas listas. 
Mejoras: Se hizo verificación de rango ingreso de datos.
Se valida que la temperatura del bulbo seco > bulbo húmedo.
Se completó la  carga de datos en las tablas.
Pendiente: hacer eficiente el código con uso de funciones, introducir algún concepto de
POO, mostrar valores en una ventana, hacer que el usuario interactúe con el programa
Sebastián Damiano. 04/01/22 23:42.
