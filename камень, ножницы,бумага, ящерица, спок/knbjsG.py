import sys
import random
import time

print('КАМЕНЬ, НОЖНИЦЫ, БУМАГА, ЯЩЕРИЦА, СПОК')

# В этих переменных накапливается количество
# побед, поражений и ничьих

wins = 0
losses = 0
ties = 0

while True:  # Главный цикл игры
    print('%s побед, %s поражений, %s ничьих' % (wins, losses, ties))

    while True:  # цикл выбора хода
        print('Выберете ход: (к)амень, (н)ожницы, (б)умага, (я)щерица, (с)пок или (в)ыход')
        playerMove = input(':')
        if playerMove == 'в':
            sys.exit()  # выход из программы

        if playerMove == 'к' or playerMove == 'н' or playerMove == 'б' or playerMove == 'я' or playerMove == 'с':
            break
        print('Введите "к", "н", "б", "я","с" или "в".')

    #  Отображение выбора пользователя

    if playerMove == 'к':
        print('КАМЕНЬ и ...')
    elif playerMove == 'н':
        print('НОЖНИЦЫ и ...')
    elif playerMove == 'б':
        print('БУМАГА и ...')
    elif playerMove == 'я':
        print('ЯЩЕРИЦА и ...')
    elif playerMove == 'с':
        print('СПОК и ...')

    time.sleep(2)  # сон в три секунды

    # Отображение выбора компьютера

    randomNumber = random.randint(1, 5)
    if randomNumber == 1:
        computerMove = 'к'
        print('КАМЕНЬ')
    elif randomNumber == 2:
        computerMove = 'н'
        print('НОЖНИЦЫ')
    elif randomNumber == 3:
        computerMove = 'б'
        print('БУМАГА')
    elif randomNumber == 4:
        computerMove = 'я'
        print('ЯЩЕРИЦА')
    elif randomNumber == 5:
        computerMove = 'с'
        print('СПОК')

    # Отображение и учет результатов

    if playerMove == computerMove:
        print('Ничья!')
        ties += 1
    elif playerMove == 'к' and computerMove == 'н':
        print('Победа!')
        wins += 1
    elif playerMove == 'к' and computerMove == 'я':
        print('Победа!')
        wins += 1
    elif playerMove == 'н' and computerMove == 'б':
        print('Победа!')
        wins += 1
    elif playerMove == 'н' and computerMove == 'я':
        print('Победа!')
        wins += 1
    elif playerMove == 'б' and computerMove == 'к':
        print('Победа!')
        wins += 1
    elif playerMove == 'б' and computerMove == 'с':
        print('Победа!')
        wins += 1
    elif playerMove == 'я' and computerMove == 'с':
        print('Победа!')
        wins += 1
    elif playerMove == 'я' and computerMove == 'б':
        print('Победа!')
        wins += 1
    elif playerMove == 'с' and computerMove == 'к':
        print('Победа!')
        wins += 1
    elif playerMove == 'с' and computerMove == 'н':
        print('Победа!')
        wins += 1
    elif playerMove == 'б' and computerMove == 'н':
        print('Поражение!')
        losses += 1
    elif playerMove == 'б' and computerMove == 'я':
        print('Поражение!')
        losses += 1
    elif playerMove == 'н' and computerMove == 'к':
        print('Поражение!')
        losses += 1
    elif playerMove == 'н' and computerMove == 'с':
        print('Поражение!')
        losses += 1
    elif playerMove == 'к' and computerMove == 'б':
        print('Поражение!')
        losses += 1
    elif playerMove == 'к' and computerMove == 'с':
        print('Поражение!')
        losses += 1
    elif playerMove == 'я' and computerMove == 'н':
        print('Поражение!')
        losses += 1
    elif playerMove == 'я' and computerMove == 'к':
        print('Поражение!')
        losses += 1
    elif playerMove == 'с' and computerMove == 'б':
        print('Поражение!')
        losses += 1
    elif playerMove == 'с' and computerMove == 'я':
        print('Поражение!')
        losses += 1