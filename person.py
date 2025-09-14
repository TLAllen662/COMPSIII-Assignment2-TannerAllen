class Person:
    # Delete pass and write your code here
    def __init__ (self, name, age, country):
        self.name = name
        self.age = age
        self.country = country
    
    def can_vote (self):
        return self.age >= 18
    

    def __str__ (self):
        return f"{self.name}, is {self.age} years old and lives in {self.country}."
person_1 = Person("Alice", 30, "USA")
print(person_1)
print(person_1.can_vote()) # True
person_2 = Person("Bob", 17, "Canada")
print(person_2)
print(person_2.can_vote()) # False