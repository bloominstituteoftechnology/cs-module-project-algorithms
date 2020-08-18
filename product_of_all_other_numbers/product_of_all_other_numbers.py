'''
Input: a List of integers
Returns: a List of integers
'''
def product_of_all_other_numbers(arr):
    # a starting int
    counter = 0
    # empty list for result
    res = []
    # the loop runs as long as the counter is less then the length of the array
    while counter < len(arr):
        #starting 
        if counter ==0:
            #prod is holder for int number 1
            # take the prod multiply by elements in the array
            prod = 1
            for i in range(1, len(arr)):
                prod = (prod*arr[i])
            counter += 1
            #counter
            # append to result
            res.append(prod)
        #if the arr is equal to zero
        elif counter == len(arr)-1:
            #take prod multiply elements in the array
            prod = 1
            for i in range(0, len(arr)-1):
                prod = (prod*arr[i])
            counter += 1
            res.append(prod)
        # counter > len(arr)
        else:
            left = arr[:counter]
            right = arr[counter+1:]
            prod = 1
            for num in (left + right):
                prod = (prod*num)
            counter += 1
            res.append(prod)


    return res


if __name__ == '__main__':
    # Use the main function to test your implementation
    # arr = [1, 2, 3, 4, 5]
    arr = [2, 6, 9, 8, 2, 2, 9, 10, 7, 4, 7, 1, 9, 5, 9, 1, 8, 1, 8, 6, 2, 6, 4, 8, 9, 5, 4, 9, 10, 3, 9, 1, 9, 2, 6, 8, 5, 5, 4, 7, 7, 5, 8, 1, 6, 5, 1, 7, 7, 8]

    print(f"Output of product_of_all_other_numbers: {product_of_all_other_numbers(arr)}")


