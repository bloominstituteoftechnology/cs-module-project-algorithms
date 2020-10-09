import math
def product_of_all_other_numbers(arr):
    # Your code here
    new_calc_array = []
# find the product of all of the other numbers of an array input 
# iterate through the list until reaching the end
    for x in range(len(arr)):
        # temp = arr[x]
        # arr.remove(temp)
        ok_boii = math.prod(arr) // arr[x]
        new_calc_array.append(ok_boii)
        print(new_calc_array)

    return new_calc_array
    
arrOne = [7,9,1,8,6,7,8,8,7,10]
product_of_all_other_numbers(arrOne)