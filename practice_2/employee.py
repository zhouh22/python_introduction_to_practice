class Employee:
    def __init__(self, last_name, first_name, salary):
        self.last_name = last_name
        self.first_name = first_name
        self.salary = salary

    def give_raise(self, salary_raise=5000):
        self.salary += salary_raise
        return self.salary
