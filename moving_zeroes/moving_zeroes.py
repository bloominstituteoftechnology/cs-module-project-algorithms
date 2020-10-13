'''
Input: a List of integers
Returns: a List of integers
'''
def moving_zeroes(arr):
    # Your code here
    altered = [number for number in arr if number != 0]
    zero = [number for number in arr if number is 0]
    altered.extend(zero)
    return altered

print(moving_zeroes([0, 3, 1, 0, -2]))    


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")