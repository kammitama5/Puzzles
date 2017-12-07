def naive(a, b):
  x = a; y = b; 
  z = 0;
  while x > 0:
    z = z + y;
    x = x - 1;
  print z 
  return z 
  
naive(1,1) # 1 * 1 
naive(4,2) # 4 * 2
naive(4,1) # 4 * 1
naive(1,0) # 1 * 0

"""
Inductive step: 
If ab = xy + z before 
then ab = x' y' + z' after 
x' = x - 1, y' = y, z' = z + y 
x' y' + z' = (x - 1)(y) + (z + y)
           = xy - y + z + y 
           = xy + z 
           = ab
"""

"""
Ancient Egyptian vs Russian Peasant algorithm
def russian(a, b):
  x = a; y = b;
  z = 0; 
  while x > 0:
    if x % 2 == 1: (if remainder is 1, num is odd)
      z = z + y 
      y = y << 1 
      x = x >> 1
"""

print 17 >> 1 #8 subtracts 1 and halfs
print 6 >> 1 # halfs number 

"""
How many additions for russian(20, 7)
-> 2 
x   y   z 
20  7   0 
10  14  0 
5   28  0 
2   56  28 
1   112 28 
0   224 140
"""

