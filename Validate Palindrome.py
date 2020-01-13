def is_palindrome(s):
  l = list(s.lower())
  x = list(s.lower())
  for i in l: 
    if i == ' ':
      l.remove(' ')
      x.remove(' ')
  for i in range((len(l)/2)):
    temp = l[i]
    l[i] = l[-(i+1)]
    l[-(i+1)] = temp

  print (x)
  print (l)
  if x == l:
    return True
  else:
    return False