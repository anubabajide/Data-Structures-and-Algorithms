def reverse_string(str1):
  l = list(str1)
  seperator = ''
  for i in range((len(l)/2)):
    temp = l[i]
    l[i] = l[-(i+1)]
    l[-(i+1)] = temp
  str1 = seperator.join(l)
  print (str1)
  return str1