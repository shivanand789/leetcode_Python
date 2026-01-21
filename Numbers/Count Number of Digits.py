
def CountDigits(num):
    # Handling 0 immediately
    if num == 0:
        return 1

    # Handling negatives to prevent infinite loops or errors
    num = abs(num)

    cnt = 0
    while num > 0:
        num //= 10  # This is slightly faster than num = num // 10
        cnt += 1
    return cnt
print(CountDigits(1231))


import math

def CountDigits_log(num):
    if num == 0: return 1
    return math.floor(math.log10(abs(num))) + 1