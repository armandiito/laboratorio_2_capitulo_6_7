print('Only print code if all iterations completed')
num = int(input('introduce un numero para chequiar: '))
for i in range(0, 6):
    if i == num:
        break
    print(i, ' ', end='')
else:
    print()
    print('All iterations successful')
