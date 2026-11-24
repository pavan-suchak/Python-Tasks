#       1
#      1 1
#     1 2 1
#    1 3 3 1
#   1 4 6 4 1
# 1 5 10 10 5 1

row = int(input('Enter Number of Row:'))
temp=1
for i in range(1,row+1):
    for k in range(row-i):
        print(' ',end='')
    print(f'{temp } ',end='')
    for j in range(1,i):
        temp=temp*(i-j)
        temp=temp//j
        print(f'{temp} ',end='')
    print()