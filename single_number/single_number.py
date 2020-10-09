'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''
def single_number(arr):
    # Your code here
    # First pass Solution
    
    # so we have arr would have some duplicate elements
    # then we would only pick the element with no duplicates
    # how would we do that? with very fool way
    # hmm..
    # let's do this
    # create an empty list
    # loop thru arr and append element to the new empty list
    # if we already have the element, instead of appending it,
    # pop the element from the new list
    # this is O(n^2) time complexity

    storage = {}
    new_list = []
    print(f'arr is {arr}')
    for element in arr:
        if element not in storage:
            storage[element] = 1
        else:
            storage[element] += 1
    for key, value in storage.items():
        if value == 1:
            new_list.append(key)

    if len(new_list) == 1:
        return new_list[0]
    return new_list


if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")