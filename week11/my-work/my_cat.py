# Exercise 1 - complete
# class Kitten:
#     def __init__(self, name, age, coat_color):
#         self.name = name
#         self.age = age
#         self.coat_color = coat_color
#
# cat = Kitten('Gary', 12, 'black')
# print(cat.name, cat.age, cat.coat_color)

# Exercise 2 - complete
# class Kitten:
#     def __init__(self, name, age, coat_color):
#         self.name = name
#         self.age = age
#         self.coat_color = coat_color
#
#     def purr(self):
#         print(f'{self.name} purrs')
#
# cat = Kitten('Gary', 12, 'black')
# cat.purr()

# Exercise 3 - complete
# class Dog:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
# dog = Dog('Fido', 10)
# print(dog.name, dog.age)

# Exercise 4 - complete
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        print(f'{dog.name} barks')

dog = Dog('Fido', 10)
dog.bark()

# Challenge exercise 1 - complete
class Kitten:
    def __init__(self, name, age, coat_color):
        self.name = name
        self.age = age
        self.coat_color = coat_color

    def purr(self):
        print(f'{self.name} purrs')

    def meet(self):
        if isinstance(other, (Kitten, Dog)):
            print(f'{self.name} hisses at {other.name}')

cat = Kitten('Gary', 12, 'black')
other = Kitten('Stacey', 2, 'red')
cat.meet()
other = Dog('Toto', 4)
cat.meet()

# Challenge exercise 2 - complete
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        print(f'{dog.name} barks')

    def meet(self):
        if isinstance(other, Kitten):
            print(f'{self.name} barks at {other.name}')
        elif isinstance(other, Dog):
            print(f'{self.name} wags their tail at {other.name}')

dog = Dog('Fido', 10)
other = Kitten('Stacey', 2, 'red')
dog.meet()
other = Dog('Toto', 4)
dog.meet()