"""
Input: a List of integers
Returns: a List of integers
"""


def moving_zeroes(arr):
    # Your code here
    list = arr.count(0)
    current = 0

    while current < list:
        arr.pop(arr.index(0))
        arr.append(0)

        current += 1

    return arr


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")
