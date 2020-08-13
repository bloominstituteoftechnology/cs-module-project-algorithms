'''
Input: a List of integers as well as an integer `k` representing the size of the sliding window
Returns: a List of integers
'''
def sliding_window_max(nums, k):
    # Your code here
    sums = []
    i = 0
    while i < len(nums):
        endex = i+k
        try: 
            window = nums[i:endex]
            print(window)
            if len(window) < k:
                break
            max_of_window = max(window)
            sums.append(max_of_window)
            i += 1

        except IndexError: i += 1

    return sums


if __name__ == '__main__':
    # Use the main function here to test out your implementation 
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3

    print(f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}")
