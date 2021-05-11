Input = "00000000000000000000000000001011" #Insert binary number here
n =int(Input, 2)    #treats the input as binary

def count_bits(n):
    x = 0
    while (n):      #while n == non-zero, cond. = True (e. g. 1), while n == zero, cond. False (e. g. 0)
        x += n & 1  #x = x + (n&1) --> n AND 1
        n >>= 1     #right shift by 1
    return x


print(count_bits(n))