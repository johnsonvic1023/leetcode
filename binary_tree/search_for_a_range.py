class Solution:
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        start = -1
        end = -1

        if len(nums) == 1:
            return [0, 0] if target == nums[0] else [-1, -1]

        # start point
        left = 0
        right = len(nums) - 1
        while right >= left:
            mid = left + (right - left) // 2
            if (mid == 0 or target > nums[mid-1]) and target == nums[mid]:
                start = mid
                break
            elif target > nums[mid]:
                left = mid + 1
            else:
                right = mid - 1

        # start point
        left = 0
        right = len(nums) - 1
        while right >= left:
            mid = left + (right - left) // 2
            if (mid == len(nums) - 1 or target < nums[mid+1]) and target == nums[mid]:
                end = mid
                break
            elif target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1

        return [start, end]


Sol = Solution()
nums = [8,8,8,8]
target = 8
result = Sol.searchRange(nums, target)
print(result)