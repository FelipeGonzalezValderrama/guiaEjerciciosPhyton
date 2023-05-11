
rut = input("Ingrese su RUT (sin puntos, ni guiones, sin DV): ")

serie = list(range(2,8))*2

#print(serie)

rut = rut[::-1]

suma = 0

for i in range(len(rut)):
    producto = int(rut[i]) * serie [i]
    suma = suma + producto
    ## sum += int(rut[i]) * serie [i]

#print(suma)
modulo11 = suma % 11
#print(modulo11)

dv = 11 - modulo11

if dv == 10:
    dv = "K"
elif dv == 11:
    dv = 0

print(f"Su dígito verificador es {dv}")



