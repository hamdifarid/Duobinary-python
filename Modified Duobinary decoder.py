a = []
n = int(input("Enter number of elements : "))
for i in range(0, n):
    ele = int(input())
    a.append(ele)


added=[]
final=[]
print(a,"input")
for i in range(0,len(a)):
    if a[i]==-2:
        a[i]=-1
    if a[i]==2:
        a[i]=-1
    if a[i]==0:
        a[i]=1
print(a)
for i in range(0,len(a)):
    if a[i]==-1:
        a[i]=0

print(a)
k=input("press close to exit") 
