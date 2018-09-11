import re 
import sys
valor1 = re.compile(r'foo')

print 'Introduzca lineas de texto'

contador_palabras = 0
while (contador_palabras<4):
	cadena = raw_input("linea:")
	cadena_resultado = valor1.sub("bar",cadena)
	contador_palabras = contador_palabras + 1
	print 'La cadena resultante:\n',cadena_resultado