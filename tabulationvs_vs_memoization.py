# Tabulation Example: start from zero and go UP to n

def tab_fibonacci(n):

    # start at n = 0 and n = 1:
    # [0, ........ 0] length is less than or equal to n
    # [0,1,1,2,3,4,5........]

    solution_table = [0 for _ in range(0, n+1)]

    solution_table[0] = 1
    solution_table[1] = 1
    
    for i in range(2, n+1):
        solution_table[i] = solution_table(i-1) + solution_table(i-2)

    return solution_table[n]



