def arr(nums):
    flag=1
    d=[]
    for j in range (0,len(nums)):
        if nums[j]==target:
            d.append(j)
            flag=0
            break
    for j in range (len(nums)-1,-1,-1):
        if nums[j]==target:
            d.append(j)
            flag=0
            break
    if flag==1:
        return [-1,-1]
    else:
        return d
print(arr(nums))
