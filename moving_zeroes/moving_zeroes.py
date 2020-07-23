"""
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
'''




'''
Input: a List of integers
Returns: a List of integers

​
what if we had a pointer that started at the beginning
and a pointer that started at the end
and they moved towards each other in the middle?
​
if the left pointer "sees" a zero and the right pointer "sees" a non-zero
swap
​
if the left sees a non-zero increment
if the right sees a zero increment
'''
​"""


def moving_zeroes(arr):

    
    # initialize a left and right pointer
    left_pointer = 0
    right_pointer = (len(arr)-1)
    print(f'OG array {arr}')
    #print(f'ARR at left {arr[left_pointer]}')
    #print(f'ARR at right {arr[right_pointer]}')


    # left is 0
    # right is last index in arr
    # while left <= right:
    while left_pointer <= right_pointer:
        # if left points at a zero and right points at non-zero
        if arr[left_pointer] == 0 and arr[right_pointer] != 0:
            # swap left and right items in original arr
            arr[left_pointer], arr[right_pointer] = arr[right_pointer], arr[left_pointer]
            #print(f'!!!!!ARR at left {arr[left_pointer]}')
            #print(f'!!!!!!ARR at right {arr[right_pointer]}')
            
            # increment left
        left_pointer += 1
            # decrement right
        right_pointer -= 1

        #     # if left is non-zero:
        if arr[left_pointer] != 0:
            left_pointer += 1
            print(f'ARR at left {arr[left_pointer]}')
            
        #         # increment left
        #if right is zero:
        if arr[right_pointer] == 0:
        #         # decrement right
            right_pointer -= 1
    print(arr)
    return arr



if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")