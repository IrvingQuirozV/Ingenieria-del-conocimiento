27. Encontrar la suma de los cuadrados de los enteros del 1 al N. Es decir su programa calculará: 1^2 + 2^2 + 3^2 + N^2
z=0
suma=0
num=[]

x = int(input("¿Cuántos números quieres?\n"))
while (z < x):
    y = int(input("Ingrese un número: "))
    num.append(y)
    suma += (y**2)
    z+=1   
print(suma)
