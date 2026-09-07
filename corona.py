n=int(input())
l=list(map(int,input().split()))
sp=int(input())

res=[]

for i in range(n):
    bi=""
    t=l[i]

    while t>0:
        bi=str(t%2)+bi
        t//=2

    bi=bi[0:len(bi)-sp]

    if not bi:
        res.append(0)
    else:
        res.append(int(bi,2))

print(*res)