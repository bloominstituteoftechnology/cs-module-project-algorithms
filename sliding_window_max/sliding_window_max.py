'''
Input: a List of integers as well as an integer `k` representing the size of the sliding window
Returns: a List of integers
'''
def sliding_window_max(nums, k):

    # Your code here
    #print(f'LIST: {nums}')
    #print(f'SIZE OF WINDOW: {k}')

    #incrementing variable
    i = 0

    max_list = []
    # simplest case: 
    #print(len(nums))
    while k+i <= len(nums):
        # grab the first k numbers from nums
        window_list = nums[i:k+i]
        #print(window_list)
        # call the max of the list and return the one max value
        max_value = max(window_list)
        #print(f'MAX: {max_value}')

        # append that max value to a new list
        
        max_list.append(max_value)
        #print(f'MAXLIST: {max_list}')

        # move the window over one item until the right edge of the window hits the max length of nums
        ## This is a while loop
        #increment i
        i += 1
    return max_list


if __name__ == '__main__':
    # Use the main function here to test out your implementation 
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3

    print(f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}")
