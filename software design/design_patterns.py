# Design Patterns Cheat Sheet


# 1. SINGLETON PATTERN
class Singleton:
    _instance = None

    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            cls._instance = cls()
        return cls._instance


# Usage
singleton_instance = Singleton.get_instance()


# 2. FACTORY PATTERN
class Dog:
    def speak(self):
        return "Woof!"


class Cat:
    def speak(self):
        return "Meow!"


class AnimalFactory:
    @staticmethod
    def get_animal(type):
        if type == "dog":
            return Dog()
        elif type == "cat":
            return Cat()
        raise ValueError("Unknown animal type")


# Usage
animal = AnimalFactory.get_animal("dog")
animal.speak()


# 3. STRATEGY PATTERN
class AddStrategy:
    def execute(self, a, b):
        return a + b


class SubtractStrategy:
    def execute(self, a, b):
        return a - b


class Context:
    def __init__(self, strategy):
        self.strategy = strategy

    def execute_strategy(self, a, b):
        return self.strategy.execute(a, b)


# Usage
add_strategy = Context(AddStrategy())
result = add_strategy.execute_strategy(2, 3)


# 4. OBSERVER PATTERN
class Observer:
    def update(self, message):
        print(message)


class Subject:
    def __init__(self):
        self.observers = []

    def register(self, observer):
        self.observers.append(observer)

    def notify_all(self, message):
        for observer in self.observers:
            observer.update(message)


# Usage
subject = Subject()
observer = Observer()
subject.register(observer)
subject.notify_all("Hello")


# 5. DECORATOR PATTERN
def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("Something before the function is called.")
        result = func(*args, **kwargs)
        print("Something after the function is called.")
        return result

    return wrapper


@my_decorator
def say_hello():
    print("Hello!")


# Usage
say_hello()


# 6. ADAPTER PATTERN
class OldClass:
    def specific_request(self):
        return "OldClass specific request"


class Adapter:
    def __init__(self, old_class):
        self.old_class = old_class

    def request(self):
        return self.old_class.specific_request()


# Usage
adapter = Adapter(OldClass())
adapter.request()


# 7. COMPOSITE PATTERN
class Component:
    def operation(self):
        pass


class Leaf(Component):
    def operation(self):
        print("Leaf")


class Composite(Component):
    def __init__(self):
        self.children = []

    def add(self, component):
        self.children.append(component)

    def operation(self):
        for child in self.children:
            child.operation()


# Usage
composite = Composite()
leaf1 = Leaf()
leaf2 = Leaf()
composite.add(leaf1)
composite.add(leaf2)
composite.operation()

# TIPS
# - Choose the right pattern based on your specific problem and context.
# - Understand the trade-offs of each pattern.
# - Avoid overusing design patterns; simplicity is key.
