def fibonacci(n):
  """
  Fibonacci string
  """
  if n < 0:
    print("Incorrect input")

  elif n == 0:
    return 0
  
  elif n == 1 or n == 2:
    return 1
  
  else:
    return fibonacci (n-1) + fibonacci (n-2)

# print(fibonacci(4))

def lucas(n) :
  """
  Lucas string
  """
  a = 2
  b = 1

  if (n == 0) :
    return a
  
  for i in range(2, n + 1) :
    c = a + b
    a = b
    b = c
  return b
  

# print(lucas(9))

def sum_series(n, first_num=0, second_num= 0):
  """
  Sum_series goes here...
  """
  if first_num == 0 and second_num == 1:
    return fibonacci(n)
  elif first_num == 2 and second_num ==1:
    return lucas(n)





















# def wacky_series(n, first_num=0, second_num=1):
#   """
#   Docstring goes here...
#   """
#   if first_num == 0 and second_num == 1:
#     return fibonacci(n)
#   elif first_num == 2 and second_num ==1:
#     return lucas(n)

# def fibonacci(n):
#   print('first is 0, second is 1')

# def lucas(n):
#   print('first is 2, second is 1')

# def sum(n):
#   print('first is 10, second is 12')

# wacky_series(5)