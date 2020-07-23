# FIRST-PASS:
def sliding_window_max(nums, k):
    '''
    Input: a List of integers as well as an integer `k` representing the size of the sliding window
    Returns: a List of integers
    '''
    # Your code here

    output_arr_size = len(nums) - (len(nums) - k - 1)
    print("num of max_vals", output_arr_size)

    # going to have an array of k-length
    point1 = 0
    point2 = k  # > can slice via nums[point1:point2]
    # will need point1 and point2 to increment by 1 in order to iterate
    # through nums
    # also need to make sure point2 stays in range

    # need placeholder for max_vals
    max_vals = []

    while point2 <= (len(nums)): #> O(n)

        # slice k-len array of nums
        # print("point2 before:", point2)
        x = nums[point1:point2] #> O(k) for slicing
        point1 += 1
        point2 += 1
        # print("x:", x)
        # print("point2 after:", point2)

        # now, need to find max value of x
        val = max(x)
        max_vals.append(val) #> O(1)

    return max_vals

# if k == 2:
    # output_arr len is len(arr) - 1

# if k == 3:
    # output_arr len is len(arr) - 2

# if k == 4:
    # output_arr len is len(arr) - 3

# if k == 5:
    # output_arr len is len(arr) - 4

# By this logic, if I know the len(arr) and know k,
# can always know the size of the output_arr

# If I know size of output_arr, then I also know how many 
# max values to retrieve

# len(nums) - k - 1


if __name__ == '__main__':
    # # Use the main function here to test out your implementation
    # arr = [1, 3, -1, -3, 5, 3, 6, 7]
    # k = 3

    # print(f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}")

    # ## Example
    # ```
    # Sample Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
    # Expected Output: [3,3,5,5,6,7]
    # Explanation:

    # Window position                Max
    # ---------------               -----
    # [1  3  -1] -3  5  3  6  7       3
    # 1 [3  -1  -3] 5  3  6  7       3
    # 1  3 [-1  -3  5] 3  6  7       5
    # 1  3  -1 [-3  5  3] 6  7       5
    # 1  3  -1  -3 [5  3  6] 7       6
    # 1  3  -1  -3  5 [3  6  7]      7
    # ```

    my_list = [5, 10, 15, 20]
    # breakpoint()
    # print(sliding_window_max(my_list, 3))

    samp = [x for x in range(0,10)]
    print(samp)
    print("Samp size:", len(samp))
    x = sliding_window_max(samp, 5) #> observing that when k is 3, output arr is always -2 its orig len
    print(x)  # > [3,3,5,5,6,7]
    print("Output array size:", len(x))

