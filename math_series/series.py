def fibonacci(n):
  """
  The function should return the nth value in the fibonacci series. One parameter n -> number. Returns number
  """
  if n == 1:
    return 0 
  elif n == 2:
    return 1
  else:
    return fibonacci(n-2) + fibonacci(n-1)

def lucas(n) :
  """
  Function returns the value of the num within the lucas sequence for a given position (num)
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

def sum_series(n, first_num=0, second_num=1):
  """
  sum_series with one required parameter and two optional parameters. The required parameter will determine which element in the series to print.
  """
  if n == 1:
    return first_num
  elif n == 2:
    return second_num
  else:
    return sum_series(n-2,first_num, second_num) + sum_series(n-1, first_num,second_num)

