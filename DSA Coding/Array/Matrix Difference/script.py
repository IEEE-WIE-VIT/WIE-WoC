r1 = int(input())
c1 = int(input())
M1 = []
M3 = []
for row_counter in range(r1):
    matrix_row = input().strip() + " "
    M_row = []
    temp = ''
    counter = 0
    column_counter = 0
    while column_counter < c1:
        if matrix_row[counter] != ' ':
            temp += matrix_row[counter]
        else:
            M_row.append(temp)
            temp = ''
            column_counter += 1
        counter += 1
    M1.append(M_row)
    M3.append(M_row)
r2 = int(input())
c2 = int(input())
M2 = []
for row_counter in range(r2):
    matrix_row = input().strip() + " "
    temp = ''
    counter = 0
    column_counter = 0
    while column_counter < c2:
        if matrix_row[counter] != ' ':
            temp += matrix_row[counter]
        else:
            M2.append(temp)
            temp = ''
            column_counter += 1
        counter += 1
for row_counter in range(r1):
        for column_counter in range(c1):
            if M1[row_counter][column_counter] in M2:
                M3[row_counter][column_counter] = '0'
for row_counter in range(r1):
    for column_counter in range(c1):
        print(M3[row_counter][column_counter], end=" ")
    print()

