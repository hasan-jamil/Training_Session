def MergeSortedArray(num1, m, num2, n):
	final_array = []
	for i in range(m):
		value = num1[i]
		final_array.append(value)

	for i in range(n):
		value = num2[i]
		final_array.append(value)

	final_array = sorted(final_array)
	num1 = final_array  
	return num1        # time Complexity O(m + n) and Space Complexity O(m + n)
