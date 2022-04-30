names = ['Christian', 'DJ', 'Natalia', 'Hannah']
print(names[0:3])
names[0] = 'Paige'
print(names[0])

numbers = [3, 5, 8, 2, 1, 12, 9, 10]
max = numbers[0]
for number in numbers:
    if number > max:
        max = number
print(max)