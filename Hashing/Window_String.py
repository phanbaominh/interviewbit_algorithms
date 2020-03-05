def minWindow(A, B):
    count = {}
    table = {}
    for w in B:
        if count.get(w) == None:
            count[w] = 1
            table[w] = 0
        else:
            count[w] += 1
    j = 0
    nw = int(len(B))

    while j < len(A) and table.get(A[j]) == None:
            j += 1

    if j >= len(A):
        return ""
    i = j + 1
    cw =1
    minlen = (2**31) - 1
    s = -1
    table[A[j]] += 1

    while i < len(A) or cw == nw:
        if i < len(A) and table.get(A[i]) >= 0:
            if table[A[i]] < count[A[i]]:
                cw += 1
            table[A[i]] += 1
            
        while cw == nw:
            if i >= len(A):
                e = len(A) - 1
            else:
                e = i

            if e - j + 1 < minlen:
                minlen = i - j + 1
                s = j
            table[A[j]] -= 1

            if table[A[j]] < count[A[j]]:
                cw -= 1
            j += 1

            while j < len(A) and table.get(A[j]) == None:
                j += 1
        i += 1

    if s == -1:
        return ""
    return A[s:s+minlen]
                
                