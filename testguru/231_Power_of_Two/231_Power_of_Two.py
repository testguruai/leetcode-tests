class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n < 0:
            return False
        bin_str = bin(n)
        return sum([int(x) for x in list(bin_str[2:])]) == 1