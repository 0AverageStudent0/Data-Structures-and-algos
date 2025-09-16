class Student:

    def __init__(self,name : str,rollnumber : int,marks : list[int]):
        self.name = name
        self.rollnumber = rollnumber
        self.marks = marks
    
    def display_details(self):
        print(f"name : {self.name}")
        print(f"rollnum : {self.rollnumber}")
        print(f"marks : {self.marks}")
    
    def calc_marks(self):
        total = sum(self.marks)
        percentage = total / len(self.marks)
        return percentage

student1 = Student("sahil",201,[30,20,10,20,40])
student2 = Student("rasheed",202,[40,40,40,40,40])

student2.display_details()
print(student2.calc_marks())