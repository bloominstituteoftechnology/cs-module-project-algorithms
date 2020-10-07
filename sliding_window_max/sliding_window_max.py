'''
Input: a List of integers as well as an integer `k` representing the size of the sliding window
Returns: a List of integers
'''
def sliding_window_max(nums, k):
    # Your code here

    left_index = 0
    right_index = 2
    maxx = []

    while nums[left_index] == 0 and nums[right_index] == 2:s
        maxx.append(max(nums[left_index : right_index]))
        left_index += 1
        right_index += 1

    


if __name__ == '__main__':
    # Use the main function here to test out your implementation 
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3

    print(f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}")
