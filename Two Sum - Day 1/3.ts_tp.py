def two_sum_sorted(nums, target):
  
  l, r = 0, len(nums) - 1
  while l < r:
    s = nums[l] + nums[r]
    if s == target:
      return [l+1, r+1]
    if s < target:
      l += 1
    else:
      r -= 1
  return None


arr = [1, 2, 3, 4, 6]
t = 6
print(two_sum_sorted(arr, t))  # (1, 3) because 2 + 4 == 6
