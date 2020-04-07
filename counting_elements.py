from collections import defaultdict

class Solution(object):
    def countElements(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        count = 0
        lookup = defaultdict(int)
        for i in arr:
            lookup[i] += 1
        for j in arr:
            if lookup[j+1] != 0:
                count += 1
        return count