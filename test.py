# x = int(input("Please enter an integer: "))

# if x < 0:
#     x = 0
#     print('Negative changed to zero')
# elif x == 0:
#     print('Zero')
# elif x in range(1,10):
#     print('Single')
# else:
#     print('More')

# ---------------------------------------

# import math

# r = 3

# area = math.pi * r * r

# print(f"{area:.4f} ft\u00b2") 

# ---------------------------------------

def devides_self(num):
    value = num

    while num != 0:
        digit = int(value % 10)
        # print(digit)

        if digit == 0 or num % digit !=0:
            return False

        value /= 10

    return True



print(devides_self(120))
print(devides_self(39))