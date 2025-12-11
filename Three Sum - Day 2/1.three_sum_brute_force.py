def three_sum_bruteforce(nums):
    """
    Return list of unique triplets [a,b,c] such that a+b+c == 0.
    Brute-force: check all triples i<j<k.
    """
    n = len(nums)
    found = set()  # store tuples (a,b,c) sorted to dedupe
    for i in range(n-2):
        for j in range(i+1, n-1):
            for k in range(j+1, n):
                if nums[i] + nums[j] + nums[k] == 0:
                    trip = tuple(sorted((nums[i], nums[j], nums[k])))
                    found.add(trip)
    # convert to list of lists
    return [list(t) for t in found]


# quick demo
if __name__ == "__main__":
    arr = [-1, 0, 1, 2, -1, -4]
    print(three_sum_bruteforce(arr))
    # possible output (order may vary):
    # [[-1, -1, 2], [-1, 0, 1]]
