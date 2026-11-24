#* * * * *
#* * * *
#* * *
#* *
#*

row = int(input('Enter Number of Rows:'))
for i in range(row,0,-1):
    for j in range(i):
        print('*',end='')
    print()