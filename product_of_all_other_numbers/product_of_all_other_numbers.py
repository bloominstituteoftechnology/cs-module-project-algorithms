'''
Input: a List of integers
Returns: a List of integers
'''
def product_of_all_other_numbers(arr):
    # Your code here
    # keep track of the index we are on
    current_index = 0
    # create a new array to use fo us to do multiplication
    new_array = []

    # loop until we go through the entire length of array
    while current_index < len(arr):
        #for our new multiplication number we start at 1 each time
        new_num = 1

        # loop through the entire array
        for x in range(0, len(arr)):
            # if we are on the current index we want to skip this iteration
            if current_index == x:
                continue
            #otherwise we will multiple this item to all the other
            else: 
                new_num *= arr[x]
        # after going through all the numbers in the array add the product to the array
        new_array.append(new_num)
        #go to the next index in the array
        current_index += 1
    
    return new_array


if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 2, 3, 4, 5]
    # arr = [2, 6, 9, 8, 2, 2, 9, 10, 7, 4, 7, 1, 9, 5, 9, 1, 8, 1, 8, 6, 2, 6, 4, 8, 9, 5, 4, 9, 10, 3, 9, 1, 9, 2, 6, 8, 5, 5, 4, 7, 7, 5, 8, 1, 6, 5, 1, 7, 7, 8]

    print(f"Output of product_of_all_other_numbers: {product_of_all_other_numbers(arr)}")
