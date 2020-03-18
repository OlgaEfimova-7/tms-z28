from random import randint


class Book:
    def __init__(self, name=None, author=None, amount_of_pages=None):
        self.__name = name
        self.__author = author
        self.__amount_of_pages = amount_of_pages

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def author(self):
        return self.__author

    @author.setter
    def author(self, author):
        self.__author = author

    @property
    def amount_of_pages(self):
        return self.__amount_of_pages

    @amount_of_pages.setter
    def amount_of_pages(self, amount_of_pages):
        self.__amount_of_pages = amount_of_pages

    def generator_of_page(self):
        print(f'Generated page is {randint(1, self.__amount_of_pages)}')

    def generator_of_quote(self, name_of_the_file):
        with open(name_of_the_file, 'r') as my_file:
            amount_of_str = 0
            while True:
                line = my_file.readline()
                if not line:
                    break
                amount_of_str += 1
        with open(name_of_the_file, 'r') as my_file:
            for index, line in enumerate(my_file.readlines()):
                if index + 1 == randint(1, amount_of_str):
                    break
            return f'Generated string is {index + 1} : {line}'

    def end_of_the_book(self):
        print('Сongratulations! You did it!')


book1 = Book()
book1.name = 'Woe from wit'
book1.author = 'Griboedov'
book1.amount_of_pages = 110
print(book1.generator_of_quote('Woe from wit.txt'))
