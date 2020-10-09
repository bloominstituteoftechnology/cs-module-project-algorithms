'''
Input: a List of integers as well as an integer `k` representing the size of the sliding window
Returns: a List of integers
'''
def sliding_window_max(arr, k):
    max = 0
    x = []
    for i in range(len(arr) - k + 1): 
        max = arr[i]
        for j in range(1, k):
            if arr[i + j] > max:
                max = arr[i + j]
        x.append(max)
        
    return x

# Driver method
if __name__ == '__main__':
    # Use the main function here to test out your implementation 
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3

    print(f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}")