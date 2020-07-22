'''
Input: an integer
Returns: an integer
'''
# n = [0, 1, 2, 3, 4, 5]
# perms = [1, 1, 2, 4, 7, 13]
# TRIBONNACI SEQUENCE D:



def eating_cookies(n, temp=None):
    series = [1, 1, 2]
    [series.append(series[k - 1] + series[k - 2] + series[k - 3]) for k in range(3, n+1)]
    return series[n]

if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_cookies = 5

    print(f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to each {num_cookies} cookies")
