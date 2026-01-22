#Largest Element in Array
class Solution:
    def largest(self, arr):
        maxi = arr[0]
        for i in arr:
            if i >= maxi:
                maxi = max(maxi,i)
        print (maxi)
        return maxi    

arr=[7,6,5]
print(Solution().largest(arr))

## Input arr=[7,6,5]
## Output 7

#Test push 01152026




