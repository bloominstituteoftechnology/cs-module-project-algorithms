'''
Input: a List of integers
Returns: a List of integers
'''
# This is the first pass of the solution
# Will loop through the list using the index
# will have a second loop within the  first loop 
# that will then multiply everthing found in the array
# except at the index of the first array
def product_of_all_other_numbers(arr):
    new_array = []
    
    for i in range(len(arr)):
        value = 1
        # second loop
        for k in range(len(arr)):
            if i != k:
                # do the multiplication here
                value *= arr[k]
        # appending to the array
        new_array.append(value)
    return new_array

    

   


if __name__ == '__main__':
    # Use the main function to test your implementation
    #arr = [1, 2, 3, 4, 5]
    arr = [2, 6, 9, 8, 2, 2, 9, 10, 7, 4, 7, 1, 9, 5, 9, 1, 8, 1, 8, 6, 2, 6, 4, 8, 9, 5, 4, 9, 10, 3, 9, 1, 9, 2, 6, 8, 5, 5, 4, 7, 7, 5, 8, 1, 6, 5, 1, 7, 7, 8]

    print(f"Output of product_of_all_other_numbers: {product_of_all_other_numbers(arr)}")
