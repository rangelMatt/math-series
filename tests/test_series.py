from math_series.series import fibonacci, lucas, sum_series

def test_fib_1():
  actual = fibonacci(1)
  expected = 0
  assert actual == expected

def test_fib_2():
  actual = fibonacci(3)
  expected = 1
  assert actual == expected

def test_fib_3():
  actual = fibonacci(5)
  expected = 3
  assert actual == expected

def test_luc_1():
  actual = lucas(0)
  expected = 2
  assert actual == expected

def test_luc_2():
  actual = lucas(3)
  expected = 4
  assert actual == expected

def test_luc_3():
  actual = lucas(10)
  expected = 123
  assert actual == expected

def test_sum_series1():
  actual = sum_series(3,2,1)
  expected = 3
  assert actual == expected

def test_sum_series_1():
  actual = sum_series(3,2,1)
  expected = 3
  assert actual == expected

def test_sum_series_2():
  actual = sum_series(5,2,1)
  expected = 7
  assert actual == expected

def test_sum_series_3():
  actual = sum_series(10,2,1)
  expected = 76
  assert actual == expected