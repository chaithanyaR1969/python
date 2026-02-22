class heroine:
    def __init__(self):
        self.name="anushka"
        self.age=46
        self.numOfMovies=23
    def act(self):
        print("she is a good actress")
h1=heroine()
print(h1.name)
print(h1.age)
print(h1.numOfMovies)
h1.act()
h1.height=6
print(h1.height)
h1.age=47
print(h1.age)
del h1.numOfMovies
print(h1.numOfMovies)
