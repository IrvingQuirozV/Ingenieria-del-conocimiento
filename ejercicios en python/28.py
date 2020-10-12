28. Calcular la suma de las raíces cuadradas de los números impares que hay entre 1 y 1000
suma=0

print("Imprimir potencia de números impares entre 1 y 1000")

for i in range(1001):
    if i%2!=0:
        suma += i**2
    
print(suma)
