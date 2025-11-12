import math

i = complex(0, 1)

def FFT(P):
  # P is a coefficient list here.
  n = len(P) # needs to be a power of 2 here, pad as necessary prior
  if n == 1:
    return [P[0]]
  
  # exp = (2 * math.pi * i) / n
  # w = math.e ^ exp
  theta = -2 * math.pi / n
  w = list( complex( math.cos(theta * i), math.sin(theta * i)) for i in range(n) ) 

  Pe, Po = P[0::2], P[1::2]
  ye, yo = FFT(Pe), FFT(Po)

  y = [0] * n
  mid = n // 2
  for j in range(mid):
    prod = w[j] * yo[j]
    even_grab = ye[j]
    y[j] = even_grab + prod
    y[j + mid] = even_grab - prod

  return y


def pair_wise_mult(A, B):
  print()

# A = [1, 1, 1, 1] # x^3 + x^2 + x + 1
A = [1, 2, 3, 4] 
B = [1, 2, -1, 1] # x^3 + 2x^2 - x + 1

fft_returnA = FFT(A)
fft_returnB = FFT(B)
A_points = []
B_points = []

for a in fft_returnA:
  A_points.append((round(a.real), round(a.imag)))
  print(a, end=" ")
print(A_points) # the returned 

for b in fft_returnB:
  B_points.append((round(b.real), round(b.imag)))
  # print(b, end=" ")
print(B_points)

C_points = pair_wise_mult(A_points, B_points)