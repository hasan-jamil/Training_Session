def longestPeak(array):
	longestPeaklength = 0
	i = 1
	while i < (len(array) - 1):
		peak = array[i] > array[i - 1] and array[i] > array[i + 1]
		if not peak:
			i += 1
			continue

		left = i - 2
		while left >= 0 and array[left] < array[left + 1]:      
			left -= 1

		right = i + 2
		while right < len(array) and array[right] < array[right - 1]:
			right += 1

		currentPeakLength = right - left - 1
		longestPeaklength = max(longestPeaklength, currentPeakLength)
		i = right

	return longestPeaklength   # time complexity O(n) and space complexity O(1)
