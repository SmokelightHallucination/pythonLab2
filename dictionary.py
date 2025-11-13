n = int(input("Введите размер словаря квадратов: "))
squares = []
integers = []

for i in range(1, n+1):
    integers.append(i)

for i in range(1, n+1):
    squares.append(pow(i,2))

squares_dictionary = {integer: square for integer, square in zip(integers, squares) }

print(squares_dictionary)