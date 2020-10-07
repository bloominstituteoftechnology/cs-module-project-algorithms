'''
Input: a List of integers as well as an integer `k` representing the size of the sliding window
Returns: a List of integers
'''
def sliding_window_max(nums, k):
    # Your code here
    result = []

    for i in range(len(nums)):
        greatest_num = None

        if i + k > len(nums):
            break

        for j in range(i, i + k):
            if greatest_num is None:
                greatest_num = nums[j]
            elif nums[j] > greatest_num:
                greatest_num = nums[j]

        result.append(greatest_num)

    return result


if __name__ == '__main__':
    # Use the main function here to test out your implementation 
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3

    print(f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}")
