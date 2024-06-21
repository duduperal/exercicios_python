t = str(input('Digite uma frase: ')).upper().strip()
print('A letra A aparece {} vezes'.format(t.count('A')))
print('A letra A aparece pela primeira vez na posição {}'.format(t.find('A') + 1))
print('A letra A aparece pela última vez na posição {}'.format(t.rfind('A') + 1))