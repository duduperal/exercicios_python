# Pega o peso da pessoa e a altura
peso = float(input('Qual o seu peso: (Kg) '))
altura = float(input('Qual a sua altura: (m) '))

# Calcula o IMC
imc = peso / (altura ** 2)
print('O IMC dessa pessoa é de {:.1f}'.format(imc))

# Checa o IMC da pessoa de acordo com a tabela
if imc < 18.5:
    print('Abaixo do peso')
elif imc < 25:
    print('Peso ideal')
elif imc < 30:
    print('Sobrepeso')
elif imc < 40:
    print('Obesidade')
else:
    print('Obesidade mórbida')
    