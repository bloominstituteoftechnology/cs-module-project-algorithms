'''
Input: a List of integers
Returns: a List of integers
'''
#  using division
# def product_of_all_other_numbers(arr):
#     if len(arr) == 0:
#         return 0

#     if len(arr) == 1:
#         return arr(0)

#     product_list = [0] * len(arr)
    
#     product = 1

#     for x in arr:
#         product *= x
       
#     for i in range(len(arr)):
#         arr[i] = int(product/arr[i])

#     return arr

def product_of_all_other_numbers(arr):

    if len(arr) == 0:
        return 0

    if len(arr) == 1:
        return arr(0)

    product_list = [0] * len(arr)

    temp_product = 1
    for i in range(len(arr)):
        product_list[i] = temp_product
        temp_product *= arr[i]

    temp_product = 1
    # count backwords through range by -1
    for i in range(len(arr) - 1, -1, -1):
        product_list[i] *= temp_product
        temp_product *= arr[i]

    return product_list


if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 2, 3]
    # arr = [2, 6, 9, 8, 2, 2, 9, 10, 7, 4, 7, 1, 9, 5, 9, 1, 8, 1, 8, 6, 2, 6, 4, 8, 9, 5, 4, 9, 10, 3, 9, 1, 9, 2, 6, 8, 5, 5, 4, 7, 7, 5, 8, 1, 6, 5, 1, 7, 7, 8]

    print(f"Output of product_of_all_other_numbers: {product_of_all_other_numbers(arr)}")
