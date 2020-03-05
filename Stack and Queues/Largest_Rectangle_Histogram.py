# @param A : list of integers
# @return an integer
def largestRectangleArea(A):
    stack = []
    value = []
    n = int(len(A))
    max1=0
    for i in range(n+1):
        #print(stack,value,max1)
        if i<n and (len(value) == 0 or A[i]>A[value[-1]]):
            stack.append(i)
            value.append(i)
        else:
            while len(value)>0 and (i>=n or A[i]<A[value[-1]]):
                S = (i - stack.pop())*A[value.pop()]
                if S > max1:
                    max1 = S
            if len(value)==0:
                add = 0
            else:
                add = value[-1] + 1
            stack.append(add)
            value.append(i)
    return max1
                        