'''
Input: a List of integers
Returns: a List of integers
'''
def product_of_all_other_numbers(arr):
    # ugly
    from functools import reduce

    #return [reduce(lambda x,y: x*y, [j for j in arr if j != i]) for i in arr]
    
    forward = [1]
    backward = [1]
    tally = 1
    for i in range(len(arr)-1):
        tally = tally * arr[i]
        forward.append(tally)

    arr.reverse()

    tally = 1
    for i in range(len(arr)-1):
        tally = tally * arr[i]
        backward.append(tally)

    backward.reverse()

    output = list(map(lambda x,y:x*y,forward,backward))

    return output

# [1], [1]*[2], [1]*[2]*[3], [1]*[2]*[3]*[4], [1]*[2]*[3]*[4]*[5]
# [5], [5]*[4], [5]*[4]*[3], [5]*[4]*[3]*[2], [5]*[4]*[3]*[2]*[1]

# 1, [1], [1]*[2], [1]*[2]*[3], [1]*[2]*[3]*[4]
# 1, [5], [5]*[4], [5]*[4]*[3], [5]*[4]*[3]*[2] - reverse this then elementwise multiply

if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 2, 3, 4, 5]
    #arr = [2, 6, 9, 8, 2, 2, 9, 10, 7, 4, 7, 1, 9, 5, 9, 1, 8, 1, 8, 6, 2, 6, 4, 8, 9, 5, 4, 9, 10, 3, 9, 1, 9, 2, 6, 8, 5, 5, 4, 7, 7, 5, 8, 1, 6, 5, 1, 7, 7, 8]

    print(f"Output of product_of_all_other_numbers: {product_of_all_other_numbers(arr)}")
