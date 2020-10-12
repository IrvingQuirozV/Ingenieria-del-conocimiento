23. Introducir N enteros. Calcular e imprimir el producto de los números pares.
z=0
suma=0
num=[]

x = int(input("¿Cuántos números quieres?\n"))
while (z < x):
    y = int(input("Ingrese un número: "))
    num.append(y)
    if y%2==0:
        suma += y
    z+=1   
print(suma)
