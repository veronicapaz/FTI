import re 

valor1 = re.compile(r'(/^(foo){1}$/)')
valor2 = re.compile(r'(/^(bar){1}$/)')
#crea una expresion regular

try:
		archivo = open('/home/veronica/Documentos/FTI 2018/TP1/archivo.txt','r') 
except IOError:		
		print("Error -> No se puede abrir el archivo")
else:
		texto = archivo.read()
		texto_reemplazado = re.sub(valor1,valor2,texto)
		archivo.close

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