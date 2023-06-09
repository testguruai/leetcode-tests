class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        # https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes#Algorithm_complexity
        isPrime = [True] * n
        for i in range(2, n):
            if i * i >= n:
                break
            if not isPrime[i]:
                continue
            for j in range(i * i, n, i):
                isPrime[j] = False
        count = 0
        for i in range(2, n):
            if isPrime[i]:
                count += 1
        return count
