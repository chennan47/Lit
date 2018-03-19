#MERGESORT
def merge_sort(A):
    merge_sort_util(A, 0, len(A)-1)


def merge_sort_util(A, first, last):
    if first < last:
        middle = (first + last) // 2
        merge_sort_util(A, first, middle)
        merge_sort_util(A, middle+1, last)
        merge(A, first, middle, last)


def merge(A, first, middle, last):
    L = A[first:middle]
    R = A[middle:last+1]
    i = j = 0
    for k in range(first, last+1):
        if L[i] <= R[j]:
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1


# 88. Merge Sorted Array

# Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.
#
# Note:
# You may assume that nums1 has enough space (size that is greater or equal to m + n) to hold additional elements
# from nums2. The number of elements initialized in nums1 and nums2 are m and n respectively.


def merge(self, nums1, m, nums2, n):
    while m > 0 and n > 0:
        if nums1[m - 1] >= nums2[n - 1]:
            nums1[m + n - 1] = nums1[m - 1]
            m -= 1
        else:
            nums1[m + n - 1] = nums2[n - 1]
            n -= 1
    if n > 0:
        nums1[:n] = nums2[:n]


def find_kth_smallest(self, nums1, nums2, k):
    m, n = len(nums1), len(nums2)
    if m > n:
        return self.find_kth_smallest(nums2, nums1, k)

    if not nums1:
        return nums2[k - 1]
    if k == 1:
        return min(nums1[0], nums2[0])

    i = min(k / 2, m)
    j = min(k / 2, n)
    if nums1[i - 1] > nums2[j - 1]:
        return self.find_kth_smallest(nums1, nums2[j:], k - j)
    else:
        return self.find_kth_smallest(nums1[i:], nums2, k - i)