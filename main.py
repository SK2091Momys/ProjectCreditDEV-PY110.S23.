import json
from random import randint, choice, uniform
from typing import Optional

from faker import Faker

from conf import MODEL


def get_model():
    model = MODEL
    return model


def get_title():
    with open('books.txt', encoding='UTF-8') as books:
        title = choice(books.readlines())
    return title


def get_year():
    year = randint(1900, 2023)
    return year


def get_pages():
    pages = randint(500, 1000)
    return pages


def get_isbn_13():
    fake = Faker()
    isbn = fake.isbn13()
    return isbn


def get_rating():
    rating = round(uniform(0.0, 5.0), 2)
    return rating


def get_price():
    price = round(uniform(400.0, 1200.0), 2)
    return price


def get_author():
    fake_ = Faker()
    fake_name = fake_.name()
    return fake_name


def generator_book(size_dict: Optional[int] = 1) -> dict:
    pk = 1
    for _ in range(1, size_dict+1):
        dict_book = {"model": get_model(),
                     "pk": pk,
                     "fields": {
                         'title': get_title(),
                         'year': get_year(),
                         'pages': get_pages(),
                         'isbn13': get_isbn_13(),
                         'rating': get_rating(),
                         'price': get_price(),
                         'author': get_author()}}
        yield dict_book
        # with open("books.json", "a", encoding="UTF-8") as books:
        #     json.dump(dict_book, books, ensure_ascii=False, indent=4)
        pk += 1





if __name__ == '__main__':
    book = generator_book(100)
    with open("books.json", "w", encoding="UTF-8") as books:
        json.dump([i for i in book], books, ensure_ascii=False, indent=4)