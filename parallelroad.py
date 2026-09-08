n1=int(input())
n2=int(input())

a=[]
b=[]
for i in range(n1):
    a.append(int(input()))

for i in range(n2):
    b.append(int(input()))

a.extend(b)
a=list(set(a))
a.sort()

if len(a)%2==0:
    i=len(a)//2
    j=len(a)//2-1
    print(((a[i]+a[j]))/2)
else:
    print(a[len(a)//2])

