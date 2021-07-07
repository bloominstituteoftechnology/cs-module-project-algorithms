# ### FIRST_PASS:
# def single_number(arr):
#     '''
#     Input: a List of integers where every int except one shows up twice
#     Returns: an integer
#     '''
#     # Your code here

#     # create a counter
#     count = 0

#     # loop through array and update counter
#     for i in arr:
#         # compare count of item
#         if arr.count(i) == 1:
#             return i

### OPTIMIZED:
def single_number(arr):
    '''
    Input: a List of integers where every int except one shows up twice
    Returns: an integer
    '''
    # use a set to hold memory
    memory = set()

    # loop through array
    for i in arr:
        # if elem in set
        if i in memory:
            memory.remove(i)
        else:
            memory.add(i)

    # set should only have 1 elem
    return list(memory)[0]


if __name__ == '__main__':
    # # Use the main function to test your implementation
    # arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    # print(f"The odd-number-out is {single_number(arr)}")

    # Examples
    # ```
    # Sample input: [2, 2, 1]
    # Expected output: 1
    # ```

    # ```
    # Sample iput: [4, 1, 2, 1, 2]
    # Expected output: 4
    # ```

    samp = [4, 1, 2, 1, 2]

    count = 0
    for i in samp:
        # print(f"{i}:{samp.count(i)}")
        if samp.count(i) == 1:
            print(i)
    # print(count)
    # breakpoint()
