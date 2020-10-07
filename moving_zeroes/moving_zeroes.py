'''
Input: a List of integers
Returns: a List of integers
Write a function that takes an array of integers and moves each non-zero integer to the left side of the array, 
then returns the altered array. 
The order of the non-zero integers does not matter in the mutated array.
'''
def moving_zeroes(arr):
    number_zeros = arr.count(0)
    array_without_zeros = [i for i in arr if i != 0]
    array_with_zeros = [0] * number_zeros

    moved_zero_array = array_without_zeros + array_with_zeros
    return moved_zero_array

if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")