#Ejemplo simple de cómo exportar datos a un archivo formateado para HTML con Python (02/01/2022)

# El index.html aparecerá en la misma carpeta donde está el archivo .py
# Funciona para correrlo desde un servidor Apache. 
# Resulta interesante con datos dinámicos los que aportan sensores meteorol&oacute;gicos

doc = open("index.html", "w") # Se crea un archivo en modo write

doc.write("<html>")
doc.write("<head>")
doc.write("<title>Exportar HTML con PYTHON</title>")
doc.write("</head>")
doc.write("<body style='background-color:F0EBA5;'>")
doc.write("<center>")
doc.write("<B>Prueba de escritura formateada para HTML</B>")
doc.write("<br>")
doc.write("Se pueden agregar variables convirti&eacute;ndolas a STR")
doc.write("<br>")
doc.write("<I>Y se puede publicar a través de un servidor Apache para hacerlo visible en la web</I>")
doc.write("<br>")
doc.write("<A HREF='https://github.com/'>GitHub: Where the world builds software</A>")
doc.write("</center>")
doc.write("</body>")
doc.write("</html>")
doc.close() 
