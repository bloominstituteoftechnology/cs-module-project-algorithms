'''
Input: an integer
Returns: an integer
'''
def eating_cookies(n):
    if n == 0:
        return 1
    # Your code here
    counter = 0
    option_list = [1,2,3]

    def rec(num_cookies_left, *args):
        if num_cookies_left == 0:
            print('NO COOKIES LEFT! EXIT')
            return
        print('args', args)
        if args:
            option = args[0]
            if num_cookies_left >= option:
                print(f'we can still eat!! num cookie left: {num_cookies_left} with option: {option}')
                num_cookies_left -= option
                if num_cookies_left == 0:
                    nonlocal counter
                    counter += 1
                    print(f'counter ++ {counter}')
            else:
                return
            
        for item in option_list:
            print(f'lets go recursion with item: {item}')
            rec(num_cookies_left, item)    
    
    rec(n)
    print('counter', counter)
    return counter

if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_cookies = 5

    print(f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to each {num_cookies} cookies")
