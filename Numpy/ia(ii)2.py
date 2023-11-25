class Job:
    def __init__(self, title, salary):
        self.title = title
        self.salary = salary
    
    def get_info(self):
        return f"Job: {self.title}, Salary: ${self.salary}"

class Person:
    def __init__(self, name, age, job):
        self.name = name
        self.age = age
        self.job = job  # Composition: Person has-a Job
    
    def get_info(self):
        return f"Name: {self.name}, Age: {self.age}\n{self.job.get_info()}"

# Create a Job object
software_engineer = Job("Software Engineer", 80000)

# Create a Person object with a Job
john = Person("John Doe", 30, software_engineer)

# Get information about John
print(john.get_info())
