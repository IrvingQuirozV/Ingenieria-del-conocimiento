24. Calcular e Imprimir una tabla de dos columnas que muestre, en la primera, los enteros del 1 al n y en la segunda a n2. No utilizar un numero mayor que 30 para N
num=[]
num1=[]
x = int(input("¿Cuántos números quieres menor que 30?\n"))
if x > 30:
    print("La cantidad debe ser menor que 30")
else:
    for i in range(x):
        if i%2==0:
            num.append(i)
            num1.append(i**2)
print(num)
print (num1)
