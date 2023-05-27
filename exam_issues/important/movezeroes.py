nums = [0,1,0,3,12]
cnt = 0
for i in range(len(nums)):
    if nums[i] == 0:
        cnt += 1
    else:
        nums[i-cnt], nums[i] = nums[i], nums[i-cnt]
    
print(nums)