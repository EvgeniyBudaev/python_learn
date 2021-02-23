import unittest
import upper

class TestStringMethods(unittest.TestCase):
  def test_one_word(self):
    text = 'hello!'
    result = upper.upper_text(text)
    self.assertEqual(result, 'HELLO!')


if __name__=='__main__':
  unittest.main()    