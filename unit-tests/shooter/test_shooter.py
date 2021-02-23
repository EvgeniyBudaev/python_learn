# setUp() - runs before each test method. Установить
# tearDown() - runs after each test method. Уничтожить
import unittest
from shooter import Shooter

class TestShooter(unittest.TestCase):
  mock_data = [] 
  
  def setUp(self):
    self.jake = Shooter('Jake')
    self.mock_data = [1, 2, 3]

  def tearDown(self):
    self.mock_data = []  

  def test_get_cash(self):
    # jake = Shooter('Jake')
    self.jake.get_cash(500)
    self.assertEqual(self.jake.money, 1500)

  def test_greet(self):
    # jake = Shooter('Jake')
    self.assertEqual(self.jake.greet(), "Hello! How are you?")  


if __name__=='__main__':
  unittest.main()    