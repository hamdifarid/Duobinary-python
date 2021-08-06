a = []
n = int(input("Enter number of elements : "))
for i in range(0, n):
    ele = int(input())
 
    a.append(ele)
val = [0]
emparra=[]
added=[]
print(a,"input")
for i in range(0,len(a)):
    emparra.append(val[i])
    val[i] = val[i]^a[i]
    val.append(val[i])
    if val[i]==0:
        val[i]=-1
    if emparra[i]==0:
        emparra[i]=-1
    if a[i]==0:
        a[i]=-1      
print(a,"Polar Input")
print(emparra,"second")
print(val,"exored(please ignore the last zero or one)")

for i in range(0,len(a)):
    a[i]=emparra[i]+val[i]
print(a,"added")

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

print(a,'decoded')
k=input("press close to exit") 
