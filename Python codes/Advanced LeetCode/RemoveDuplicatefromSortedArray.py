nums = [1,1,2]
x = 1
for i in range(len(nums)-1):
    if(nums[i]!=nums[i+1]):
        nums[x] = nums[i+1]
        print(nums[x])
        x = x +1
print(x)
print(nums)