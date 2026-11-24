number = input('Enter Number to check: ')
int(number)
rev = number[::-1]
if number==rev:
    print('Number is Palindrome')
else:
    print('Number is Not Palindrome')