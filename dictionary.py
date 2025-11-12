# dictionary{}
# for i in range(2, 100):

n = int(input("Введите размер словоря квадратов: "))
squares = [n]
integers = [n]

for i in range(1, n+1):
    integers.append(i)

print(integers)

for i in range(1, n+1):
    squares.append(pow(i,2))

# squares_dictionary = {integers: for i in range(101), }