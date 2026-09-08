""" Joseph is learning digital logic subject which will be for his next semester. He usually tries to solve unit
assignment problems before the lecture. Today he got one tricky question. The problem statement is “A
positive integer has been given as an input. Convert decimal value to binary representation. Toggle all bits of
it after the most significant bit including the most significant bit. Print the positive integer value after toggling
all bits”.
Constraints :
1<=N<=100
Example 1:
Input :
10 
Output :
5   """

# code ----


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
