class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:

        count = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[count] = nums[i]
                count = count+1

        return count, nums


arr = [1,2,3,5,4,65,3]
s = Solution()
print(s.removeElement(arr, 3))
