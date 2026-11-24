#1
#1 2
#1 2 3
#1 2 3 4
#1 2 3 4 5

row = int(input('Enter Number of Rows:'))
for i in range(1,row+1):
    for j in range(1,i+1):
        print(j,end='')
        num+=1
    print()