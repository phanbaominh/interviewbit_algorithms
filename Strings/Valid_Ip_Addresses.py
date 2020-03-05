def duyetTrau(A,pos,c,res):
    n=int(len(A))
    tmp=A
    if (c==3):
        num=int(tmp[pos:int(len(tmp))],10)
        if (num!=0 and tmp[pos]=='0'):
            return
        if (num==0 and pos!=len(tmp)-1):
            return
        if (num>=0 and num<=255):
            res.append(tmp[:])
        return

    for i in range(pos,n-1):
        num=int(tmp[pos:i+1],10)
        if (num>=0 and num<=255):
            tmp=tmp[:i+1]+'.'+tmp[i+1:]
            duyetTrau(tmp,i+2,c+1,res)
            if tmp[pos]=='0':
                break
            tmp=A

# @param A : string
# @return a list of strings
def restoreIpAddresses(A):
    res=[]
    duyetTrau(A,0,0,res)
    return res
