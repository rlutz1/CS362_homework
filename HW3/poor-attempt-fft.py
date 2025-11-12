
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
