class Duration:
    def __init__(self,v,k):
        self.v=v
        self.k=k
# @param arrive : list of integers
# @param depart : list of integers
# @param K : integer
# @return a boolean
def hotel(arrive, depart, K):
    dur=[]
    N=int(len(arrive))
    if N==1 and K==0:
        return False
    for i in range(N):
        dur.append(Duration(arrive[i],1))
        dur.append(Duration(depart[i],-1))
    dur.sort(key=lambda x:x.v)
    sum1=0
    i=0
    while i<N*2:
        val=dur[i].v
        while i<N*2 and dur[i].v==val:
            sum1+=dur[i].k
            i+=1
        if sum1>K:
            return False
    return True