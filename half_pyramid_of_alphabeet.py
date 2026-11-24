#A
#B B
#C C C
#D D D D
#E E E E E

row = int(input('Enter Number of Rows:'))
num = 65
for i in range(1,row+1):
    for j in range(i):
        print(chr(num),end='')
    num+=1
    print()