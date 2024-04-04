### Часть 1: Создание базового класса Animal



class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def make_sound(self):
        print(f"{self.name} makes a sound.")

    def eat(self):
        print(f"{self.name} is eating.")




### Часть 2: Наследование и подклассы



class Bird(Animal):
    def make_sound(self):
        print(f"{self.name} chirps.")


class Mammal(Animal):
    def make_sound(self):
        print(f"{self.name} grunts.")


class Reptile(Animal):
    def make_sound(self):
        print(f"{self.name} hisses.")




### Часть 3: Полиморфизм



def animal_sound(animals):
    for animal in animals:
        animal.make_sound()




### Часть 4: Композиция в классе Zoo



class Zoo:
    def __init__(self):
        self.animals = []
        self.staff = []

    def add_animal(self, animal):
        self.animals.append(animal)

    def add_staff(self, staff_member):
        self.staff.append(staff_member)




### Часть 5: Классы сотрудников



class ZooKeeper:
    def feed_animal(self, animal):
        print(f"{animal.name} has been fed.")


class Veterinarian:
    def heal_animal(self, animal):
        print(f"{animal.name} has been healed.")




### Дополнительные функции: Сохранение и загрузка состояния зоопарка


import pickle


def save_zoo(zoo, filename):
    with open(filename, 'wb') as f:
        pickle.dump(zoo, f)


def load_zoo(filename):
    with open(filename, 'rb') as f:
        zoo = pickle.load(f)
    return zoo




### Пример использования:

if __name__ == "__main__":
    zoo = Zoo()
    animal_1 = Mammal("Elephant", 10)
    keeper = ZooKeeper()
    vet = Veterinarian()

    zoo.add_animal(animal_1)
    zoo.add_staff(keeper)
    zoo.add_staff(vet)

    animal_sound(zoo.animals)  # Демонстрация полиморфизма

    # Дополнительные функции
    save_zoo(zoo, 'my_zoo.pickle')  # Сохранение состояния зоопарка
    loaded_zoo = load_zoo('my_zoo.pickle')  # Загрузка состояния зоопарка

    # Проверка после загрузки
    animal_sound(loaded_zoo.animals)