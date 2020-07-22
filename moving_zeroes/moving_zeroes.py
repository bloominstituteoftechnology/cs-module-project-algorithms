'''
Input: a List of integers
Returns: a List of integers



```
Sample input: [0, 3, 1, 0, -2]
Expected output: 3
Expected output array state: [3, 1, -2, 0, 0]
```

```
Sample input: [4, 2, 1, 5]
Expected output: 4
Expected output array state: [4, 2, 1, 5]
```



'''
def moving_zeroes(arr):
    # Your code here

    ## go through each item in the list 
    for item in arr:
        ## if that item is not a zero , move it to the left size of the array
        if item != 0:
            arr.remove(item)
            arr.insert(0, item)
    
    print(arr)
    return arr
    

    #pass


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")