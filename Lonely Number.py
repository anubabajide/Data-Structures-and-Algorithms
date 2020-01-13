def lonely_number(numbers):
	#change list to set
	yes=set(numbers)
	# loop through all items in list
	for _ in range(len(numbers)):
		#remove first item 
		x=numbers.pop(0)
		#create a set without the removed item 
		no=set(numbers)
		#add removed item back to list
		numbers.append(x)
		
		#If there is a difference between the two sets, there is a lonely number
		if bool(yes.difference(no)) is True:
			return[list(yes.difference(no))[0]]
		
	#return null if there is no difference
	return []
