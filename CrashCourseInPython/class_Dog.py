class Dog(): # classes capitalized
    """A simple attempt to model a dog"""

    # init method runs automatically at each 'instance' creation
    # 'self' refers to the instance itself
    def __init__(self, name, age):
        """Initialize name and age attributes"""
        # variables accessed through instances are called attributes
        self.name = name
        self.age = age

    def sit(self):
        """simulate dog sitting in response to command"""
        print(self.name.title() + " is now sitting.")

    def roll_over(self):
        """Simulate rolling over in response to command"""
        print(self.name.title() + " rolled over!")

# make an instance (lower case) representing a specific dog
# will run the __init__ method Dog
my_dog = Dog('oliver', 3)
