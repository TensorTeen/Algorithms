# Python implementation of Karatsuba algorithm for bit string multiplication.
 
# Helper method: given two unequal sized bit strings, converts them to
# same length by adding leading 0s in the smaller string. Returns the
# the new length
def make_equal_length(str1, str2):
    len1 = len(str1)
    len2 = len(str2)
    if len1 < len2:
        for i in range(len2 - len1):
            str1 = '0' + str1
        return len2
    elif len1 > len2:
        for i in range(len1 - len2):
            str2 = '0' + str2
    return len1 # If len1 >= len2
 
# The main function that adds two bit sequences and returns the addition
def add_bit_strings(first, second):
    result = ""  # To store the sum bits
 
    # make the lengths same before adding
    length = make_equal_length(first, second)
    carry = 0  # Initialize carry
 
    # Add all bits one by one
    for i in range(length-1, -1, -1):
        first_bit = int(first[i])
        second_bit = int(second[i])
 
        # boolean expression for sum of 3 bits
        sum = (first_bit ^ second_bit ^ carry) + ord('0')
 
        result = chr(sum) + result
 
        # boolean expression for 3-bit addition
        carry = (first_bit & second_bit) | (second_bit & carry) | (first_bit & carry)
 
    # if overflow, then add a leading 1
    if carry:
        result = '1' + result
 
    return result
 
# A utility function to multiply single bits of strings a and b
def multiply_single_bit(a, b):
    return int(a[0]) * int(b[0])
 
# The main function that multiplies two bit strings X and Y and returns
# result as long integer
def multiply(X, Y):
    # Find the maximum of lengths of x and Y and make length
    # of smaller string same as that of larger string
    n = max(len(X), len(Y))
    X = X.zfill(n)
    Y = Y.zfill(n)
 
    # Base cases
    if n == 0: return 0
    if n == 1: return int(X[0])*int(Y[0])
 
    fh = n//2  # First half of string
    sh = n - fh  # Second half of string
 
    # Find the first half and second half of first string.
    Xl = X[:fh]
    Xr = X[fh:]
 
    # Find the first half and second half of second string
    Yl = Y[:fh]
    Yr = Y[fh:]
 
    # Recursively calculate the three products of inputs of size n/2
    P1 = multiply(Xl, Yl)
    P2 = multiply(Xr, Yr)
    P3 = multiply(str(int(Xl, 2) + int(Xr, 2)), str(int(Yl, 2) + int(Yr, 2)))
 
    # Combine the three products to get the final result.
    return P1*(1<<(2*sh)) + (P3 - P1 - P2)*(1<<sh) + P2
 
if __name__ == '__main__':
    print(multiply(str("1101001101110010111010001111000000011010110001110010011100110010101110101000011100110001101010101001111010110010110010110100000111100000101011100101111000011001101010001010001000011110111101111100001110101001011"), str("1111010001100000100100101011001111010001111101100100000001001011101000111010101011100100010110100101110011111011001000000010010101000111110010111110110101000101110110110010100000100011101111000001001000101010000")))
