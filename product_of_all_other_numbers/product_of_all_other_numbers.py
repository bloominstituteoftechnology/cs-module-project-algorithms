'''
Input: a List of integers
Returns: a List of integers
'''
def product_of_all_other_numbers(arr):
    # Your code here
    new_calc_array = []
    temp_array = []
    total = 0
    current = 0
    current_next = 1
# find the product of all of the other numbers of an array input 
# iterate through the list until reaching the end
    for x in range(len(arr)):
        total = 1
        for y in range(len(arr)):
            if y == current:
                continue
            elif y == current_next:
                if total == 1:
                    total = arr[y]
                else:
                    total *= arr[y]
            else:
                total *= arr[y]
                
        current += 1
        current_next += 1
        new_calc_array.append(total)

    return new_calc_array
                    
                
                
# arr = [7, 9, 1, 8, 6, 7, 8, 8, 7, 10]
# product_of_all_other_numbers(arr)

# could possible seperate all of the elements into another array

if __name__ == '__main__':
    # Use the main function to test your implementation
    # arr = [1, 2, 3, 4, 5]
    # arr = [2, 6, 9, 8, 2, 2, 9, 10, 7, 4, 7, 1, 9, 5, 9, 1, 8, 1, 8, 6, 2, 6, 4, 8, 9, 5, 4, 9, 10, 3, 9, 1, 9, 2, 6, 8, 5, 5, 4, 7, 7, 5, 8, 1, 6, 5, 1, 7, 7, 8]
    arr = [7, 9, 1, 8, 6, 0, 7, 8, 8, 7, 10]
    print(f"Output of product_of_all_other_numbers: {product_of_all_other_numbers(arr)}")
