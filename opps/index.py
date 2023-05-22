class Person:
    def __init__(self,name, occ,salary):
      print('hey i am a person')
      self.name = name
      self.occ = occ
      self.salary = salary

    def info(self):
        print(f"{self.name} is a {self.occ}")
        
    def multiple_salary (self):
        return self.salary * 3    


a = Person('Akash','Developer',100);

a.info()
print(a.multiple_salary())
