'''
Input: a List of integers
Returns: a List of integers
'''
# return the product of every single element EXECPT the one that is selected. if index[0] is selected, index[0] is equal to the product of rest of the numbers 
def product_of_all_other_numbers(arr):
    # Your code here
    result = 1
    for nums in arr:
        result *= nums
        # print(result) 

    for i in range(len(arr)):
        arr[i] = result // arr[i]
    
    return arr
   
        


if __name__ == '__main__':
    # Use the main function to test your implementation
    # arr = [1, 2, 3]
    arr = [2, 6, 9, 8, 2, 2, 9, 10, 7, 4, 7, 1, 9, 5, 9, 1, 8, 1, 8, 6, 2, 6, 4, 8, 9, 5, 4, 9, 10, 3, 9, 1, 9, 2, 6, 8, 5, 5, 4, 7, 7, 5, 8, 1, 6, 5, 1, 7, 7, 8]

    print(f"Output of product_of_all_other_numbers: {product_of_all_other_numbers(arr)}")

