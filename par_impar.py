# programa para verificar si un numero es par o impar

print("----------------------------------------")
print("-----------INGRESE UN NUMERO------------")
print("----------------------------------------")

# input
x = int(input("Digite un numero: "))

# processing
r = (x%2)
if r==0:
    msj="PAR"
else:
    msj="IMPAR"    

#output
print("----------------------------------------")
print("--------------RESULTADO-----------------")
print("----------------------------------------")

print("El numero " + str(x) + "es" + msj)