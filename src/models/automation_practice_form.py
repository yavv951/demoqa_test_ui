import random

import attr
from faker import Faker

fake = Faker()


@attr.s
class PracticeFormPageModel:
    first_name: str = attr.ib(default=None)
    last_name: str = attr.ib(default=None)
    user_email: str = attr.ib(default=None)
    user_number: str = attr.ib(default=None)
    gender: str = attr.ib(default=None)
    hobbies: str = attr.ib(default=None)
    subjects: str = attr.ib(default=None)
    current_address: str = attr.ib(default=None)
    state: str = attr.ib(default=None)
    city: str = attr.ib(default=None)
    month: str = attr.ib(default=None)
    year: str = attr.ib(default=None)
    day: str = attr.ib(default=None)

    @classmethod
    def random(cls):
        return PracticeFormPageModel(first_name="Ivan",
                                     last_name="Ivanov",
                                     user_email="ivanov@mail.ru",
                                     user_number="9009999999",
                                     gender=random.choice(["Male", "Female", "Other"]),
                                     subjects=random.choice(["English", "Physics"]),
                                     hobbies=random.choice(["Sports", "Reading", "Music"]),
                                     state=random.choice(["Haryana"]),
                                     city=random.choice(["Karnal", "Panipat"]),
                                     current_address="2-юго-западная",
                                     month=random.choice(["1"]),
                                     year=random.choice(["2020"]),
                                     day=random.choice(["10"])
                                     )

