class Parent:
    """
    This is a parent class called Parent.
    """
    def __init__(self, name):
        self.name = name
    
    def hello(self):
        """
        This method prints a greeting message that includes the name attribute of the instance.
        """
        print(f"Hello, {self.name}!")
        
class Child(Parent):
    """
    This is a child class called Child that inherits from the Parent class.
    """
    def __init__(self, name, age, toy):
        """
        This is a constructor method for the Child class.
        It uses the super() function to call the constructor of the Parent class and pass the name parameter to it.
        It also initializes  new attributes called age and toy.
        """
        super().__init__(name)
        self.age = age
        self.toy = toy
    
    def hello(self):
        """
        This method overrides the hello method of the Parent class.
        It first calls the hello method of the Parent class using the super() function.
        It then prints a message that includes the age attribute and the toy attribute of the instance.
        """
        super().hello()
        print(f"You are {self.age} years old and your favorite toy is a {self.toy}.")
        
# Create a new instance of the Child class with name "Alice", age 7 and favorite toy.
child = Child("Tommy", 7, "Toy car")

# Call the hello method of the Child instance.
child.hello()
