class Solution:
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return 0

        l = 0
        r = len(nums) - 1
        while r >= l:
            if r == l:
                return r
            mid = (r + l) // 2
            if nums[mid] > nums[mid+1]:
                r = mid
            else:
                l = mid + 1


Sol = Solution()
nums = [3, 2, 1, 3, 5, 6, 4]
result = Sol.findPeakElement(nums)
print(result)