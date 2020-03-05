def recursive(A):
    if A == 1:
        return [[0], [1]]
    G = recursive(A-1)
    res = []
    for i in range(0,2):
        G.reverse()
        for j in range(int(len(G))):
            tmp = G[j][:]
            tmp.insert(0,i)
            res.append(tmp)
    return res
# @param A : integer
# @return a list of integers
def grayCode(A):
    res = recursive(A)
    decres = []
    for bina in res:
        output = 0
        for ele in bina:
            output = (output << 1) | ele
        decres.append(output)
    return decres