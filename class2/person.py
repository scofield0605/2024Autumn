# Define the Person class
class Person:
#建構式
    def __init__(self, eyesColor, hairColor):
        self.eyesColor=eyesColor
        self.hairColor=hairColor
#美國人
    @classmethod 
    def american(cls):
        return cls("blue", "brown")
#台灣人
    @classmethod 
    def taiwanese(cls):
        return cls("black", "black")
    def introduce(self):
        print("My eyes is f} and my hair is f}.".format(self.eyesColor, self.hairColor))


amy = Person.american()
ben = Person.taiwanese()
amy.introduce() 
ben.introduce ()