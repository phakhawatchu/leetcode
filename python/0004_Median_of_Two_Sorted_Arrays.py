from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        arr = sorted([*nums1, *nums2])
        if len(arr)%2 == 0:
            return (arr[len(arr)//2] + arr[(len(arr)//2)-1]) / 2
        return arr[(len(arr)-1)//2]

if __name__ == '__main__':
    nums1 = [1,2]
    nums2 = [3,4]
    s = Solution()
    print(s.findMedianSortedArrays(nums1, nums2))