valores=[]
for i in range(10):
    valor=int(input(f"ingrese el valor {i+1}: "))
    valores.append(valor)
    continue
print(valores)
promedioValores=sum(valores)/len(valores)
ordenAsc=sorted(valores)
ordenDesc=sorted(valores, reverse=True)
print(promedioValores)
print(ordenAsc)
print(ordenDesc)