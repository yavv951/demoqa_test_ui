import random

import attr
from faker import Faker

fake = Faker()


@attr.s
class WebTablesPageModel:
    first_name: str = attr.ib(default=None)
    last_name: str = attr.ib(default=None)
    user_email: str = attr.ib(default=None)
    age: str = attr.ib(default=None)
    salary: str = attr.ib(default=None)
    department: str = attr.ib(default=None)

    @classmethod
    def random(cls):
        return WebTablesPageModel(first_name=fake.name(),
                                  last_name=fake.name(),
                                  user_email="ivanov@mail.ru",
                                  age=str(random.randint(10, 50)),
                                  salary=str(random.randint(10000, 50000)),
                                  department=random.choice(["Finance", "Gumanitar"])
                                  )
