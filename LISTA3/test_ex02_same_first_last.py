from ex02 import same_first_last            


def test_ex02():
  print ('Same_first_last')
  assert same_first_last([1, 2, 3]) == False
  assert same_first_last([1, 2, 3, 1]) == True
  assert same_first_last([1, 2, 1]) == True
  assert same_first_last([7]) == True
  assert same_first_last([]) == False
  assert same_first_last([7, 7]) == True


