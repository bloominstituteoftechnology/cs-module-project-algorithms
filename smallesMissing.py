# Find the smalles missing elemenet from an array 

def find_smallest_missing(arr):
    low = 0
    high = len(arr) - 1
    # handle our edge case where 0 is the smallest missing 
    if arr[0] != 0:
        return 0
​
    # handle edge case where no element is missing
    if arr[high] == high:
        return arr[-1] + 1
​
    # is there a possibility of using binary search for this problem? 
    # with binary search, we need to know our target element 
    # the smallest element is the first element that doesn't match its array index 
    # can we use binary search to find this element
​
    # use binary search, except when we check the midpoint element, we're 
    # checking to see if the value matches the index itself 
​
    while low < high:
        mid = (low + high) // 2
​
        # if it does, then the smallest missing element could still occur after this point 
        # so we'll cut out the left half 
        if arr[mid] == mid:
            # check the adjacent element to see if it's the smallest missing 
            # if arr[mid + 1] != arr[mid] + 1:
            #     return arr[mid] + 1
            # update our low variable 
            low = mid + 1
​
        # if it doesn't, then either the midpoint is the smallest missing element, or
        # the smallest missing happened earlier to the left 
        # so we'll cut out the right half
        else:
            high = mid 
​
        # continue this process until we narrow it down to either one element or 
        # the low and high indices surpass one another 
​
    # if we don't find anything by the end of the loop, then there was no smallest 
    # missing element, so return the last element + 1
	return high