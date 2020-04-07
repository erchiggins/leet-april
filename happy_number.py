from collections import defaultdict

class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        seen = set()
        happy = False
        if n < 0:
            n = -n
        while not happy:
            next_val = 0
            digits = [int(x) for x in str(n)]
            for d in digits:
                next_val += d*d
            if next_val == 1:
                happy = True
            elif next_val in seen:
                break
            else:
                seen.add(next_val)
                n = next_val
        return happy
            
