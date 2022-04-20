from series import fibonacci, lucas, sum_series

def test_one():
  actual = fibonacci(0)
  expected = 0
  assert actual == expected

def test_two():
  actual = lucas(0)
  expected = 2
  assert actual == expected

def test_three():
  actual = sum_series(0,2,0)
  expected = None
  assert actual == expected

