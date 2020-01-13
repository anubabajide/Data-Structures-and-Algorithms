def intersection(nums1, nums2):
  nums1 = set(nums1)
  nums2 = set(nums2)
  
  print(nums1.intersection(nums2))
  return list(nums1.intersection(nums2))
