'''
Input: a List of integers
Returns: a List of integers
'''

def product_of_all_other_numbers(arr):
    # receives an array of ints [1, 7, 3, 4] arr
    # loop within a loop
        # declare a variable for index
        # check to see if we're on that index in the loop
            # if we're on that index, ignore that index's value (skip) and keep going (increase index)
            # otherwise, multiple all values together and keep going (increase index)
        # insert each answer into a new array
    # returns new array

    current_index = 0
    new_array = []

    while current_index < len(arr): # start "counter" loop
        inside_index = 0 # counter for inside loop
        result = 1 # need this to multiply elements
        while inside_index < len(arr): # loop over array for each item
            if inside_index == current_index: # if the inside index is the same amount of times as the current index
                inside_index += 1 # then increment the inside counter loop by 1
            else: # otherwise
                result = result * arr[inside_index] # multiple the items together
                inside_index += 1 # increment the inside counter loop by 1
        new_array.append(result) # append result to new array
        current_index += 1 # increment index for outer loop by 1
    return new_array
        

if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 2, 3, 4, 5]
    # arr = [2, 6, 9, 8, 2, 2, 9, 10, 7, 4, 7, 1, 9, 5, 9, 1, 8, 1, 8, 6, 2, 6, 4, 8, 9, 5, 4, 9, 10, 3, 9, 1, 9, 2, 6, 8, 5, 5, 4, 7, 7, 5, 8, 1, 6, 5, 1, 7, 7, 8]

    print(f"Output of product_of_all_other_numbers: {product_of_all_other_numbers(arr)}")
