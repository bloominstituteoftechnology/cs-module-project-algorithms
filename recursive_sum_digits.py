def sum_digits(n):

    if n < 10:
        return n

    else:
        last = n % 10
        all_but_last = n // 10

    return sum_digits(all_but_last) + last
