"""
Russian expressed recursively
"""

def rec_russian(a, b):
  if a == 0: return 0 
  if a % 2 == 0: return 2 * rec_russian(a/2, b)
  return b + (2 * rec_russian((a-1)/2, b))
  
print(rec_russian(2,2))

"""
T(a) = 
if a = 0, 1 
else if a is even, 3 + T(a/2)
else 3+T((a-1)/2)

recurrence relation: 3[log2 a] + 4
"""
