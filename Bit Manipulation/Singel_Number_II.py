# @param A : tuple of integers
# @return an integer
def singleNumber(A):
    count=[]
    for i in range(32):
        count.append(0)
    n=int(len(A))
    for i in range(n):
        tmp=A[i]
        c=0
        while tmp>0:
            count[c]+=(tmp+1)%2
            tmp=tmp>>1
            c+=1
    num=0
    for i in range(32):
        if count[i]%3!=0:
            num=num+2**i
    return num
    