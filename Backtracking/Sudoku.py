def solve(A,B,C,row,col):
    table = (row // 3) + (col // 3) * 3 
    table_num = (row % 3) * 3 + (col % 3)
    if row == 9:
        return True
    if A[row][col] != '.':
        if col < 8:
            check = solve(A,B,C,row,col + 1)
        else:
            check = solve(A,B,C,row + 1,0)
        if check:
            return True
    else:
        for j in range(1,10):
            i = str(j)
            if (i not in A[row]) and (i not in B[col]) and (i not in C[table]):
                #print(i,row,col,table,table_num)
                A[row][col] = i
                B[col][row] = i
                C[table][table_num] = i
                if col < 8:
                    check = solve(A,B,C,row,col + 1)
                else:
                    check = solve(A,B,C,row + 1,0)
                if check:
                    return True
                A[row][col] = B[col][row] = C[table][table_num] = '.'
    return False
# @param A : list of list of chars
# @return nothing
def solveSudoku(A):
    B = []
    C = []
    for i in range(9):
        column = []
        for j in range(9):
            column.append(A[j][i])
        B.append(column[:])
    for s in range(3):
        for i in range(3):
            table = []
            for j in range(i*3,i*3 + 3):
                for k in range(s*3,s*3+3):
                    table.append(A[j][k])
            C.append(table[:])
    #print(A)
    solve(A,B,C,0,0)