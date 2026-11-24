row = int(input('Enter Number of Rows:'))
col = int(input('Enter Number of Columns:'))

row2 = int(input('Enter Number of Rows:'))
col2 = int(input('Enter Number of Columns:'))

if col != row2:
    print('No. of Row in 1st maxtix musb be same of no. of cols in matrix 2')
else:
    matr = []
    matr2 = []

    print('Enter Value For Matrix 1:')

    for i in range(row):
        row_one = []
        for j in range(col):
            row_one.append(int(input()))
        matr.append(row_one)

    print('Enter Value For Matrix 2:')

    for k in range(row2):
        row_two=[]
        for l in range(col2):
            row_two.append(int(input()))
        matr2.append(row_two)

    multiple = [[0 for _ in range(col)] for _ in range(row)]

    for a in range(row):
        for b in range(col):
            for c in range(col):
                multiple[a][b] += matr[a][c]*matr2[c][b] 

print('Multiplication')
for m in multiple:
    print(m)