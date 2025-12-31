class Dog:
    species = "Dog"

    def __init__(self, breed, age):
        self.breed = breed
        self.age = age

    def display(self):
        print("Species:", Dog.species)
        print("Breed:", self.breed)
        print("Age:", self.age)


dog1 = Dog("Labrador", 3)
dog2 = Dog("German Shepherd", 5)

dog1.display()
dog2.display()
