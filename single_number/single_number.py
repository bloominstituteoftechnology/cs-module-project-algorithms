'''
Input: a List of integers where every int except one shows up twice
Returns: an integer

```
Sample input: [2, 2, 1]
Expected output: 1
```

```
Sample iput: [4, 1, 2, 1, 2]
Expected output: 4
```

'''
def single_number(arr):
    # Your code here

    ### Count the number of times that a given value has appeared
    ## use a dictionary

    '''
    integer_count = {}

    for item in arr: #O(n)
        if item in integer_count: #O(1)
            integer_count[item] += 1
        else: 
            integer_count[item] = 1

    # at the end of the list, return only the value that has one instance
    for item in arr:
        if integer_count[item] == 1:
            print(item)
            return item

    #print(integer_count)

    '''

    #Nice, very short solutioon
    
    for item in arr:
        if arr.count(item) == 1:
            return item
    
    

    #pass


if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")