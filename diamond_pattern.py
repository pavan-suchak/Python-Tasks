#    * 
#   * * 
#  * * * 
# * * * * 
#* * * * * 
# * * * * 
#  * * * 
#   * * 
#    *

row = int(input('Enter Number of Rows:'))

for i in range(1,row+1):
    for j in range(row-i):
        print(' ',end='') 

    for k in range(i):
        print('* ',end='')
    
    print()

for l in range(1,row):
    for m in range(l):
        print(' ',end='')

    for x in range(row-l):
        print('* ',end='')

    print()