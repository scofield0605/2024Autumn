from abc import ABC, abstractmethod

# Abstract class
class Sport(ABC):
    @abstractmethod
    def play(self):
        pass

# Child class for Basketball
class Basketball(Sport):
    def play(self):
        return "Playing basketball takes 2 hours."

# Child class for Baseball
class Baseball(Sport):
    def play(self):
        return "Playing baseball takes 4 hours."

# Creating instances of each child class
basketball = Basketball()
baseball = Baseball()

# Printing the results
print(basketball.play())
print(baseball.play())