def gaus_way_one(A):
    A_res = A[:]
    forbidden_col = []
    forbidden_rows = []
    n = len(A)
    print_martix(A)
    while n > 0:
        main = find_main(A,forbidden_rows, forbidden_col)[0]
        p = find_main(A, forbidden_rows, forbidden_col)[1]
        q = find_main(A, forbidden_rows, forbidden_col)[2]
        A = change_matrix(A, p, q, forbidden_rows, forbidden_col)
        print_martix(A)
        #A = cross_rows_cols(A, p, q)
        forbidden_rows.append(p)
        forbidden_col.append(q)
        n -= 1
    solutions = get_sol(A,forbidden_rows, forbidden_col)
    check(A, solutions)
    return solutions
def find_main(A, forbidden_rows, forbidden_col):
    n = len(A)
    row = 0
    column = 0
    max = abs(A[0][0])
    for p in range (n):
        for q in range(n):
            if p not in forbidden_rows and q not in forbidden_col:
                if abs(A[p][q]) > max:
                    max = abs(A[p][q])
                    row = p
                    column = q
    return (max, row, column)

def change_matrix(A, p, q, forbidden_rows, forbidden_col):
    n = len(A)
    m = []
    for i in range(n):
        if i != p and p not in forbidden_rows:
            m_i = - A[i][q] / A[p][q]
        else:
            m_i = 0
        m.append(m_i)
    for i in range(n):
        for j in range(n + 1):
            if i not in forbidden_rows and j not in forbidden_col:
                if i != p:
                    A[i][j] += A[p][j] * m[i]
    return A

def print_martix(A):
    print('this is matrix')
    for arr in A:
        print(arr)
    print('\n')

def cross_rows_cols(A, p, q):
    A_new = []
    for arr in A:
        arr.pop(q)
    for arr in A:
        if A.index(arr) != p:
            A_new.append(arr)
    return A_new

def copy_A(A):
    A_res = []
    for arr in A:
        A_res.append(arr)
    return A_res

def get_sol(A,forbidden_rows, forbidden_col ):
    n = len(A)
    solutions = []
    for t in range(n):
        solutions.append(0)
    while forbidden_rows:
        i = forbidden_rows[-1]
        j = forbidden_col[-1]
        sum = 0
        for k in range(n):
            sum += solutions[k] * A[i][k]
        sum = A[i][n] - sum
        x = sum / A[i][j]
        #solutions[j] = A[i][n] / A[i][j]
        forbidden_rows.pop(-1)
        forbidden_col.pop(-1)
        solutions[j] = x
    for i in range(n):
        solutions[i] = round(solutions[i], 6)
    print(solutions)
    return solutions

def check(A, solutions):
    n = len(A)
    result = []
    for i in range(n):
        sum = 0
        for j in range(n):
            sum += solutions[j] * A[i][j]
        sum -= A[i][n]
        result.append(sum)
    print(result)



