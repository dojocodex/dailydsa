def twoSumHashmap(nums, target):
    seen = {}
    for i in range(len(nums)):
        required = target - nums[i]
        if required in seen:
            return [seen[required], i]
        seen[nums[i]] = i

    return -1

print(twoSumHashmap([2,7,11,15], 9))