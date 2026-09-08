"""  Two parallel roads separated by a river are connected from cities A and B to an outer ring road. Both roads
have a high flow of traffic throughout the day. People who want to travel from city A to city B or vice versa
have to pass through the ring road which is a huge waste of time and money. To ease the traffic and also to
make it convenient for commuters to travel from city A to city B and vice versa, the construction of a bridge
over the river is planned.
The surveillance team submitted a report stating the bridge should be constructed in the following manner:
 The ground or soil is stronger at certain points on the road favorable for the construction of the
bridge.
 The strong ground positions are given from the starting point of each road. Say, the road of city A has
strong ground at 1,4 meaning there is a strong ground at a distance of 1 unit, another strong ground
point at a distance of 4 units from the starting point of the road of city A.
Collate the strong ground positions of both roads. Sort them in ascending order. Calculate the middle point or
median of the combined strong ground positions. The bridge should be constructed from road A as per the
middle point calculated. Given the number of strong positions on roads A and B(N1 and N2 respectively) and
the strong ground positions on each road, the task here is to calculate the midpoint of the combined strong
positions on both roads.
NOTE: When the strong positions are combined, the repeated positions on the different roads are dropped.
Example 1:
Input:
3 -> Value of N1
3 -> Value of N2
{3,5,2} -> a[ ], Elements a[0]to a[N1-1], where each input element is separated by new line
{1,2,3} -> b[ ], Elements b[0]to b[N2-1), where each input element is separated by new line
Output: 2.5
Example 2:
Input:
2 -> Value of N1
3 -> Value of N2
{2,3} -> all, Elements a[O]to a[N1-1), where each input element is separated by new line
{5,6,4} -> b[ ], Elements b[O]to b[N2-1], where each input element is separated by new line  """


# code -----


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

