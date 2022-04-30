# Weight conversion calculator
weight = input("Enter Weight:")
conversion = input('lbs or kgs?')
if conversion == 'lbs':
    weight =  int(weight) / 2.2
    print(f'You weigh {int(weight)} kgs')
elif conversion == 'kgs':
    weight = int(weight) * 2.2
    print(f'You weigh {int(weight)} lbs')
else:
    print('Please enter either "kgs" or "lbs"')

