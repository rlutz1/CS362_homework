import cmath

i = complex(0, 1)

# def IFFT(P):
#   # P is a list of points here.
#   n = len(P) # needs to be a power of 2 here, pad as necessary prior
#   if n == 1:
#     return [P[0]]
  
#   # exp = (2 * math.pi * i) / n
#   # w = math.e ^ exp
#   theta = -2 * math.pi / n 
#   w = list( complex( math.cos(theta * i), math.sin(theta * i)) for i in range(n) ) 
  
#   Pe, Po = P[0::2], P[1::2]
#   ye, yo = FFT(Pe), FFT(Po)

#   y = [0] * n
#   mid = n // 2
#   for j in range(mid):
#     prod = w[j] * yo[j]
#     even_grab = ye[j]
#     y[j] = even_grab + prod
#     y[j + mid] = even_grab - prod

#   return y

# def FFT(P):
#   # P is a coefficient list here.
#   n = len(P) # needs to be a power of 2 here, pad as necessary prior
#   if n == 1:
#     return [P[0]]
  
#   # exp = (2 * math.pi * i) / n
#   # w = math.e ^ exp
#   theta = -2 * math.pi / n
#   w = list( complex( math.cos(theta * i), math.sin(theta * i)) for i in range(n) ) 

#   Pe, Po = P[0::2], P[1::2]
#   ye, yo = FFT(Pe), FFT(Po)

#   y = [0] * n
#   mid = n // 2
#   for j in range(mid):
#     prod = w[j] * yo[j]
#     even_grab = ye[j]
#     y[j] = even_grab + prod
#     y[j + mid] = even_grab - prod

#   return y


# Fast Fourier Transform implementation
def FFT(coeffs, invert=False):
    n = len(coeffs)
    if n == 1:
        return

    # Split into even and odd indexed terms
    even_terms = [coeffs[2 * i] for i in range(n // 2)]
    odd_terms = [coeffs[2 * i + 1] for i in range(n // 2)]

    # Recursive FFT on both halves
    FFT(even_terms, invert)
    FFT(odd_terms, invert)

    # Calculate angle and root of unity
    pi = cmath.pi
    angle = 2 * pi / n * (-1 if invert else 1)
    w = complex(1, 0)
    wn = cmath.exp(complex(0, angle))

    # Combine
    for i in range(n // 2):
        t = w * odd_terms[i]
        coeffs[i] = even_terms[i] + t
        coeffs[i + n // 2] = even_terms[i] - t

        if invert:
            coeffs[i] /= 2
            coeffs[i + n // 2] /= 2
        w *= wn

# def pair_wise_mult(A, B):
#   C = []
#   bc = 0
#   for x1, y1 in A:
#     x2, y2 = B[bc]
#     C.append((x1 * x2, y1 * y2))
#     bc += 1
#   return C


# Function to multiply two polynomials using FFT
def multiply(A, B):
    n = 1
    while n < len(A) + len(B):
        n <<= 1

    fftA = [complex(A[i] if i < len(A) else 0, 0) for i in range(n)]
    fftB = [complex(B[i] if i < len(B) else 0, 0) for i in range(n)]

    # Apply forward FFT to both
    FFT(fftA, False)
    FFT(fftB, False)

    # Point-wise multiplication
    for i in range(n):
        fftA[i] *= fftB[i]

    # Inverse FFT to get back coefficients
    FFT(fftA, True)

    # Round real parts to integers
    result = [round(fftA[i].real) for i in range(n)]

    # Remove trailing zeroes (optional)
    while len(result) >= (len(A) + len(B)):
        result.pop()

    return result

def eval(P, x):
    # evaluate a polynomial at a given x
    # should be a list of coefficients, we'll assume lowest to highest order
    exp = 0
    acc = 0
    for coeff in P:
        acc += coeff * (x ** exp)
        exp += 1
    return acc
        
        

# A = [1, 1, 1, 1] # x^3 + x^2 + x + 1
A = [1, 2, 3, 4] # number is 4321
B = [1, 2, 2, 0] # number is 221
# 4321 * 221 = 954941 !
A = [2, 0, 0, 0]
B = [0, 0, 0, 2]
# 2 * 2000 = 4000


product = multiply(A, B)
print(*product)

sol = eval(product, 10)
print(sol)

# fft_returnA = FFT(A)
# fft_returnB = FFT(B)
# A_points = []
# B_points = []

# for a in fft_returnA:
#   A_points.append((round(a.real), round(a.imag)))
#   # print(a, end=" ")
# print(A_points) # the returned 

# for b in fft_returnB:
#   B_points.append((round(b.real), round(b.imag)))
#   # print(b, end=" ")
# print(B_points)

# C_points = pair_wise_mult(A_points, B_points)
# print(C_points)

# final_coef = IFFT(C_points)
# print(final_coef)
