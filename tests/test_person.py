from person import Person
class Person:
    def test_can_create_person_1():
        person_1 = Person("John", 17, "Canada")
        assert person_1.name == "John"
        assert person_1.age == 17
        assert person_1.country == "Canada"

    def test_can_create_person_2():
        person_2 = Person("Maria", 25, "Spain")
        assert person_2.name == "Maria"
        assert person_2.age == 25
        assert person_2.country == "Spain"

    def __str__ (person_1):
        return f"{person_1.name} is {person_1.age} years old and is from {person_1.country}."

    def __str__ (person_2):
        return f"{person_2.name} is {person_2.age} years old and is from {person_2.country}."
        person_2 = Person("Maria", 25, "Spain")
        assert str(person_2) == "Maria is 25 years old and is from Spain."

    def test_person_1_cannot_vote():
        person_1 = Person("John", 17, "Canada")
        assert (person_1.can_vote()) # False

    def test_person_2_can_vote():
        person_2 = Person("Maria", 25, "Spain")
        assert (person_2.can_vote()) # True