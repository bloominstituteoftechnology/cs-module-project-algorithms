'''
Input: a List of integers
Returns: a List of integers
'''
def product_of_all_other_numbers(arr): #it returns an array of all the products except for the index element(at the index)
    # Your code here
    new_product = [] #holds all new product values
    for x in range(0, len(arr)): #loop through the product array
        new_item = 1 #assigning index value to 1 in array we are looping through, so it wont affect outcome
        for y in range(0, len(arr)): #we are looping through original array
            if y != x: #if y element does not = the x element, that means the index doesnt match 
                new_item *= arr[y] #because the index doesnt match we dont include it (when we calculate product) , we include everything buy index
        new_product.append(new_item) #add our new products into product array
    return new_product #returning new product array

    


if __name__ == '__main__':
    # Use the main function to test your implementation
    # arr = [1, 2, 3, 4, 5]
    arr = [2, 6, 9, 8, 2, 2, 9, 10, 7, 4, 7, 1, 9, 5, 9, 1, 8, 1, 8, 6, 2, 6, 4, 8, 9, 5, 4, 9, 10, 3, 9, 1, 9, 2, 6, 8, 5, 5, 4, 7, 7, 5, 8, 1, 6, 5, 1, 7, 7, 8]

    print(f"Output of product_of_all_other_numbers: {product_of_all_other_numbers(arr)}")
