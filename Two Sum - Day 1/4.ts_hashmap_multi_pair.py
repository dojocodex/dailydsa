def twoSumHashmap(nums, target):
    seen = {}
    s = set()
    for i in range(len(nums)):
        required = target - nums[i]
        if required in seen:
            # return [seen[required], i]
            s.add((min(seen[required], i), max(seen[required], i)))
        seen[nums[i]] = i

    return s

print(twoSumHashmap([2,7,11,15,8,1], 9))