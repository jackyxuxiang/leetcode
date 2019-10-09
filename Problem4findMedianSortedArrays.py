from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        len1 = len(nums1)
        len2 = len(nums2)

        if (len1+len2)%2 == 0:
            leftval = self.findKth(nums1,nums2,(len1+len2)//2)
            rightval = self.findKth(nums1,nums2,(len1+len2)//2+1)
            return (leftval+rightval)/2
        else:
            return self.findKth(nums1,nums2,(len1+len2)//2+1)

    def findKth(self,nums1: List[int], nums2: List[int],k):

        len1 = len(nums1)
        len2 = len(nums2)

        low  = max(0,k-len2)
        high = min(len1,k)

        while low<=high:
            mid1 = (low + high) // 2   #
            mid2 = k-mid1
            right1 = mid1 + 1
            right2 = mid2 + 1

            if(mid1 != 0 and right2<=len2 and nums1[mid1-1]>nums2[right2-1]):
                high = mid1-1
            elif mid2!=0 and right1<=len1 and nums2[mid2-1]>nums1[right1-1]:
                low = mid1+1
            else:
                if mid1 == 0:
                    return nums2[mid2-1]
                elif mid2 == 0:
                    return nums1[mid1-1]
                else:
                    return max(nums1[mid1-1],nums2[mid2-1])
        return 0

if __name__ == '__main__':
    nums1 = [1,3,5,7]
    nums2 = [2,4]
    k= 4

    a= Solution().findKth(nums1,nums2,k)
    print(5)
    b= Solution().findMedianSortedArrays(nums1,nums2)
    print(b)