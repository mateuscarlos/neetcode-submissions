class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2
        total = len(nums1) + len(nums2)
        half = total // 2

        if len(B) < len(A):
            A, B = B, A

        start, end = 0, len(A) - 1

        while True:
            i = (start + end) // 2 #A
            j = half - i - 2 #B

            Astart = A[i] if i >= 0 else float("-infinity")
            Aend = A[i + 1] if (i + 1) < len(A) else float("infinity")
            Bstart = B[j] if j >= 0 else float("-infinity")
            Bend = B[j + 1] if (j + 1) < len(B) else float("infinity")

            #partition is correct
            if Astart <= Bend and Bstart <= Aend:
                #odd
                if total % 2:
                    return min(Aend, Bend)
                #even
                return (max(Astart, Bstart) + min(Aend, Bend)) / 2
            elif Astart > Bend:
                end = i -1
            else:
                start = i + 1