# @param A : list of integers
# @param B : integer
# @return an integer
def threeSumClosest(A, B):
    if len(A)==3:
        return sum(A)
    A.sort()
    int_max=2**32-1
    min1=1000000000

    for i in range(int(len(A)-2)):
        j=i+1
        k=i+2
        v=A[i]+A[j]+A[k]

        if abs(v-B)<abs(min1-B):
            min1=v
            if min1==B:
                    return min1

        while True:
            tmp2=tmp3=int_max
            if j<k-1:
                tmp2=abs(A[i]+A[j+1]+A[k]-B)
            if k<len(A)-1:
                tmp3=abs(A[i]+A[j]+A[k+1]-B)
            if tmp2==tmp3 and tmp2==int_max:
                break
            if tmp2<=tmp3:
                j+=1
            elif tmp3<=tmp2:
                k+=1
            v=A[i]+A[j]+A[k]
            if abs(v-B)<abs(min1-B):
                min1=v
                if min1==B:
                    return min1
        
        
        
    return min1
            