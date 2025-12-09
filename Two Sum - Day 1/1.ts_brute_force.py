def two_sum_bf(nums, target):
  n = len(nums)
  
  for i in range(n):
    for j in range(i+1, n):
        if nums[i] + nums[j] == target:
            return [i, j]
  
ans = two_sum_bf([2,7,11,15], 9)
print(ans)