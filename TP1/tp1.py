import re 
import sys

#se ejecuta python tp1.py
ER_A = re.compile(r':\d+s/[a-z]*/[a-z]*/g')
ER_B = re.compile(r':%s/[a-z]*/[a-z]*/g')
ER_C = re.compile(r':\d+\,\d+s/[a-z]*/[a-z]*/g')

patron_init = sys.argv[1]

val = re.compile(r':(\d+|%|\d+\,\d+)s/[a-z]*/[a-z]*/g')

if val.search(patron_init) != None:
    print ("Expresion regular VALIDA\n")
else:
    print ("Expresion INVALIDA\n")
    sys.exit()

archivo = open('/home/ub18/Documentos/2018/FTI/FTI/TP1/archivo.txt','r')

str_patron1 = re.split('/', patron_init)[1]
str_patron2 = re.split('/', patron_init)[2]

patron1 = re.compile(str_patron1)

if ER_A.match(patron_init):
    print('Exp. Reg. A\n')
    num_linea = int(re.split(r'(:|s)',patron_init)[2])
    lineas = archivo.readlines()
    try:
        lineas[num_linea] = patron1.sub(str_patron2,lineas[num_linea])
    except IndexError:
        print('linea inexistente\n')
elif ER_B.match(patron_init):
    print('Exp. Reg. B\n')
    lineas = archivo.read()
    lineas = patron1.sub(str_patron2,lineas)
else:
    print('Exp. Reg. C\n')
    lin_ini = int(re.split(r'(:|\,|s)',patron_init)[2])
    lin_fin = int(re.split(r'(:|\,|s)',patron_init)[4])
    if lin_ini > lin_fin:
        print('Rango de lineas incorrectos\n')
        sys.exit()
    try:
        lineas = archivo.readlines()
        for i in range(lin_ini, lin_fin+1):
            lineas[i] = patron1.sub(str_patron2,lineas[i])
    except IndexError:
        print('linea inexistente\n')

print('**********************************************************')
print ('********* OPERACION realizada satisfactoriamente *********')
print('**********************************************************')
output = open("output.txt","w")
output.writelines(lineas)

output.close()
archivo.close()