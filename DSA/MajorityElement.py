# MajorityElement

class Solution:
    def majorityElement(self, arr):
        #code here
        #Search for the element and store the number of time found in the count
        candidate = None 
        count = 0 
        # Step 1: Find potential candidate 
        for num in arr: 
            if count == 0: 
                candidate = num 
            if num == candidate: 
                count += 1 
            else: 
                count -= 1 
                
        # Step 2: Verify candidate 
        if arr.count(candidate) > len(arr) // 2: 
            return candidate 
        return -1
            

 # ------------------------
 # Testing
sol = Solution()
arr = [1,2,1]
print(sol.majorityElement(arr))