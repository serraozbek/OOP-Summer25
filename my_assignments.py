#1. Create a variable called "city" that stores the name of the city you live in. Then print: "I live in <city>".

city = "Warsaw" 
print("I live in", city)



# 2. Create a list of 3 things you would take to a deserted island. Then print second item.

items = ["lighter", "knife", "sleeping bag"]
print(items[1])  



# 3. Create a list of 5 numbers. Use a for loop to print only the numbers that are greater than 10.

numbers = [20, 12, 3, 18, 7]
for number in numbers:
    if number > 10:
        print(number)



# 4. Create a dictionary called "laptop" with keys: "brand", "model", and "year". Print the model.

laptop = {
    "brand": "Asus",
    "model": "Zenbook",
    "year": 2023
}
print(laptop["model"]) 

# 5. Create a function called greet_user(name) that prints "Hello, <name>!" when called.

def greet_user(name):
    print(f"Hello, {name}!")

greet_user("Serra")  



# 6. Create a class called Car with attributes "brand" and "speed". Add a method that says if the car is fast (>100 km/h).

class Car:
    def __init__(self, brand, speed):
        self.brand = brand
        self.speed = speed

    def is_fast(self):
        if self.speed > 100:
            print(f"{self.brand} is fast.")
        else:
            print(f"{self.brand} is not fast.")

my_car = Car("BMW", 120)
my_car.is_fast() 



# 7. Create a list of temperatures (in Celsius). Write a loop to convert each one to Fahrenheit and print it.

celsius_temps = [0, 20, 30]
for temp in celsius_temps:
    fahrenheit = (temp * 9/5) + 32
    print(f"{temp}°C = {fahrenheit}°F")



# 8. Write a function that takes a list of numbers and returns the average of the numbers.

def average(numbers):
    return sum(numbers) / len(numbers)

print(average([10, 20, 30]))  



# 9. Create a class called Song with attributes "title" and "artist". Add a method play() that prints "<title> by <artist> is playing".

class Song:
    def __init__(self, title, artist):
        self.title = title
        self.artist = artist

    def play(self):
        print(f"{self.title} by {self.artist} is playing")

my_song = Song("Cloud Nine", "Gemini")
my_song.play() 

# 10. Create a dictionary of 3 countries and their capitals. Then use input() to let the user type a country name and print its capital.

capitals = {
    "Poland": "Warsaw",
    "Turkey": "Ankara",
    "Korea": "Seul"
}

country = input("Enter a country: ")
print("Capital:", capitals.get(country, "Country not found"))