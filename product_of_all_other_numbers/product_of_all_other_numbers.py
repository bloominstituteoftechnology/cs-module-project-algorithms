'''
Input: a List of integers
Returns: a List of integers
'''
# ***First Pass***

    # receives an arr of ints [1, 5, 3, 4, 6]
    # loop through the loop through again
        # declare variable for index
        # check if looped through to the last index
            # skip last index if there and keep going
            # otherwise, multiple  all values together and keep going
        # insert each answer into a new array
    #return new array


def product_of_all_other_numbers(arr):
    current_index = 0
    new_array = []
    length = len(arr)

    while current_index < length: # start "counter" loop
        inside_index = 0 # counter for inside loop
        result = 1 # multiply all elements by 1
        while inside_index < length: # loop over array for each item
            if inside_index == current_index: # if inside index is same as current index
                inside_index += 1 # then increment the inside loop by one
            else: # unless
                result = result * arr[inside_index] # multiply the items together
                inside_index += 1 # increment the inside loop by 1
        new_array.append(result) # append result to new array
        current_index += 1 # increment index for outer loop
    return new_array



if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 2, 3, 4, 5]
    # arr = [2, 6, 9, 8, 2, 2, 9, 10, 7, 4, 7, 1, 9, 5, 9, 1, 8, 1, 8, 6, 2, 6, 4, 8, 9, 5, 4, 9, 10, 3, 9, 1, 9, 2, 6, 8, 5, 5, 4, 7, 7, 5, 8, 1, 6, 5, 1, 7, 7, 8]

    print(f"Output of product_of_all_other_numbers: {product_of_all_other_numbers(arr)}")
