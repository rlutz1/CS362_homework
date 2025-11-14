import cmath

i = complex(0, 1)
pi = cmath.pi

# FFT implementation
def FFT(coeffs, invert):
    n = len(coeffs)
    if n == 1:
        return

    # even/odd coefficients of given coeff array
    even_coeff = coeffs[::2]
    odd_coeff = coeffs[1::2]

    # Recursive FFT on both halves
    FFT(even_coeff, invert)
    FFT(odd_coeff, invert)

    # get your roots of unity to evaluate at to make your points
    inversion_factor = -1
    if invert: inversion_factor = 1

    angle = 2 * pi / n * inversion_factor # 1/w if inverting! otherwise normal exp
    w = complex(1, 0) # set up the omega as 1 to initialize
    wn = cmath.exp(complex(0, angle)) # e ^ 2(pi)(i)/n or e ^ -2(pi)(i)/n (if invert)

    # get your points or coeffs
    for i in range(n // 2): # from 0 -> n/2 - 1
        t = w * odd_coeff[i] 
        coeffs[i] = even_coeff[i] + t # positive pairing
        coeffs[i + n // 2] = even_coeff[i] - t # negative pairing

        if invert: # inversion adjustment
            coeffs[i] /= 2
            coeffs[i + n // 2] /= 2
            
        w *= wn # accumulate to next root of unity


# multiply two polynomials using FFT
def mult_poly(A, B):
    # pad out to n + m in length to fit the new polynomial of degree at least n + m
    n = len(A)
    m = len(B)
    new_degree = 1
    while new_degree < n + m:
        new_degree <<= 1 # get this to a multiple of 2

    # pad with high order zero coefficients, convert to complex
    fftA = [complex(A[i] if i < n else 0, 0) for i in range(new_degree)]
    fftB = [complex(B[i] if i < m else 0, 0) for i in range(new_degree)]
   
    # apply fft to get 2n points at roots of unity
    FFT(fftA, False)
    FFT(fftB, False)

    # point-wise multiplication
    for i in range(new_degree):
        fftA[i] *= fftB[i]

    # invert! get the coeffs back and place into
    FFT(fftA, True)

    # round the reals--round off errors likely
    for i in range(new_degree):
        fftA[i] = round(fftA[i].real)

    # strip the padding from the end
    i = new_degree - 1
    while fftA[i] == 0:
        fftA.pop()
        i -= 1

    return fftA

def eval(P, x):
    # evaluate a polynomial at a given x
    # should be a list of coefficients, need to process
    # backwards since its given lowest to highest ordering
    # use horners method/nested mult to achieve linear mult
    n = len(P) - 1
    acc = P[n]
    for i in range(n - 1, -1, -1):
        acc = (acc * x) + P[i]
    return acc
        
# SCRIPT RUN

# comment out any A or B to try different combos

# 341 * 1 = 341
A = [1, 4, 3] 
B = [1] 

# 21 ^ 2 = 441 
# A = [1, 2]
# B = [1, 2]

# 4037 * 65 = 262405
# A = [7, 3, 0, 4]
# B = [5, 6]

# 12350960 * 53 = 654600880
# A = [0, 6, 9, 0, 5, 3, 2, 1]
# B = [3, 5]

# 2 * 4 = 8
# A = [4]
# B = [2]

product = mult_poly(A, B)
sol = eval(product, 10)
print(sol)