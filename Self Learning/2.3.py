# Calculate expression - Author: Christian Girling

# Input values for a, b, c
value_a = input('Please input a value for "a"')
value_b = input('Please input a value for "b"')
value_c = input('Please input a value for "c"')

# x = (a + b * c)/10
x_value = (float(value_a) + float(value_b) * float(value_c)) / 10

# Printing the value of x
print('Type of a is ', type(value_a))
print('x = ', x_value)