# @param A : list of integers
# @return an integer
def nTriang(A):
    n=int(len(A))
    if n<=2:
        return 0
    c=0
    A.sort()
    for i in range(n-2):
        j=n-2
        k=n-1
        while j>=i:
            while j>i and A[i]+A[j]>A[k]:
                j-=1
            c+=k-j-1
            k-=1
            if (k==j):
                j-=1
    return c %((10**9)+7)
            
