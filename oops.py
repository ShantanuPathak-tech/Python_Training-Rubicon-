class Student:
    # The __init__ method is the constructor used to initialize the attributes
    def __init__(self, name, rollno):
        self.name = name          # Instance variable for Student Name
        self.rollno = rollno      # Instance variable for Roll Number

    # Method to display the student details
    def display_info(self):
        print(f"Student Name: {self.name}")
        print(f"Roll Number:  {self.rollno}")


#  Creating Objects (Instances) of the Class 

# Creating the first student object
stud1 = Student("Alice Smith", 101)

# Creating the second student object
stud2 = Student("Bob Jones", 102)


#  Accessing Methods and Attributes 
stud1.display_info()
stud2.display_info()
 