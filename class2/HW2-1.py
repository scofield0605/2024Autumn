class Movie:
    def __init__(self, title, author, genre):
        self.title = title
        self.author = author
        self.genre = genre

    def get_details(self):
        return f"Title: {self.title}, Author: {self.author}, Genre: {self.genre}"

    def change_genre(self, new_genre):
        self.genre = new_genre

    @classmethod
    def from_string(cls, movie_string):
        title, author, genre = movie_string.split(", ")
        return cls(title, author, genre)

    @classmethod
    def create_movie(cls, title, author, genre):
        return cls(title, author, genre)



movie1 = Movie.create_movie("Harry Potter", "JK Rowling", "Sci-Fi")
movie2 = Movie.from_string("Oppenheimer, Christopher Nolan, Based on true story")

print(movie1.get_details())  
movie2.change_genre("Historical Fiction")
print(movie2.get_details()) 