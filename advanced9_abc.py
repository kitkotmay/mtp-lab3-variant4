from abc import ABC, abstractmethod
class Animal(ABC):
    """Абстрактный базовый класс животного."""
    def __init__(self, name):
        self.name = name
    @abstractmethod
    def speak(self):
        """Возвращает звук животного."""
        pass
    @abstractmethod
    def move(self):
        """Возвращает способ передвижения животного."""
        pass
class Dog(Animal):
    """Класс собаки."""
    def speak(self):
        return f"{self.name}: Гав!"
    def move(self):
        return f"{self.name} бежит."
class Cat(Animal):
    """Класс кошки."""
    def speak(self):
        return f"{self.name}: Мяу!"
    def move(self):
        return f"{self.name} идёт."
def main():
    animals = [
        Dog("Шарик"),
        Cat("Мурка"),
    ]
    for animal in animals:
        print(animal.speak())
        print(animal.move())
        print()
if __name__ == "__main__":
    main()
