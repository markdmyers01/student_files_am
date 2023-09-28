"""

    09_namedtuples.py
    Creating the classic namedtuple.

"""
from collections import namedtuple

header = ['first', 'last', 'age', 'email']
# c = namedtuple('Contact', header)


class Contact:
    def __init__(self, first, last, age, email):
        self.first = first
        self.last = last
        self.age = age
        self.email = email

    def __str__(self):
        return f'{self.first} Age: {self.age}'

c = Contact

print(type(c))

records = [
    c('John',  'Smith',   43, 'jsbrony@yahoo.com'),
    c('Ellen', 'James',   32, 'jamestel@google.com'),
    c('Sally', 'Edwards', 36, 'steclone@yahoo.com'),
    c('Keith', 'Cramer',  29, 'kcramer@sintech.com')
]
records.sort(key=lambda one_rec: one_rec.age, reverse=True)

records[0].age = 55

print(records)
for record in records:
    print(type(record))
    # print(record.last, record.age)
    print(record)
