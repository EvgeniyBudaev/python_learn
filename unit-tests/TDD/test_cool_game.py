import unittest
import cool_game

class TestCoolGameFunction(unittest.TestCase):
  def test_greet(self):
    self.assertEqual(cool_game.greet('Jack', False), 'Hello Jack! How are you?')

  def test_greet_enemy(self):
    self.assertEqual(cool_game.greet('Ivan', True), 'Hello Ivan! I will kill you, bastard!') 

  def test_eat_burgers(self):
    self.assertEqual(cool_game.eat_burgers(3), 'Mmm! That was excelent!')

  def test_eat_too_much_burgers(self):
    self.assertEqual(cool_game.eat_burgers(4), 'Oh! I overate!') 

  def test_can_fly_batman(self):
    self.assertTrue(cool_game.can_fly('Batman'), 'Batman have to be able to fly')

  def test_can_fly_anyone(self):
    self.assertEqual(cool_game.can_fly('Bob'), False) 

  # def test_greet_enemy(self):
  #   with self.assertRaises(ValueError):  
  #     cool_game.greet2('Ivan', 'Bla-Bla')        


if __name__=='__main__':
  unittest.main()