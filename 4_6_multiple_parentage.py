class Person:
    def __init__(self, name, age):
        self.name, self.age = name, age

    def display_person_info(self):
        print(f'Person: {self.name}, {self.age}')


class Company:
    def __init__(self, company_name, location):
        self.company_name, self.location = company_name, location

    def display_company_info(self):
        print(f'Company: {self.company_name}, {self.location}')


class Employee(Person, Company):
    def __init__(self, name, age, company_name, location):
        super(Employee, self).__init__(name, age)
        Company.__init__(self, company_name, location)


emp = Employee('Jessica', 28, 'Google', 'Atlanta')
emp.display_person_info()
emp.display_company_info()
