'''
Input: a List of integers
Returns: a List of integers
'''
def product_of_all_other_numbers(arr):
    # Your code here
    # multiply all indexes except current, set
    new_arr = []
    for index in range(0, len(arr)):
        product = 1
        for item in range(0, len(arr)):
            if index != item:
                product = product * arr[item]
        new_arr.append(int(product))

    return new_arr




if __name__ == '__main__':
    # Use the main function to test your implementation
    # arr = [1, 2, 3, 4, 5]
    # arr = [2, 6, 9, 8, 2, 2, 9, 10, 7, 4, 7, 1, 9, 5, 9, 1, 8, 1, 8, 6, 2, 6, 4, 8, 9, 5, 4, 9, 10, 3, 9, 1, 9, 2, 6, 8, 5, 5, 4, 7, 7, 5, 8, 1, 6, 5, 1, 7, 7, 8]
              i
    arr = [2, 4, 9, 0]
              j        
    print(f"Output of product_of_all_other_numbers: {product_of_all_other_numbers(arr)}")
