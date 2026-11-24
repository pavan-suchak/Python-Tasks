# * * * * * * * * *
#  * * * * * * *
#    * * * * *
#      * * *
#        *

row = int(input('Enter Number of Rows:'))
for i in range(0,row):
    for j in range(i*2):
        print(' ',end='')
    
    for j in range(row-i-1):
        print('* ',end='')

    for k in range(row-i):
        print('* ',end='')
        
    print()