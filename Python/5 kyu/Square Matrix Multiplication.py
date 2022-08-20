"""Square Matrix Multiplication"""


def matrix_mult(n, m):
    lst1 = []
    lst2 = []
    for i in range(len(n)):
        for j in range(len(m[0])):
            sums = 0
            for k in range(len(m)):
                sums=sums+(n[i][k]*m[k][j])
            lst1.append(sums)
        lst2.append(lst1)
        lst1 = []
    return lst2