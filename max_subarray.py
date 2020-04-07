def maxSubArrayNaive(nums):
    max_sum = max(nums)
    size = len(nums)
    idxs = [r for r in range(0, size)]
    sums = dict(zip(idxs, nums))
    for i in idxs:
        for j in idxs[:size-i]:
            if i != 0 and sums[j] > max_sum:
                max_sum = sums[j]
            if (j+i != size-1):
                sums[j] += nums[j+i+1]
    return max_sum


def maxSubArrayKadane(input):
    if len(input) == 0:
        return None
    maxSoFar = maxEndingHere = input[0]
    for idx, value in enumerate(input):
        if idx >= 1:
            maxEndingHere = max(value, maxEndingHere + value)
            if maxEndingHere > maxSoFar:
                maxSoFar = maxEndingHere
    return maxSoFar


input = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

print(maxSubArrayKadane(input))
