a = []
n = int(input("Enter number of elements : "))
for i in range(0, n):
    ele = int(input())
    a.append(ele)


added=[]
final=[]
print(a,"input")
for i in range(0,len(a)):
    if a[i]==0:
        a[i]=-1

meh=a.copy()
a.insert(0,-1)
a.pop(len(a)-1)
print(meh,"Polar Input")
print(a,'shifted')
for i in range(0,len(a)):
    meh[i]=meh[i]+a[i]

print(meh,'final output')    
k=input("press close to exit") 
