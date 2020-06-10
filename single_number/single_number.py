'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''
def single_number(arr):
	# Your code here
	first = []
	second = []

	for i in range(0, len(arr)):
		if arr[i] in first:
			second.append(arr[i])
		else:
			first.append(arr[i])

	return (list(set(first) - set(second)))[0] # returns in 0.015s


if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")
