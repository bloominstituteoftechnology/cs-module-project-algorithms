'''
Input: a List of integers as well as an integer `k` representing the size of the sliding window
Returns: a List of integers
'''
import time
start = time.time()
def sliding_window_max(nums, k):
    start = 0
    end = k
    result = [0] * (len(nums) - k + 1)
    while end <= len(nums):
        result[start] = max(nums[start:end])
        start += 1
        end += 1

    return result

# TODO currently checking every number need to come up with something better 

if __name__ == '__main__':
    # Use the main function here to test out your implementation 
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3



    print(f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}")

end = time.time()
print(f"{end - start:.21f}")
