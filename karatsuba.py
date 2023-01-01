import timeit

def karatsuba(x, y):
    if x < 10 and y < 10:
        return x * y

    num1_len = len(str(x))
    num2_len = len(str(y))

    n = max(num1_len,num2_len)
    
    nby2 = round(n/2)

    num1 = x // (10 ** nby2)
    rem1 = x % (10 ** nby2)

    num2 = y // (10 ** nby2)
    rem2 = y % (10 ** nby2)

    ac = karatsuba(num1, num2)
    bd = karatsuba(rem1, rem2)
    ad_plus_bc = karatsuba(num1 + rem1, num2 + rem2) - ac - bd

    return (10 ** (2*nby2))*ac + (10 ** nby2)*ad_plus_bc + bd

start = timeit.default_timer()
karatsuba_result = karatsuba(12345689123546789132456789321465789123456789,12345689123546789132456789321465789123456789)
stop = timeit.default_timer()
print('Time Karatsuba: ', stop - start)

start_2 = timeit.default_timer()
python_result = 12345689123546789132456789321465789123456789 * 12345689123546789132456789321465789123456789
stop_2 = timeit.default_timer()
print('Time Default Python Multiplication: ', stop_2 - start_2)

# Python uses O(N^2) grade school multiplication algorithm for small numbers, but for big numbers it uses Karatsuba algorithm.
# Basically multiplication is handled in C code, which can be compiled to machine code and executed faster.