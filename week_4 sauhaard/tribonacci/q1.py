def tribonacci(a):
    if a==1:
        return 0
    if a==2:
        return 0
    if a==3:
        return 1
    else:
        return (tribonacci(a-1)+tribonacci(a-2)+tribonacci(a-3))
x=int(input())
for i in range (0,x):
    print(tribonacci(int(input())))
    
