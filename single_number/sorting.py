# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements

    # set index values to iterate through the sorted arrays and add to merged
    #. array
    k = 0
    i = 0
    j = 0

    # while index values are in range
    while (i < len(arrA)) and (j < len(arrB)):
        
        # if the value at the index in first array is less than or equal to
        #. the value at the index in the second array, add it to the merged
        #. array and increase i by 1
        if arrA[i] <= arrB[j]:
            merged_arr[k] = arrA[i]
            i += 1
            
        # Otherwise, add the value in the second array to merged array because
        #. it is smaller, and increment j by 1
        else:
            merged_arr[k] = arrB[j]
            j += 1
            
        # increment k by 1 no matter what
        k += 1
        
    # to account for when arrB is empty and arrA still has values
    while (i < len(arrA)):
        
        # each element gets added to merged_arr until index i is out of
        #. range
        merged_arr[k] = arrA[i]
        i += 1
        k += 1
        
    # same thing for when arrA is empty and arrB still has values
    while (j < len(arrB)):
        merged_arr[k] = arrB[j]
        j += 1
        k += 1

    return merged_arr

# TO-DO: implement the Merge Sort function below recursively
def merge_sort(arr):
    # Your code here

    if len(arr) > 1:
    
        # find the mid index so we can slice into left and right sublists
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]

        # recur on the left
        left = merge_sort(left)
        # recur on the right
        right = merge_sort(right)
        
        arr = merge(left, right)

    return arr