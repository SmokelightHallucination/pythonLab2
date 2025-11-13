def recursive_sum(n):
    if n == 1:
        return 1
    else:
        return n + recursive_sum(n - 1)


number = int(input("Введите число: "))
print("Сумма чисел от 1 до", number, "равна", recursive_sum(number))
