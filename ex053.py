frase = str(input('Digite uma frase qualquer: ')).replace(' ', '').upper()  
frase_invertida = frase[::-1]
tot = 0
print('O inverso de {} é {}'.format(frase, frase_invertida))
if frase_invertida == frase:
    print('Temos um palíndromo!')
else:
    print('Não é palíndromo!')

'''
for i in range(0, len(frase)):
    if frase_invertida[i] == frase[i]:
        tot += 1
if tot == len(frase):
    print('É palíndromo')
else:
    print('Não é palíndromo')
'''



