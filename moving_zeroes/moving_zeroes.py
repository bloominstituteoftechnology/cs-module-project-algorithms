'''
Input: a List of integers
Returns: a List of integers
'''


def moving_zeroes(arr):
    holder = []

    for num in arr:
        if num == 0:
            holder.append(num)
        else:
            holder.insert(0, num)

    return holder


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")

"""
Input: a List of integers
Returns: a List of integers

"""

"""
what if we had a pointer that started at the beginning and a pointer that started at the end
and they moved towards each other in the middle?

if the left pointer "sees" a zero and the right pointer "sees" a non-zero 
swap 

if the left sees a non-zero increment
if the right sees a zero increment

"""

def moving_zeroes(arr):
    # initialize a left and right pointer
    # left is 0
    # right is last index in arr

    # while left <= right:
        # if left points at a zero and right points at non-zero
            # swap left and right items in original arr

            # increment left
            # increment right

        # else

            # if left is non-zero:
                # increment left

            # if right is zero:
                # decrement right

    return arr

"""
What can I do to avoid having nested loops or needing to slice the arrays?
What about the names of my variable names?
Could those also be improved?
"""




















