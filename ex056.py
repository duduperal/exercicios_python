tot_idade = 0
media = 0
idade_homem_mais_velho = 0
nome_homem_mais_velho = ''
tot_mul = 0
for i in range(1, 5):
    print('----- {}ª PESSOA -----'.format(i))
    nome = str(input('Digite o nome: ')).strip().title()
    idade = int(input('Digite a idade: '))
    sexo = str(input('Digite o sexo (M/F): ')).strip().upper()
    tot_idade += idade
    if idade > idade_homem_mais_velho and sexo == 'M':
        idade_homem_mais_velho = idade
        nome_homem_mais_velho = nome
    if sexo == 'F' and idade < 20:
        tot_mul += 1

nome_homem_mais_velho = nome_homem_mais_velho.title()
media = tot_idade / 4
print('-=' * 20)
print('A média de idade do grupo é igual a: {:.2f} anos'.format(media))
print('O nome do homem mais velho é {} com {} anos!'.format(nome_homem_mais_velho, idade_homem_mais_velho))
if tot_mul == 1:
    print('E existe apenas 1 mulher com menos de 20 anos!')
else:
    print('E existem {} mulheres com menos de 20 anos!'.format(tot_mul))