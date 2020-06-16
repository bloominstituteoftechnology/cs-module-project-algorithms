'''
Input: a List of integers as well as an integer `k` representing the size of the sliding window
Returns: a List of integers
'''


def sliding_window_max(nums, k):
    # Your code here
    max_numbers = []
    counter = 0

    while nums[counter:k + counter][k - 1] != nums[len(nums) - 1]:
        max_numbers.append(max(nums[counter:k + counter]))
        counter += 1

    max_numbers.append(max(nums[counter:k + counter]))

    return max_numbers


if __name__ == '__main__':
    # Use the main function here to test out your implementation 
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3

    print(f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}")
