'''
Input: a List of integers as well as an integer `k` representing the size of the sliding window
Returns: a List of integers
'''
def sliding_window_max(nums, k):
    # Your code here
    # first pass solution

    # loop thru nums
    # loop in range of k
    # pick the big one and append it
    new_list = []
    limit = len(nums) - k
    for i, value in enumerate(nums):
        if i > limit: break
        # print(i, value)
        max = value
        for j in range(k):
            if max < nums[i+j]:
                max =  nums[i+j]
        new_list.append(max)
    return new_list


if __name__ == '__main__':
    # Use the main function here to test out your implementation 
    # arr = [1,2,3,4,5]
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3

    print(f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}")
