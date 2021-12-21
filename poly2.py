#polymorphism miras uygulamasıyla birlikte
from math import pi #genel bir değişken
class Shape:
     def __init__(self,name):
          self.name=name
     def alan():
          pass
     def __str__(self):
          return self.name

class Square(Shape):
     def __init__(self,a):
          super().__init__("Square")
          self.a=a
     def alan(self):
          return self.a*self.a

class Circle(Shape):
     def __init__(self,radius):
          super().__init__("Daire")#üst sınıf constructor çağrıldı
          self.radius=radius
     def alan(self):
          return pi*self.radius*self.radius
class Rectangle(Shape):
     def __init__(self,b,c):
          super().__init__("Rectangle")
          self.b=b
          self.c=c
     def alan(self):
          return self.b*self.c
     

d=Square(10)
print("Square Alan:",d.alan())
c=Circle(10)
print("Circle Alan:",c.alan())
r=Rectangle(8,5)
print("Rectangle Alan:",r.alan())
     
               
