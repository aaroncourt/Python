class Ninja:
    def __str__(self):
        return f'Person({self.first_name}, {self.pet})'

    def __repr__(self):
        return f'Person({self.first_name}, {self.pet})'

    def __init__(self, first_name, last_name, treats, pet_food, pet ): 
        self.first_name = first_name
        self.last_name= last_name
        self.pet = pet
        self.treats = treats
        self.pet_food = pet_food

    def walk(self):
        Pet.play(self.pet)
        return self

    def feed(self):
        Pet.eat(self.pet)
        return self

    def bathe(self):
        print(f'You bathe {self.pet.name}.')
        Pet.noise(self.pet)
        return self

    # def pet_info(self):
    #     print(f'Your {Pet.name}\'s health is {Pet.health} and energy is {Pet.energy}')

class Pet:
    energy = 50
    health = 50

    def __init__(self, name, type, tricks):
        self.name = name
        self.type = type
        self.tricks = tricks
        self.health = Pet.health
        self.energy = Pet.energy

    def sleep(self):
        self.energy += 25
        print(f'{self.name}\'s energy is now {self.energy}')
        return self

    def eat(self):
        self.energy += 5
        self.health += 10
        print(f'Your pet\'s health and enegry has increased by 10 and 5 and is now {self.health} and {self.energy}')
        return self

    def play(self):
        self.health += 5
        print(f'Your pet\'s health has increased by 5 and is now {self.health}')
        return self

    def noise(self):
        if self.type == 'dog':
            print('Bark!')
        elif self.type == 'cat':
            print('Meow!')
        else:
            print('Your pet is quiet during their bath.')


sparky = Pet('Sparky', 'dog', 'sit')
aaron = Ninja('Aaron', 'danger', 'dog_bones', 'dog_food', 'dog')\

aaron.pet = sparky
aaron.walk().feed().bathe()
sparky.eat().sleep()

