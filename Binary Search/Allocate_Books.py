def findStudents(A,v):
    sum1=0
    count=0
    for i in range(int(len(A))):
        if sum1+A[i]>v:
            count+=1
            sum1=A[i]
        else:
            sum1+=A[i]
    return count
# @param A : list of integers
# @param B : integer
# @return an integer
def books(A, B):
    s=max(A)
    e=sum(A)
    if (int(len(A))<B):
        return -1
    elif (int(len(A))==B):
        return s
    while s<e:
        mid=(s+e)/2
        num=findStudents(A,mid)
        if (num<B):
            e=mid
        else:
            s=mid+1
    return e
                