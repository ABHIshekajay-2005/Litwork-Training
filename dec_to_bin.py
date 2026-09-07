n=int(input())

bs=""
t=n
while t>0:
    bs=str(t%2)+bs
    t//=2
print(bs)

bs=bs.replace("0","x")
bs=bs.replace("1","0")
bs=bs.replace("x","1")


print(int(bs,2))
