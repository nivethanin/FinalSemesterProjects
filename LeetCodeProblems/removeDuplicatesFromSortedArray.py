class Solution:

    def removeDuplicates(self, nums:list[int]) -> int:
        if not nums:
            return 0
        
        temp = 0

        for i in range(1, len(nums)):
            print(nums)
            if nums[temp] != nums[i]:
                temp +=1
                nums[temp] = nums[i]
            
            nums[i] = '_'
        
        return temp + 1



arr = [0,0,1,1,2,3,4,4,4,4,5]

g = Solution()
print(g.removeDuplicates(arr))
print(f"The final array: {arr}")