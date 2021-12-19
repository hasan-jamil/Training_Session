def FirstDuplicateValue(array):
	lst = []
	for i , value in enumerate(array):
		item = array[i]
		p = item in lst
		if p == True:
			return item 
		lst.append(item)


	return -1    # time compexity O(n) and Space Complexity O(n)