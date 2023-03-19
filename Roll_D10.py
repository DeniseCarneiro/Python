#Roll D10 Dices

import random 
from time import sleep

print('Roll D10s')

D10 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print('Settings')
success = int(input('From which number is a sucess?  ')) 
r10 = int(input('10 is 2 success?\n1-Yes\n2-No\n '))
r1 = int(input('Does result 1 cancel 1 success?\n1-Yes\n2-No\n '))

repeat = 1

while repeat ==1:
    q_dices = int(input('How many dices?  '))
    qSuccess = 0
    qFlaws = 0

    print('-'*50)
    print(f'Random results for {q_dices} D10:')

    while q_dices>0:
        result = random.choice(D10)
        print(result)
        q_dices = q_dices -1
        if result>= success:
            qSuccess = qSuccess + 1
        if result == 10 and r10 == 1:
            qSuccess += 1
        if result == 1:
            qFlaws +=1
    if r1 == 1:
        print(f'Original amount of successes: {qSuccess}')
        print(f'Amount of flaws: {qFlaws}')
        qSuccess = qSuccess - qFlaws

    print(f'Amount of Success: {qSuccess}')

    print('-'*50)

    sleep(5)

    repeat = int(input('\n\nTo roll more dice, type 1.\nTo exit, type any other number.\n'))


