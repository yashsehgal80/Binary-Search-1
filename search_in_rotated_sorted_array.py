class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if nums == None or len(nums) == 0:
            return -1

        n = len(nums)
        low = 0
        high = n - 1
        while low <= high:
            mid = low + (high-low) // 2
            if nums[mid] == target:
                return mid
            if nums[low] <= nums[mid]:
                if target >= nums[low] and target < nums[mid]:
                    high = mid - 1
                else:
                    low = mid + 1
            else:
                if target > nums[mid] and target <= nums[high]:
                    low = mid + 1
                else:
                    high = mid - 1
        
        return -1