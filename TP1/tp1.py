import re 
import sys

#se ejecuta python tp1.py
a = re.compile(r':\d+s/[a-z]*/[a-z]*/g')
b = re.compile(r':%s/[a-z]*/[a-z]*/g')
c = re.compile(r':\d+\,\d+s/[a-z]*/[a-z]*/g')

print "Lista de argumentos: ", sys.argv
patron_init = sys.argv[1]
#VER DE INGRESAR OTRO PARAMETRO PARA LA LINEA ACTUAL O TODAS LAS LINEAS


val = re.compile(r':(\d+|%|\d+\,\d+)s/[a-z]*/[a-z]*/g')

#print(sys.argv[1])

if val.search(patron_init) != None:
    print ("Expresion regular VALIDA")
else:
    print ("Expresion INVALIDA")
    sys.exit()

archivo = open('/home/ub18/Documentos/2018/FTI/FTI/TP1/archivo.txt','r')

#lineas = archivo.readlines()[2]
#print(lineas)
#texto = archivo.read()

str_patron1 = re.split('/', patron_init)[1]
str_patron2 = re.split('/', patron_init)[2]

patron1 = re.compile(str_patron1)

if a.match(patron_init):
    print('patron ingresado A')
    num_linea = int(re.split(r'(:|s)',patron_init)[2])
    lineas = archivo.readlines()
    try:
        lineas[num_linea] = patron1.sub(str_patron2,lineas[num_linea])
        output = open("output.txt","w")
        output.writelines(lineas)
        print (lineas)
    except IndexError:
        print('linea inexistente')
elif b.match(patron_init):
    print('patron ingresado B\n')
    print('TEXTO ORIGINAL\n')
    texto = archivo.read()
    print(texto)
    print('\n')
    texto = patron1.sub(str_patron2,texto)
    print(texto)
else:
    print('patron ingresado C')

#print(patron_init)
#print(re.split(r'(:|s)',patron_init)[2])

#print( re.split('s', sys.argv[1]))


"""
palabras = re.split('/', sys.argv[1])
p1 = palabras[1]
p2 = palabras[2]

print ('voy a cambiar "' + p1 + '" por "' + p2 +'"')

archivo = open('/home/ub18/Documentos/2018/FTI/FTI/TP1/archivo.txt','r')
#print (archivo.read()) 
texto = archivo.read()

val = re.compile(p1)
texto = val.sub(p2,texto)

print(texto)

archivo = open('/home/ub18/Documentos/2018/FTI/FTI/TP1/archivo.txt','r')
linea = archivo.readlines()
try:
    print (linea[9])
except IndexError:
    print('linea inexistente')


##VALIDAR LA EXPRESION



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