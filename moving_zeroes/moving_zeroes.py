'''
Input: a List of integers
Returns: a List of integers
'''
def moving_zeroes(arr):
    # Your code here

    # Old Code:
    i = 0
    end_idx = len(arr) - 1
    while i < len(arr):
        # print(i, end_idx, arr[i])
        if arr[i] == 0:
            if i >= end_idx:
                break
            arr.append(arr.pop(i))
            i -= 1
            end_idx -= 1
        i += 1
    
    return arr

    # Currently, it employs what I'm going to call a rollback-
    # selection sort, which has a runtime of O(n+m-m), where 
    # n is the length of the array and m is the number of zeroes
    # in the array. I specify that the runtime is plus m minus m
    # because every time a zero is found, it rolls back the index
    # the search was looking at by one, but also decreases the index
    # where it stops looking by one.

    # Also, I do not think that I can improve this code in any way,
    # considering it has an O(n) runtime, whereas a standard
    # selection sort, as well as a bubble sort, would be O(nm)

    # maybe if I used quicksort or mergesort, but then again
    # the runtime with the old code for me is 0.001s, so I
    # wouldn't be able to tell.

if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 0, 0, 0, 3, 2, 1] 

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")