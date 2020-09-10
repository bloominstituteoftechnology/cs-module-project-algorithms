"""
Input: a List of integers
Returns: a List of integers
"""


def moving_zeroes(arr):
    zeros = 0
    out = []
    for n in arr:
        if n == 0:
            zeros += 1
        else:
            out.append(n)
    out.extend([0] * zeros)
    return out


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")