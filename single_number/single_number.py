"""
Input: a List of integers where every int except one shows up twice
Returns: an integer
"""


def single_number(arr, num):
    # Your code here
    # sort your code
    arr.sort()
    # set a starting point
    start_count = len(arr) + 1
    # find the uncommon number
    uncommon = -1
    # create counter
    current = 1
    # loop
    for i in range(1, len(arr)):
        # go to next value
        if arr[i] == arr[i - 1]:
            current += 1

        else:
            if current < start_count:
                start_count = current
                uncommon = arr[len(arr) - 1]

    return uncommon





    res = arr[0]
    for i in range(1, num):
        res = res ^ arr[i]
    return res


if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr, len(arr))}")
