A,B=list(map(int,input().split()))
if (A**B)>=((10**9)+7):
    print ((A**B)%((10**9)+7))
else:
    print(A**B)
