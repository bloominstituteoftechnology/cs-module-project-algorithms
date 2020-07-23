'''
Input: a List of integers as well as an integer `k` representing the size of the sliding window
Returns: a List of integers
'''


def sliding_window_max(array, k):
    startWindowIndex = 0
    endWindowIndex = k
    holder = []

    for _ in array:
        window = array[startWindowIndex:endWindowIndex]
        max_value = max(window)
        holder.append(max_value)

        # continously move window to right until we reach the end
        if endWindowIndex < len(array):
            startWindowIndex += 1
            endWindowIndex += 1
        else:
            return holder
    return holder




if __name__ == '__main__':
    # Use the main function here to test out your implementation 
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3

    print(f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}")
