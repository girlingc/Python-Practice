# Refia Elif Emiroglu A01084126 Week 3
# one example of a conditional,
# a while loop, a for loop - out of the videos.
# conditional examples functions

""" Conditional to check the language"""
language = "python"

if language == 'python':
    print('Lang is py')
elif language == 'java':
    print('Lang is java')
else:
    print('no match')

""" Conditional to check the user"""
user = 'Admin'
logged_in = True

if user == 'Admin' and logged_in:
    print('Admin Page')
else:
    print('Bad Creds')



""" for Loop to go trhough a list of numbers"""
""" iterates through a certain number of values"""
nums = [1, 2, 3, 4, 5]
for num in nums:
    if num == 3:
        # print('Found the number!')
        continue
    print(num)


""" while loop for incrementing x by 1"""
""" while loop iterates until a certain condition is met"""
print('while loop ')
x = 0
while x <10:
    if x == 5:
        continue
    print(x)
    x +=1