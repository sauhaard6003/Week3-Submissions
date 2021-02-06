def divisible(a,b):
    if a%b==0:
        return 0
    else:
        return(b-(a%b))
l=int(input())
for t in range (0,l):
    k,m=list(map(int,input().split()))
    print(divisible(k,m))
        
