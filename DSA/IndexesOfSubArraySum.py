#Given an array arr[] containing only non-negative integers, your task is to find a continuous subarray (a contiguous sequence of elements) 
#whose sum equals a specified value target. You need to return the 1-based indices of the leftmost and rightmost elements of this subarray. 
#You need to find the first subarray whose sum is equal to the target.
#Note: If no such array is possible then, return [-1].

#Input: arr[] = [1, 2, 3, 7, 5], target = 12
#Output: [2, 4]
#Explanation: The sum of elements from 2nd to 4th position is 12.

class Solution:
	def subArraySum(self,a,k): 
		n = len(a)
		start = 0
		curr_sum = 0

		for end in range(n): 
			curr_sum += a[end]
		
			#shrink the window while sum is too large
			while curr_sum > k and start <= end:
				curr_sum -= a[start]
				start += 1
	
			if curr_sum == k and start <= end:
				return [start + 1, end + 1]

		return [-1]

# ---- RUN TEST ----
sol = Solution()
a = [1, 2, 3, 7, 5]
k = 12
print(sol.subArraySum(a, k))