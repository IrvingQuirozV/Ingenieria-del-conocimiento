31. Convertir P libras inglesas, S chelines y E peniques D dólares y C centavos. (1 libra  20 = chelines; 1 chelin = 12 peniques)
p=int(input("cuantas libras, chelines y peniques desea convertir a dolar y centavos\n"))

s=p*20
e=s*12
d=p/2.80
c=d/100
ds=s/2.80
cs=ds/100
de=e/2.80
ce=de/100

print("libras a dolar: ", + d)
print("libras a centavos de dolar", + c)
print("chelines a dolar ", + ds)
print("chelines a centavos de dolar", + cs)
print("peniques a dolar", + de)
print("peniques a centavos de dolar", +ce)
