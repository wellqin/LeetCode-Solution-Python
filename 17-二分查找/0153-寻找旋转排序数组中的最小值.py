# 153. 寻找旋转排序数组中的最小值
# 假设按照升序排序的数组在预先未知的某个点上进行了旋转。
# ( 例如，数组 [0,1,2,4,5,6,7] 可能变为 [4,5,6,7,0,1,2] )。
# 请找出其中最小的元素。
# 你可以假设数组中不存在重复元素。

from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        size = len(nums)
        if size == 0:
            raise Exception('程序出错')
        if size == 1:
            return nums[0]
        left = 0
        right = size - 1
        while left < right:
            # mid = left + (right - left) // 2
            mid = (left + right) >> 1
            # [7, 8, 1, 2, 3, 4, 5, 6]
            if nums[mid] > nums[right]:
                # [3, 4, 5, 6, 7, 8, 1, 2]
                # 此时 mid 肯定不是最小元素
                left = mid + 1
            else:
                # mid 有可能是最小元素，所以，不能排除它
                assert nums[mid] < nums[right]
                right = mid
        # 一定存在最小元素，因此无需再做判断
        return nums[left]
