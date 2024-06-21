primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão da PA: '))
cont = 1
termo = primeiro
mais = 10
total = 0
while mais != 0:
    total += mais
    while cont <= total:
        print(termo, end=' ')
        termo += razao
        cont += 1
    print('PAUSA')
    mais = int(input('Quantos termos a mais você gostaria de ver? [Digite 0 para finalizar]: '))
print('Progressão finalizada!')
