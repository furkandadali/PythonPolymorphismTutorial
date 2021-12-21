#Bu örnek bize bir miras uygulaması gösterecektir
#Ana sınıf olarak Polygon ve üçgen is buradan türetilecek alt sınıf olarak seçilmiştir

class Polygon:
     def __init__(self,no_of_sides):  #Yapıci (constructor)
          self.n=no_of_sides
          self.sides=[0 for i in range(no_of_sides)]

     def inputSides(self):
          self.sides=[float(input("Enter side: "+str(i+1)+":"))for i in range(self.n)]

     def dispSides(self):
          for i in range(self.n):
               print("Side",(i+1),"is",self.sides[i])
#Şimdi Polygon ana sınıfını kullanarak Triangle (Üçgen) sınıfını türetelim

class Triangle(Polygon):  #Bu satır Triangle sınıfının Polygon sınıfından türeyen alt bir sınıf olduğunu gösterir
     def __init__(self):
          Polygon.__init__(self,3)#genelde üst sınıf yapıcı fonksiyonda burada çağrılır, bu genelde üst sınıf ismi olabldiği
                                  #gibi super() fonksiyonu kullanılabilir (eğer tekil miras ise)
#Triangle sınıfı yukarıda Polygon sınıfında verilen üye fonksiyonlara otomatik olarak sahip olacaktır
     def alan(self):
          a,b,c=self.sides
          #alan hesaplanabilir
          s=(a+b+c)/2
          alan=(s*(s-a)*(s-b)*(s-c))**0.5
          print("Üçgenin Alanı:",alan)
#şimdi nesneleri yaratalım
t=Triangle()
t.inputSides()
print("Alan:",t.alan())
          
          
