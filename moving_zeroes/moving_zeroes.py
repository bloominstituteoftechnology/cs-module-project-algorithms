'''
Input: a List of integers
Returns: a List of integers
'''

x =150
s = str(x)
y = s.split(',')
print(y)
def moving_zeroes(arr):
    # Your code here
    new_arr = []
    zarr=[]
    for i in arr:
        s = str(i)
        s.split(',')
         
        new_arr.append(s)
        for i in new_arr:
            if '0' in i:
               zarr.append(i)
               new_arr.remove(i)
               
    return new_arr + zarr 


stuff = [10,3,4,5,20]
print("THIS",moving_zeroes(stuff)) 
if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")