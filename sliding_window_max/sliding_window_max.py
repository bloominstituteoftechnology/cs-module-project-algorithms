'''
Input: a List of integers as well as an integer `k` representing the size of the sliding window
Returns: a List of integers
'''
def sliding_window_max(nums, k):
    array_length = len(nums)
    new_array = []
    
    max_value = [0 for i in range(array_length)]

    other_value = []
    other_value.append(0)
    
    for i in range(1,array_length):
        while (len(other_value) > 0 and nums[other_value[-1]] < nums[i]):
            max_value[nums[-1]] = array_length - 1
            del other_value[-1]
        
        other_value.append(i)
        
    while (len(other_value) > 0):
        max_value[other_value[-1]] = array_length - 1
        del other_value[-1]

    another_value = 0
    
    for i in range(array_length - k +1):

        while (another_value < i or max_value[another_value] < i + k - 1):

            another_value += 1
            new_array.append(nums[another_value])
        

    return new_array


if __name__ == '__main__':
    # Use the main function here to test out your implementation 
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3

    print(f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}")
