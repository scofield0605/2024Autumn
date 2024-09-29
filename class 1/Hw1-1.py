class Movie:
    def __init__(self, title, author, type):
        self.title = title
        self.author = author
        self.type = type

    def get_details(self):
        return f"Title: {self.title}, Author: {self.author}, Genre: {self.type}"

    def change_type(self, new_type):
        self.type = new_type

# Create two book objects
movie1 = Movie("harry potter", "JK Rowling", "Sci-Fi")
movie2 = Movie("Oppenhimer", "Christopher Nolan", "Base on true story")

print(movie1.get_details())
movie2.change_type("Historical Fiction")
print(movie2.get_details())