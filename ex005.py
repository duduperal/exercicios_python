num = int(input("Digite um número: "))
cores = {'limpa': '\033[m',
         'vermelho': '\033[31m',
         'verde': '\033[32m',
         'amarelo': '\033[33m',
         'azul': '\033[34m',
         'roxo': '\033[35m',
         'ciano': '\033[36m',
         'cinza': '\033[37m', }
print("Analisando o número {}{}{} o seu antecessor é {}{}{} e o seu sucessor é {}{}{}"
      .format(cores['vermelho'], num, cores['limpa'], cores['verde'], num - 1, cores['limpa'], cores['roxo'],
              num + 1, cores['limpa']))
