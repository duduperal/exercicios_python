comp1 = float(input('Comprimento da primeira reta: '))
comp2 = float(input('Comprimento da segunda reta: '))
comp3 = float(input('Comprimento da terceira reta: '))

if comp1 < comp2 + comp3 and comp2 < comp1 + comp3 and comp3 < comp1 + comp2:
    print('As 3 retas PODEM FORMAR um triângulo!!')
else:
    print('As 3 retas NÃO PODEM FORMAR um triângulo!!')
