def RemoveElement(nums, val):
	lst = []
	for item in nums:
		if item != val:
			lst.append(item)


	nums = lst

	return len(nums)      # time Complexity O(n) and Space Complexity O(n)