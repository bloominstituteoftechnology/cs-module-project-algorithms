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

