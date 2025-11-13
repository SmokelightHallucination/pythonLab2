import subprocess
import os

hiddenNumber = int(input("Игрок 1, загадай число: "))

def clear_console():
    subprocess.call('clear' if os.name == 'posix' else 'cls', shell=True)

clear_console()

def guess(hiddenNumber):
    guessedNumber = int(input("Игрок 2, попробуй отгадать: "))
    while hiddenNumber != guessedNumber:
        if hiddenNumber < guessedNumber:
            print("Игрок 2, твоё число больше, чем загаданное")
        else:
            print("Игрок 2, твоё число меньше, чем загаданное")
        guessedNumber = int(input("Попробуй ещё раз: "))
    print("Поздравляю! Ты угадал число!")

guess(hiddenNumber)
