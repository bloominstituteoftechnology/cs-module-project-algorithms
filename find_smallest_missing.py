'''
def find_smallest_missing(arr):
    for i in range(0, len(arr)):
        if arr[i] != i:
            return i
    return len(arr)
arr = [0,1,2,3,4,6,7,8,9]
test = find_smallest_missing(arr)
print(test)
'''

# Binary version
def find_smallest_missing(arr):
    low = 0 
    high = len(arr) - 1
    
    while low < high:
        mid = (low+high) // 2
        if arr[mid] == mid:
            if arr[mid+1] != arr[mid]+1:
                return arr[mid] + 1
            
            low = mid + 1
        else:
            high = mid

arr = [1,2,3,4,5,6,7,8,9]
find_smallest_missing(arr)
