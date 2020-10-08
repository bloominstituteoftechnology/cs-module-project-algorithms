'''
Input: a List of integers
Returns: a List of integers



```
[1, 7, 3, 4]
```
your function should return 
```
[84, 12, 28, 21]
``` 
by calculating 
```
[7*3*4, 1*3*4, 1*7*4, 1*7*3]
```



'''
def product_of_all_other_numbers(arr):
    # Your code here

    final_array = []
    # for each item in an array
    for item in arr:
        print(f'ITEM {item}')
        ## Need to make a copy of this original array, otherwise it updates the original
        to_multiply = arr.copy()
        #print(f'OG TO MULTIPLY {to_multiply}')
        # # take in each other item BUT pop out the current item
        to_multiply.remove(item)
        print(f'NEW TO MULTIPLY {to_multiply}')

        #create a final value to be appended to a list for each item
        multiplied = 1

        # multiply all the items together
        for item in to_multiply:
            multiplied *= item
            print(f'MULTIPLIED: {multiplied}')
        
        final_array.append(multiplied)
        print(f'FINAL ARRAY {final_array}') 
    return final_array
    #pass


if __name__ == '__main__':
    # Use the main function to test your implementation
    #arr = [1, 2, 3, 4]
    # arr = [1, 2, 3, 4, 5]
    # arr = [2, 6, 9, 8, 2, 2, 9, 10, 7, 4, 7, 1, 9, 5, 9, 1, 8, 1, 8, 6, 2, 6, 4, 8, 9, 5, 4, 9, 10, 3, 9, 1, 9, 2, 6, 8, 5, 5, 4, 7, 7, 5, 8, 1, 6, 5, 1, 7, 7, 8]

    print(f"Output of product_of_all_other_numbers: {product_of_all_other_numbers(arr)}")
