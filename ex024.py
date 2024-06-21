cid = str(input('Nome da sua cidade: ')).strip()
divido = cid.split()
tem = 'SANTO' in divido[0].upper()
print(tem)
'''
    ///Deixando mais bonito\\\

if 'santo' in divido[0].lower():
    print('EXISTE!')
else:
    print('NÃO EXISTE!')
    
'''