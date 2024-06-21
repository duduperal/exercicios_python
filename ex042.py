# Coleta os comprimentos das 3 retas
comp1 = float(input('Digite o comprimento da primeira reta: '))
comp2 = float(input('Digite o comprimento da segunda reta: '))
comp3 = float(input('Digite o comprimento da terceira reta: '))

# Verifica se as retas podem formar um triângulo
if comp1 < comp2 + comp3 and comp2 < comp1 + comp3 and comp3 < comp1 + comp2:
    print('As retas PODEM FORMAR um triângulo!')

    # Verifica se o triângulo formado é equilátero, isósceles, ou escaleno
    if comp1 == comp2 == comp3:
        print('E o triângulo formado pelas 3 retas é equilátero!')
    elif comp1 == comp2 or comp2 == comp3 or comp3 == comp1:
        print('E o triângulo formado pelas 3 retas é isósceles!')
    else:
        print('E o triângulo formado pelas 3 retas é escaleno!')
else:
    print('As retas NÃO PODEM FORMAR um triângulo')
