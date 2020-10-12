25.  mostrar las potencias 4tas de los números del 1 al 5
suma=0
num=[]

print("Imprimir potencias cuartas de los pares menores a 50 ")

for i in range(51):
    if i%2==0:
        num.append(i**4)
    
print(num)
