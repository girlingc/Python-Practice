for x in range(4):
    for y in range(4):
        print(f'({x}, {y})')

numbers = [2, 2, 2, 2, 7]
for x_count in numbers:
    output = ''
    for count in range(x_count):
        output += 'x'
    print(output)