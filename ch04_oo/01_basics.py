"""

    01_basics.py
    A basic Python Class

"""


class Contact:
    def __init__(self, name='', address=''):
        self.name = name
        self.address = address

    def __str__(self):
        return self.name


c = Contact('John Smith', '123 Main St.')
d = Contact('John Smith', '123 Main St.')
print(c.name)
print(c, type(c))
c.name = 'Joe Jones'
print(c)
print(d)

c.foo = 'bar'
print(c.foo)
