def three_sum_hashset(nums):
    nums.sort()
    n = len(nums)
    result = set()

    for i in range(n):
        # skip duplicates for the first number
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        target = -nums[i]
        seen = set()
        
        for j in range(i + 1, n):
            complement = target - nums[j]

            if complement in seen:
                result.add(tuple(sorted([nums[i], complement, nums[j]])))

                # skip duplicates for nums[j]
                while j + 1 < n and nums[j] == nums[j + 1]:
                    j += 1
            seen.add(nums[j])
    
    return list(result)


# Example
print(three_sum_hashset([-1,0,1,2,-1,-4]))
# Output (order may vary):
# [[-1, -1, 2], [-1, 0, 1]]
