class Article:
    author = ""
    title = ""
    content = ""
    likes = 0
    
    def __str__(self):
        return self.title
    
    def summary(self):
        return self.content[:15] # slice of first 15 chars


# creating objects
a1 = Article()
a1.author = "John"
a1.title = "Python is awesome"
a1.content = "Some content will be here soon"
a1.likes = 10

a2 = Article()
a2.author = "John Cena"
a2.title = "WWE is awesome"
a2.content = "Some content will be here soon"
a2.likes = 100

a3 = Article()
a3.author = "John Doe"
a3.title = "World is awesome"
a3.content = "Some content will be here soon"
a3.likes = 1000

print("Our articles are:")
print(a1)
print(a1.summary())
print(a2)
print(a2.summary())
print(a3)
print(a3.summary())