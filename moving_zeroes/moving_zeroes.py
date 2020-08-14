'''
Input: a List of integers
Returns: a List of integers
'''
# This is the first pass solution of the function
# Will do a similar version as doing swaping
# Will have pointers that increment on the left and decrement on 
# the right.  The right will stop on a number that is not a zero
# The left will stop on a number that is a zero.  This process
# will stop when the pointers have crossed each other.
def moving_zeroes(arr):
    # checking the length of the array 
    # if the array is just one long then will just return the array
    if len(arr) == 1 or len(arr) == 0:
        return arr
    l_ptr = 0
    r_ptr = len(arr)-1
    while l_ptr < r_ptr:
       # incrementing  the left pointer
        while arr[l_ptr] != 0 and l_ptr < len(arr) -1:
            l_ptr +=1
        while arr[r_ptr] == 0 and r_ptr > 0:
            r_ptr -= 1
        # checking to make sure the pointers have 
        # not crossed each other
        if l_ptr < r_ptr:
            temp = arr[l_ptr]
            arr[l_ptr] = arr[r_ptr]
            arr[r_ptr] = temp

    return arr


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")