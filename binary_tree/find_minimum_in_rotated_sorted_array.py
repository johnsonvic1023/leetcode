class Solution:
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        if len(nums) == 1:
            return nums[0]

        left = 0
        right = len(nums) - 1

        # sorted array, e.g. 1 < 2 < 3
        if nums[right] > nums[0]:
            return nums[0]

        while right >= left:
            mid = left + (right - left) // 2

            if nums[mid - 1] > nums[mid]:
                return nums[mid]

            if nums[mid] > nums[mid + 1]:
                return nums[mid + 1]

            if nums[mid] > nums[0]:
                left = mid + 1
            else:
                right = mid - 1


Sol = Solution()
nums = [2, 1]
result = Sol.findMin(nums)
print(result)