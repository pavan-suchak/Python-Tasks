# 1
# 2 3
# 4 5 6
# 7 8 9 10

row = int(input('Enter Number of Rows:'))
num=1
for i in range(1,row+1):
    for j in range(i):
        print(f'{num} ',end='')
        num+=1
    print()