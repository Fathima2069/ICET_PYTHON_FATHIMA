class Student:
    # Method to set the attributes
    def get(self,rlno,name,totalmark):
        self.rlno=rlno  #instance  variable for roll number
        self.name=name  #instance variable for name
        self.totalmark=totalmark #Instance variable for total marks

    def disp(self): # Method to display the attributes
        print(f"Roll Number:{self.rlno}")
        print(f"Name:{self.name}")
        print(f"Total Marks:{self.totalmark}")

stud1=Student()# Create an object of the Student class
stud1.get(101,"Alice",85)# Call the get()method to set attributes
stud1.disp() # Call the disp()method to display attributes
