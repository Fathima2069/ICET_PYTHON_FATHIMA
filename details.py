class Student:
    def get(self):# Method to set the attributes by reading input from the user
        self.rlno=int(input("Enter Roll Number:"))
        self.name=input("Enter Name:")
        self.totalmark=float(input("Enter Total Marks:"))
    def disp(self): # Method to display the attributes
        print("\nStudent Details:")
        print(f"Roll Number:{self.rlno}")
        print(f"Name:{self.name}")
        print(f"Total Marks:{self.totalmark}")

stud1=Student()# Create an object of the Student class
stud1.get()# Call the get()method to set attributes
stud1.disp() # Call the disp()method to display attributes

