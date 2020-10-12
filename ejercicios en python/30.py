30.  Convertir P libras inglesas a D dólares y C centavos. Usar el tipo de cambio $2.80 = 1 libra
p=2.80

x=int(input("Desea convertir sus libras a dolar(1) o a centavos(2)"))

if x == 1:
    d=float(input("¿Cuantas libras desea convertir a dólar?\n"))
    conversion = (d/p)
if x == 2:
    c=float(input("¿Cuantas libras desea convertir a centavos?\n"))
    conversion = c/100
print("El resultado es:")
print(float(conversion))
