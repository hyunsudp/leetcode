class Solution(object):
    def smallestNumber(self, n, t):
        """
        :type n: int
        :type t: int
        :rtype: int
        """
        while True:
            digits = list(map(int, str(n)))
            product = digits[0]
            for i in range(1, len(digits)):
                product *= digits[i]
            if product % t == 0:
                return n
            n += 1