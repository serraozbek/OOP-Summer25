class Animal:
    def __init__(self, name, group, number_of_legs, skills):
        self.name = name
        self.group = group
        self.number_of_legs = number_of_legs
        self.skills = skills

    def __str__(self):
        return f"{self.name} ({self.group}): {self.number_of_legs} legs, Skills: {', '.join(self.skills)}"

animals = [
    Animal("kitten", "mammals", 4, ["jumping", "climbing", "sleeping"]),
    Animal("Dog", "mammals", 4, ["running", "barking"]),
    Animal("Fox", "mammals", 4, ["learning fast", "hunting"]),
    Animal("Capybara", "mammals", 4, ["swimming and diving", "social behavior"]),
    Animal("Snake", "reptiles", 0, ["slithering", "hunting"])
]

for animal in animals:
    print(animal)