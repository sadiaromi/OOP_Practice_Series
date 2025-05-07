class Dog:
    def __init__(self, name, breed):
        self.name = name      
        self.breed = breed

    def bark(self):
        print(f"{self.name} says: Woof! Woof!")

dog1 = Dog("Buddy", "Golden Retriever")
dog2 = Dog("Rocky", "German Shepherd")

dog1.bark()
dog2.bark()

print("Dog 1 Breed:", dog1.breed)
print("Dog 2 Breed:", dog2.breed)
