class person:
    def __init__ (self,n,o):
    
        self.name =n
        self.occ = o
    def info(self):
        print(f"{self.name} is a {self.occ}")

a = person("sahil","dev")
b = person("nan","driver")
print("hey my name is",a.name)
a.info()

print("hey my name is",b.name)
b.info()