'''
Input: a List of integers as well as an integer `k` representing the size of the sliding window
Returns: a List of integers
'''
def sliding_window_max(nums, k):
	# Your code here
	win = []
	small = [0] * k
	for i in range(0, len(nums) - k + 1):
		small = nums[i:i + k]
		win.append(max(small))

	return win # returns small in 0.000s, but large in 21.67s which is too slow

if __name__ == '__main__':
	# Use the main function here to test out your implementation
	arr = [1, 3, -1, -3, 5, 3, 6, 7]
	k = 3

	print(f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}")
