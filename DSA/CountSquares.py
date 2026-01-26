# Given a positive integer n, find the number of perfect squares that are less than n in the sample space of perfect squares.
# The sample space consists of all perfect squares starting from 1 (i.e., 1, 4, 9, 16, 25, …)

import math
class Solution:
    def countSquares(self, n):
        # code here 
        # Assign
        # Logic
        # For Loop/ While loop
        # Run the code
        # Brute Force
        # Iterate through the positive integer n.
        if n <= 1:
            return 0
        return int(math.sqrt(n - 1))
        


# ---- RUN TEST ----
sol = Solution()
n = 10
print(sol.countSquares(n))