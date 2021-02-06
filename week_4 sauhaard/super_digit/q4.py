a,b=list(map(int,input().split()))
c=""
for i in range (0,b):
    c=c+str(a)+""
c=int(c)
k=c
while (k//10)>0:
    sum=0
    while c>0:
        sum=sum+(c%10)
        c=c//10
    k=sum
    c=sum
print(k)
