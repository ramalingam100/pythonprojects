# Given an array arr[] of integers, calculate the median.

#Option 1:
class Solution:
    def findMedian(self, arr):
        #code here.

        arr.sort()
        n = len(arr)
    
        if (n & 1) == 0:
            return (arr[n//2]+arr[n//2-1])//2
        else:
            return arr[n//2]

#Option 2:
import statistics
class Solution:
    def findMedian(self,v):
        median_value = statistics.median(v)

        return(int(median_value))

 # ------------------------
 # Testing
sol = Solution()
arr = [1,2]
print(sol.findMedian(arr))
