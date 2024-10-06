# class Person:
#     @staticmethod 
#     def work(work_hour):
#         print( 'Working hours :', work_hour)
# amy = Person ()
# amy.work(8)

class Student:
    def __init__(self, name):
        self.__name = name
        self.__score = {"Math": 0, "Physics": 0, "Chemistry": 0}
#私有方法
    def __add_subject(self, subject):
        self.__score[subject] = 0
# 公有方法
    def set_score(self, subject, score):
        if subject not in self.__score: 
            self.__add_subject(subject)
        self.__score[subject] = score
    def get_subject(self):
        for key in self.__score:
            print (key)

people=Student("Scofield")
people.set_score("chinese",10)
people.get_subject()

# 被繼承的類別 ->父類別
class Person: # 1
    def _init_(self, name, age, ID):
        self.name = name
        self.age = age
        self._ID = ID
def speak(self, sentence):
    return self.name + " says " + sentence
# 繼承 Person 的類別 -> 子類別
class Athlete(Person) : # 2
    def workout(self):
        return '%s goes to the gym to exercise.' % (self.name)
    
# 繼承 Person 的類別 -> 子類別
class Athlete (Person):
#覆寫建構子
    def _init_(self, name, age, ID, height):
        super()._init_(name, age, ID) # 1
        self.height = height
# 覆寫 speak 方法
    def speak(self, sentence):
        print("Athelete: ", super().speak(sentence)) # 2