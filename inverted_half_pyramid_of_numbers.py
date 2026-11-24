#1 2 3 4 5
#1 2 3 4
#1 2 3
#1 2
#1

row = int(input('Enter Number of Rows:'))
for i in range(row,0,-1):
    num=1
    for j in range(i):
        print(num,end='')
        num+=1
    print()