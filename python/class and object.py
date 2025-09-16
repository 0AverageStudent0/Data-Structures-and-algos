class Person:
  name = "harry"
  occupation = "software dev"
  networth = 10
  def info(self):
    print(f"{self.name} is a {self.occupation}")
a=Person()
b=Person()


#print(a.name)
a.name = "sahil"
b.occupation ="chittad"
#print(a.name)
a.info()
b.info()