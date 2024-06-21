n = float(input("Uma distância em metros: "))
km = n / 1000
hm = n / 100
dam = n / 10
dm = n * 10
cm = n * 100
mm = n * 1000
cores = {'limpa': '\033[m',
         'azul': '\033[34m',
         'amarelo': '\033[33m',
         'pretoebranco': '\033[7;40m',
         'vermelho': '\033[31m',
         'verde': '\033[32m',
         'ciano': '\033[36m',
         'roxo': '\033[35m',}

bg = {'bvermelho': '\033[41m',
      'bverde': '\033[42m',
      'bamarelo': '\033[43m',
      'bazul': '\033[44m',
      'broxo': '\033[45m',}

print('{}A medida de {} corresponde a{}'.format(cores['pretoebranco'], n, cores['limpa']))
print('{}{}Km{}'.format(bg['bverde'], km, cores['limpa']))
print('{}{}hm{}'.format(bg['bverde'], hm, cores['limpa']))
print('{}{}dam{}'.format(bg['bverde'], dam, cores['limpa']))
print('{}{}dm{}'.format(bg['bverde'], dm, cores['limpa']))
print('{}{}cm{}'.format(bg['bverde'], cm, cores['limpa']))
print('{}{}mm{}'.format(bg['bverde'], mm, cores['limpa']))