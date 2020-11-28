'''
Input: a List of integers
Returns: a List of integers
'''
def product_of_all_other_numbers(arr):
    # Your code here
    placeHolder = [0] * len(arr)        # create placeholder, assign 0 to all indexes
    total = 1                           # total to be multiplied 
    for i in range(len(arr)):
        total = total * arr[i]           # multiply everything and add to total
        
    for i in range(len(arr)):
        placeHolder[i] = int(total/arr[i])    # for the spot in placehold divide 
                    
    return placeHolder


if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [9, 90]
    #arr = [1, 2, 3, 4, 5]
    #arr = [2, 6, 9, 8, 2, 2, 9, 10, 7, 4, 7, 1, 9, 5, 9, 1, 8, 1, 8, 6, 2, 6, 4, 8, 9, 5, 4, 9, 10, 3, 9, 1, 9, 2, 6, 8, 5, 5, 4, 7, 7, 5, 8, 1, 6, 5, 1, 7, 7, 8]

    print(f"Output of product_of_all_other_numbers: {product_of_all_other_numbers(arr)}")
