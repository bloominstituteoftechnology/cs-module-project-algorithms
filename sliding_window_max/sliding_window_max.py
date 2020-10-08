'''
Input: a List of integers as well as an integer `k` representing the size of the sliding window
Returns: a List of integers
'''
def sliding_window_max(nums, k):
    # Your code here
    solution = []
    start = -1
    end = k-1
    for i in nums:
        start += 1
        end += 1
        #print(start, end)
        win = nums[start:end]
        if len(win) is 3:
            print(win)
            result = 0
            for x in win:
                if x >= result and len(win) is 3:
                    result = x  
            solution.append(result)
            print(result)
            print(solution)
    return solution


if __name__ == '__main__':
    # Use the main function here to test out your implementation 
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3

    print(f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}")
