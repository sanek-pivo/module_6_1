class Animal:
    alive = True
    fed = False

    def __init__(self, name):
        self.alive = True
        self.fed = False
        self.name = name

    def eat(self, food):
        self.food = food
        if isinstance(food,Plant):
            if food.edible:
                print(f"{self.name} съел {food.name}")
                self.fed = True
            else:
                print(f"{self.name} не стал есть {food.name}")
                self.alive = False

class Plant:  # Создаём  родительский класс растений
    edible = False # (съедобность)
    def __init__(self, name):
        self.name = name

class Mammal(Animal):  # Создаём унаследованный класс животных - Травоядные
    def eat(self, food):
        if food.edible:
            print(f'{self.name} сьел {food.name}')
            self.alive = False

class Predator(Animal):  # Создаём унаследованный класс животных - Хищники
    def eat(self, food):
        if food.edible:
            print(f'{self.name} сьел {food.name}')
        else:
            print(f'{self.name} не стал есть  {food.name}')
            self.alive = False

class Flower(Plant):
    pass

class Fruit(Plant):   # Унаследованный класс растений - Фрукты
    edible = True

animal1 = Predator('Волк с Уолл-Стрит')   # Ввод названий животных и растений
animal2 = Mammal('Хатико')
plant1 = Plant('Цветик семицветик')
plant2 = Fruit('Заводной апельсин')

# Вывод результата
print(animal1.name)
print(plant1.name)

print(animal1.alive)
print(animal2.fed)

animal1.eat(plant1)
animal2.eat(plant2)
print(animal1.alive)
print(f' True')