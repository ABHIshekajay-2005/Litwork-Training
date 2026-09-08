""" The dynamic factorial of a positive integer n is obtained by
applying a dynamic sequence of operations, where the operations change based on
the parity (even or odd) of the current number:


For even numbers, the operations alternate between
multiplication * and division /. For odd numbers, the operations alternate
between addition + and subtraction -. The numbers are processed in decreasing
order, starting from n. Division uses floor division, rounding down to the
nearest integer.


Your task is to implement a function that calculates the
dynamic factorial of a given positive integer n.


The operation priority is
"/","*","+","-".


Constraints: If the input is a single number,
consider all values from the given number down to 1.


For example: Input: 6


Consider: 6 5 4 3 2 1


If the input contains two values separated by a space,
consider all values from the first number down to the second number.


For example: Input: 6 4


Consider: 6 5 4


Sample Example-1: Input: 5


Output: 4


Explanation: The sequence is computed as(5 to 1):
dynamic = 5 + (4 / 3) - (2 * 1).


Steps - 1: 5+1-2 Steps - 2: 4


Sample Example-2: Input: 6 4


Output: 5


Explanation: The sequence is computed as(6 to 4):
dynamic = (6 / 5) + 4


Steps - 1: 1 + 4 Steps - 2: 5 """



# code ---

n=list(map(int,input().strip().split()))
odd=0
even=0
res=[]
if len(n)==1:
    t=n[0]
    while t>0:
        res.append(t)
        if t%2==0:
            if even%2==0:
                res.append("//")
            else:
                res.append("*")
            even+=1
        else:
            if odd%2==0:
                res.append("+")
            else:
                res.append("-")
            odd+=1
        t-=1

else:
    for i in range(n[0],n[1]-1,-1):
        res.append(i)
        if i%2==0:
            if even%2==0:
                res.append("//")
            else:
                res.append("*")
        else:
            if odd%2==0:
                res.append("+")
            else:
                res.append("-")

res=res[:len(res)-1]
print(res)
s="".join(str(i) for i in res)
print(eval(s))