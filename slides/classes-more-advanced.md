##  Classes - another example

    class Restaurant:
        def __init__(self, name, capacity):
            self.name = name
            self.capacity = capacity
            self.currentDiners = 0

        def addTable(self, patrons):
            self.currentDiners += patrons

        def atCapacity(self):
            self.currentDiners >= self.capacity
