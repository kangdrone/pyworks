# Person2 클래스 정의

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return "이름 : {0}, 나이 : {1}".format(self.name, self.age)

class Employee(Person):
    def __init__(self, name, age, empid):
        super().__init__(name, age)    # 부모 멤버는 super()로 받는다
        self.empid = empid

    def __str__(self):
        return "이름 : {0}, 나이 : {1}, 사번 : {2}".format(self.name, self.empid, self.age)

emp1 = Employee("콩쥐", 25, 1001)
print(emp1)

emp2 = Employee("팥쥐", 25, 1002)
print(emp2)

"""
print(emp1.empid)
print(emp1.age)
print(emp1.name)
"""