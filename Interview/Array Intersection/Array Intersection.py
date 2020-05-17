def intersection(nums1, nums2):
  #Make one array a set
  nums1 = set(nums1)
  result=[]

  #check for presence of second array in set 
  for i in nums2:
  	if i in nums1:
  		result.append(i)
  
  return result