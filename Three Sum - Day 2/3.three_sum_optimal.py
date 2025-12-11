def three_sum(nums):
    nums.sort()
    n = len(nums)
    result = []

    for i in range(n):
        # Skip same element to avoid duplicate triplets
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        left, right = i + 1, n - 1
        target = -nums[i]

        while left < right:
            curr_sum = nums[left] + nums[right]

            if curr_sum == target:
                result.append([nums[i], nums[left], nums[right]])

                # Skip duplicates on the left
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                # Skip duplicates on the right
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1

                left += 1
                right -= 1

            elif curr_sum < target:
                left += 1
            else:
                right -= 1

    return result


# Example
print(three_sum([-1,0,1,2,-1,-4]))
# Output:
# [[-1, -1, 2], [-1, 0, 1]]
