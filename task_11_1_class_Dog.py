class Dog:
    def __init__(self, name=None, age=None, master=None):
        self.__name = name
        self.__age = age
        self.__master = master

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        self.__age = age

    @property
    def master(self):
        return self.__master

    @master.setter
    def master(self, master):
        self.__master = master

    def bark(self):
        print('Woof!!!')

    def run(self):
        print('Running!!!')


dog1 = Dog()
dog1.name = 'Sharik'
dog1.age = 5
dog1.master = 'Alex'
print(f'Name of this dog is {dog1.name}, he is {dog1.age} years old, his master is {dog1.master}')
dog1.bark()
dog1.run()
