
def moving_zeroes(arr):
    """
    Retuns a list of integers with 0s at the end
    
        Parameters:
                arr (list): a list of integers n length

        Returns:
                arr (list): a list of integers with the same length as input
    """
    
    zeroes = []
    non_zeroes = []
    
    for num in arr: # ---> O(n)
        if num != 0:
            non_zeroes.append(num)
        else:
            zeroes.append(num)
            
    answer = non_zeroes + zeroes
    
    return answer

if __name__ == '__main__':
    # Use the main function here to test out your implementation
    # arr = [0, 3, 1, 0, -2]
    arr = [0, 3, 1, 0, -2, 0, 10, 5, 3, 0]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")