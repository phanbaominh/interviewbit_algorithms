# @param A : tuple of integers
# @return an integer
def maximumGap(A):
    maxA, minA, n = max(A), min(A), int(len(A))
    if n<2:
        return 0
    if n==2:
        return abs(A[0]-A[1])
    gap = ((maxA - minA) * 1.0) / (n-1)
    if (gap==0):
        return 0
    bucketmax = [-1] * (n - 1)
    bucketmin = [-1] * (n - 1)
    for i in range(n):
        index=int((A[i] - minA) / gap)
        if A[i] == maxA:
            index=n-2
        if A[i] > bucketmax[index]:
            bucketmax[index]  = A[i]
        if A[i] < bucketmin[index] or bucketmin[index]==-1:
            bucketmin[index] = A[i]
    res=0
    i=0
    j=1
    while j<n-1:
        while i<n-1 and bucketmax[i]==-1:
            i+=1
        j=i+1
        while j<n-1 and bucketmin[j]==-1:
            j+=1
        
        if j<n-1 and bucketmin[j]-bucketmax[i] > res:
            res = bucketmin[j]-bucketmax[i]
        i=j
    return res