def merge(nums1, nums2,m=3, n=3):
  i, j = m-1, m+n-1

  while len(nums2) > 0 and i >= 0:
    if nums1[i] < nums2[-1]:
      nums1[j] = nums2.pop()
    else:
      nums1[j] = nums1[i]
      i -= 1
    j -= 1

  if nums2:
    nums1[:len(nums2)] = nums2

  return nums1
print(merge([1, 2, 3, 0, 0, 0], [2, 5, 6]))
(())