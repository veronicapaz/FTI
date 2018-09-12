import re 
import sys

#se ejecuta python tp1.py

print "Lista de argumentos: ", sys.argv

#VER DE INGRESAR OTRO PARAMETRO PARA LA LINEA ACTUAL O TODAS LAS LINEAS


val = re.compile(r':(% | \d+,\d+)?s/[a-z]*/[a-z]*/g')

#val = re.compile(r':(\d+)?,?[1-9]?[1-9]?%?s/[a-z]*/[a-z]*/g')
print(sys.argv[1])

if val.search(sys.argv[1]) != None:
    print ("Expresionn re contra valida")
else:
    print ("Expresion invalida")


palabras = re.split('/', sys.argv[1])
p1 = palabras[1]
p2 = palabras[2]

print ('voy a cambiar ' + p1 + 'por ' + p2)

archivo = open('/home/ub18/Documentos/2018/FTI/FTI/TP1/archivo.txt','r')
print (archivo.read()) 



##VALIDAR LA EXPRESION


"""
cadena = raw_input('Introduce una cadena de texto: ')
print 'La cadena que ingreso es:\n',cadena
valor1 = re.compile(r'foo')
#valor1 = re.compile(r'\b(F|f)oo\b')
cadena2 = valor1.sub("bar",cadena)
print 'La cadena resultante:\n',cadena2

#resultado = re.search(r'\b(F|f)oo\b', cadena)
#print 'La cadena buscada es:\n',resultado

#valor1 = re.compile(r'(/^(foo){1}$/)')
#valor2 = re.compile(r'(/^(bar){1}$/)')
#crea una expresion regular

#try:
archivo = open('/home/ub18/Documentos/2018/FTI/FTI/TP1/archivo.txt','r')
print (archivo.read()) 
#except IOError:		
#		print("Error -> No se puede abrir el archivo")
#else:
#		texto = archivo.read()
#		texto_reemplazado = re.sub(valor1,valor2,texto)
#		archivo.close

#texto_reemplazado = re.sub(pattern=(r'(/^(foo){1}$/)'),(r'(/^(bar){1}$/)'))
#el de abajo es un ejemplo que probe y que anda, cambia lo que esta escrito 
#en un txt por lo q esta escrito en el otro
#import re
#output = open("output.txt","w")
#input = open("input.txt").read()

#output.write(re.sub(r'^(.{4})(.{4})(.{4})(.{3})$',
 #                   r'\1\4\2\3', 
  #                  input, 
   #                 flags=re.M))

#output.close()


#sub_cadena = re.search(r"h", "hola mundo")
#print(sub_cadena.group())
#para utilizar las expresiones regulares
"""