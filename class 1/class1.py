class Person:
    def __init__(self, name, age, favorite_food):
        self.name = name
        self.age = age
        self.favorite_food = favorite_food
    
    # Define the introduce method using def
    def introduce(self):
        print(f"我是 {self.name}，我今年 {self.age} 歲，最喜歡吃 {self.favorite_food}。")
    
    # Define the shout method using def
    def shout(self, content):
        print(f"我大喊：「{content}」")

amy = Person ("Amy", 15, "Apple")
amy. introduce ()
amy. shout("我討厭看牙醫！")