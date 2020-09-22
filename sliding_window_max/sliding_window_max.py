'''
Input: a List of integers as well as an integer `k` representing the size of the sliding window
Returns: a List of integers
'''


def sliding_window_max(nums, k):
    # Create an empty array to house the answers
    answer = []
    # Loop once for each item in the array minus the window size + 1
    for each in range(len(nums) - k + 1):
        # Create a subArray that functions as the window.
        # This subarray takes its values from the main array, with the [each:(k+each)] designating which values are included
        subArray = nums[each:(k + each)]
        # Append the largest number in the subArray to the answer list
        answer.append(max(subArray))
    # Return the answer list after all loops have run
    return answer

# def sliding_window_max(nums, k):
#     counter = 0
#     copy = nums[counter:]
#     answer = []
#     while len(copy) > k:
#         sliding_window_max((copy[counter:]), (k + counter))
#         subArray = nums[counter:(k + counter)]
#         answer.append(max(subArray))
#         counter += 1
#     return answer


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3

    print(
        f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}")
