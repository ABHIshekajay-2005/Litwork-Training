s=input()
l=list(map(int,s))

for i in range(len(l)):
    if l[i]!=l.count(i):
        print(0)
        print("Not a Autobiographical number")
        exit()

print(len(set(l)))
print("Autobiographical number")