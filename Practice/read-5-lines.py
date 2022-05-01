file_name = input('Please enter the file name: ')
try:
    file_hand = open(file_name)
except:
    print('File can not be opened')
    exit()
count = 0
for line_to_read in file_hand:
    if count < 5:
        print(line_to_read.upper())
        count += 1
    else:
        exit()