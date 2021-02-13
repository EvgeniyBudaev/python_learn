# Атрибуты класса - описывают свойства объекта
class Car:

  wheels_number = 4

  def __init__(self, name, color, year):
    self.name = name
    self.color = color
    self.year = year

mazda_car = Car(name = 'Mazda CX7', color = 'white', year = 2020)
print(mazda_car.name, mazda_car.color, mazda_car.year)    

bmw_car = Car('BMW X3', 'black', 2021)
print(bmw_car.name, bmw_car.color, bmw_car.year, bmw_car.wheels_number)

number_of_wheels_of_2_cars = Car.wheels_number * 2
print('number_of_wheels_of_2_cars: ', number_of_wheels_of_2_cars) # 8

# Создайте класс BlogPost с атрибутами user_name, text, number_of_likes. Создайте два объекта этого класса. После создания измените атрибут number_of_likes одного из объектов. Распечатайте атрибут number_of_likes каждого из объектов

class BlogPost:
    def __init__(self, user_name, text, number_of_likes):
      self.user_name = user_name
      self.text = text
      self.number_of_likes = number_of_likes

blogPost1 = BlogPost(user_name = 'Ivan', text = 'super man', number_of_likes = 'like')
blogPost2 = BlogPost(user_name = 'Petr', text = 'first', number_of_likes = 'like')
blogPost1.number_of_likes = 'dislike'
print(blogPost1.number_of_likes)
print(blogPost2.number_of_likes)     