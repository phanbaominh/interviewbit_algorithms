def recursive(x,n,d):
    if n==1:
        return x
    if n%2==0:
        res=recursive(x,n/2,d)%d
        return (res*res)%d
    else:
        res=recursive(x,n/2,d)%d
        return (res*res*(x%d))%d
# @param x : integer
# @param n : integer
# @param d : integer
# @return an integer
def pow(x, n, d):
    if (x==0):
        return 0
    if (n==0):
        return 1
    res=recursive(x,n,d)
    if res<0:
        return d+res
    else:
        return res