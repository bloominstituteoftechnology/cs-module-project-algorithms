'''
Input: a List of integers
Returns: a List of integers
'''
def product_of_all_other_numbers(arr):
    if len(arr) == 0:
        return
    newArray = [1 for _ in range(0, len(arr))]
    
    #use pointer
    for i in range (0, len(arr)):
        p1 = 0
        p2 = len(arr) - 1
        print(i)
        while p1 != i:
            if p1 != i:
                print('p1', p1)
                newArray[i] *= arr[p1]
                print('p1 newArray', newArray[i])
                p1 += 1
        while p2 != i:
            if p2 != i:
                print('p2', p2)
                newArray[i] *= arr[p2]
                print('newArray',newArray[i])
                p2 -= 1
    return(newArray)

print(product_of_all_other_numbers([2,3,4,5,4]))

    


if __name__ == '__main__':
    # Use the main function to test your implementation
    # arr = [1, 2, 3, 4, 5]
    arr = [2, 6, 9, 8, 2, 2, 9, 10, 7, 4, 7, 1, 9, 5, 9, 1, 8, 1, 8, 6, 2, 6, 4, 8, 9, 5, 4, 9, 10, 3, 9, 1, 9, 2, 6, 8, 5, 5, 4, 7, 7, 5, 8, 1, 6, 5, 1, 7, 7, 8]

    print(f"Output of product_of_all_other_numbers: {product_of_all_other_numbers(arr)}")
