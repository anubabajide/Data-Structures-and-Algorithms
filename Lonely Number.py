def lonely_number(numbers):
  yes=set(numbers)
  for i in numbers:
    numbers2=numbers
    numbers2.remove(i)
    no=set(numbers)
    if bool(yes.difference(no)) is True:
    	maybe=list(yes.difference(no))
    	print(maybe)
    	return maybe[0]
  return [] 