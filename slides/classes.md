##  Classes

A definition of an object - something that contains attributes and functions to abstract away complexity

    class Person:
        def __init__(self, name)
            # A special function that creates new objects
            self.name = name

        def nameStartsWithT(self):
            return upper(self.name[0]) == "T"

    # Create object from class definition
    me = Person("Taylor")

    # Call Class function on object
    me.nameStartsWithT() # Returns True
