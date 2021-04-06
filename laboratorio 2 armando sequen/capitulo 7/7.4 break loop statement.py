print("solo imprima el codigo si se completaron todas las iteraciones.")
num=int(input("ingrese un numero: "))

for i in range(0,6):
    if i==num:
        break
    print(i, " ", end="")
    
print("Done")