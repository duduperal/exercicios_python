from emoji import emojize
from time import sleep
print('{:=^40}'.format('CONTAGEM REGRESSIVA'))
for c in range(10, -1, -1):
    print(c)
    sleep(1)
print(emojize
('''
  🎆🎆
🎆\033[1;4;31mBOOM\033[m🎆
  🎆🎆
'''))
#print('\033[1;4;31mBOOM\033[m')