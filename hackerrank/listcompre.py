x = int(input())
y = int(input())
z = int(input())
n = int(input())
a=[]
i=0
j=0
k=0
for i in range(0,x):
    for j in range(0,y):
        for k in range(0,z):
            while i+j+k!=n:
               a.append(i)
               a.append(j)
               a.append(k)
            print(a)