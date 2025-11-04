class Person:
    def __init__(self, name):
        self.name = name


class Employee(Person):
    def __init__(self, name, salary):
        super().__init__(name)
        self.salary = salary
        self.task = None

    def get_salary(self):
        return self.salary

    def assign_task(self, task):
        self.task = task
        print(f"{self.name} has been assigned the task: {self.task}")


class Student(Person):
    def study(self, subject):
        print(f"{self.name} is studying {subject}")


# Main program to test the classes
if __name__ == '__main__':
    # Create an Employee object
    emp = Employee("Alice", 3000)
    emp.assign_task("Prepare monthly report")
    print(f"{emp.name}'s salary: ${emp.get_salary()}")

    # Create a Student object
    stu = Student("Bob")
    stu.study("Mathematics")

    # Show that substitution still works logically
    people = [emp, stu]
    for p in people:
        print(f"Person: {p.name}")
