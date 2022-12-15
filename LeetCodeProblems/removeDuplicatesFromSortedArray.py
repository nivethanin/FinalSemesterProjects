class Solution:

    # def removeDuplicates(self, nums:list[int]) -> int:
    #     temp = -101

    #     i=0
    #     while nums[i]:
    #         print(i)
    #         if nums[i] == temp:
    #             nums.pop(i)
    #         else:
    #             temp = nums[i]
            
    #         i+=1
    
    #     return len(nums), nums

    def removeDuplicates(self, nums:list[int]) -> int:
        nums = set(nums)
        return len(nums), nums

    

arr = [0,0,1,1,2,3,4,4,4,4,5]

g = Solution()
print(g.removeDuplicates(arr[:]))
print(f"The final array: {arr}")