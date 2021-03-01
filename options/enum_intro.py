# enum - перечисления
from enum import Enum
from enum import IntEnum
from enum import IntFlag

class TrafficLight(Enum):
  RED = 1
  YELLOW = 2
  GREEN = 3


print(TrafficLight.RED) # TrafficLight.RED
print(TrafficLight.RED.name) # RED
print(TrafficLight.RED.value) # 1

for el in TrafficLight:
  print('el: ', el)

# IntEnum
class Priority(IntEnum):
  LOW = 1
  NORMAL = 2
  HIGH = 3


print(Priority.LOW < Priority.NORMAL) # True 

# IntFlag
class Color(IntFlag):
  RED = 1
  GREEN = 2
  BLUE = 4

combination = Color.RED | Color.GREEN
print(combination) # Color.GREEN|RED 
print(Color.RED in combination) # True

# ===
# class Planet(Enum):
#   MERCURY = (3.303e+23, 2,4397e6)
#   EARTH = (5.976e+24, 6.37814e6)

#   def __init__(self, mass, radius):
#     self.mass = mass
#     self.radius = radius

#   @property
#   def surface_gravity(self):
#     G = 6.67300E-11
#     return G * self.mass / (self.radius * self.radius)



 