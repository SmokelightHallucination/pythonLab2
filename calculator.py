def addition(a, b):
    return a + b

def subtraction(a, b):
    return a - b

def multiplication(a, b):
    return a * b

def division(a, b):
    return a / b

def remainder(a, b):
    return a % b


def choice(num):
    switch = {
        '1': addition,
        '2': subtraction,
        '3': multiplication,
        '4': division,
        '5': remainder,
    }
    return switch.get(num)

number1 = float(input("Введите первое число: "))
number2 = float(input("Введите второе число: "))

print("Выберите операцию (введите её номер):")
print("1. Сложение")
print("2. Вычитание")
print("3. Умножение")
print("4. Деление")
print("5. Остаток от деления")

op = input("Ваш выбор: ")

operation = choice(op)

if operation is None:
    print("Ошибка: неверный выбор операции!")
else:
    try:
        result = operation(number1, number2)
        print("Результат:", result)
    except ZeroDivisionError:
        print("Ошибка: деление на ноль!")
