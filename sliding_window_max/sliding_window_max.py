'''
Input: a List of integers as well as an integer `k` representing the size of the sliding window
Returns: a List of integers
'''


def sliding_window_max(nums, k):
    # Your code here

    # going to have an array of k-length
    point1 = 0
    point2 = k  # > can slice via nums[point1:point2]
    # will need point1 and point2 to increment by 1 in order to iterate
    # through nums
    # also need to make sure point2 stays in range

    # need placeholder for max_vals
    max_vals = []

    while point2 <= (len(nums)):
        # slice k-len array of nums
        # print("point2 before:", point2)
        x = nums[point1:point2]
        point1 += 1
        point2 += 1
        # print("x:", x)
        # print("point2 after:", point2)

        # now, need to find max value of x
        val = max(x)
        max_vals.append(val)

    return max_vals


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

    samp = [1, 3, -1, -3, 5, 3, 6, 7]
    print(sliding_window_max(samp, 3))  # > [3,3,5,5,6,7]
