'''
Input: a List of integers as well as an integer `k` representing the size of the sliding window
Returns: a List of integers
'''
def sliding_window_max(nums, k):
    start = 0
    max_arr = []
    max_numb = 0
    counter = 0
    end = True
    temp = k

    while end:
        for item in nums[start:k]:
            if counter == 0:
                max_numb = item
            if item > max_numb:
                max_numb = item
                # print("max number:", max_numb)
            # print(item)

            counter += 1
            if counter == temp:
                max_arr.append(max_numb)
                # print("length of max_arr", len(max_arr))
                counter = 0
                start += 1
                k += 1
                max_numb = 0
                # print()
            if len(nums[start:k]) < temp:
                end = False

    return max_arr


if __name__ == '__main__':
    # Use the main function here to test out your implementation 
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3

    print(f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}")
