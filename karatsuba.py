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



print(karatsuba(123412341234123412343121245687,8965852156285623182318446))