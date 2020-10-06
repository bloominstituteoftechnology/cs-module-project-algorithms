'''
Input: a List of integers
Returns: a List of integers
'''
# def product_of_all_other_numbers(arr):
#     # This one is a challenge
#     # I could do it in O(n^2) time by solving at each index
#     # I could also do it in O(n) time by multiplying all the numbers, then dividing by the number at each index
#     # But the directions say specifically not to divide

#     result = []

#     for i in range(len(arr)):
#         product = 1
#         for j in range(len(arr)):
#             if j != i:
#                 product *= arr[j]
#         result.append(product)

#     return result

# This solution runs in O(n) time, but uses division. I see that having 0s in your array causes this solution to fail.
# However, we could account for the 0s by counting them when building our initial product
def product_of_all_other_numbers(arr):
    product = 1
    zeroes = 0

    for num in arr:
        if num == 0:
            zeroes += 1
            if zeroes > 1: # if there are more than one zero
                return [0] * len(arr) # all of the products are going to be 0
        else:
            product *= num
    
    result = []
    
    # If there is one zero what we append depends on whether the current number is 0
    if zeroes == 1:
        for num in arr:
            result.append(0) if num != 0 else result.append(product)
    # Otherwise, we just append the total product divided by the current number
    else:
        for num in arr:
            result.append(product // num)

    return result


if __name__ == '__main__':
    # Use the main function to test your implementation
    # arr = [1, 2, 3, 4, 5]
    arr = [2] * 10000

    print(f"Output of product_of_all_other_numbers: {product_of_all_other_numbers(arr)}")
