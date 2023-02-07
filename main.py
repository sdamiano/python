from machine import Pin, I2C
from time import sleep_ms
import ssd1306
import bme280
pressure_values = [] #Creo la lista donde voy a guardar los valores leídos.

# Inicializa el sensor BME280 y el display SSD1306
i2c = I2C(1,scl=Pin(19), sda=Pin(18))
bme = bme280.BME280(i2c=i2c)
display = ssd1306.SSD1306_I2C(128, 64, i2c)

while True:
# Lee la presión atmosférica del sensor BME280, casteo los valores saco unidad hpa y dejo el número
    pressure = bme.values[1]
    pressure_num = pressure[:6]
    #print(type(pressure_num))
    
    presion = float(pressure_num)
    print(pressure_num)
    
# Muestra la presión atmosférica en el display SSD1306
    display.fill(0)
    display.text(pressure_num, 25, 30)
    display.show()
    sleep_ms(10000)