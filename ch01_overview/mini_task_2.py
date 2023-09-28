"""

       Mini-task 2 - Accessing sequences

"""
records = [
    ('John',  'Smith',   43, 'jsbrony@yahoo.com'),
    ('Ellen', 'James',   32, 'jamestel@google.com'),
    ('Sally', 'Edwards', 36, 'steclone@yahoo.com'),
    ('Keith', 'Cramer',  29, 'kcramer@sinotech.com')
]

# Display Sally Edwards age
print(records[2][2])

# Add a new record into records
tup = records[1] # ('Ellen', 'James',   32, 'jamestel@google.com')
my_list = list(tup)
my_list[0] = 'Jill'
tup = tuple(my_list)
print(type(tup))
print(tup)
records.insert(2, tup)
print(records)

# Display how many records you then have after this
print(len(records))

# Display how many fields are in the second record from the end record
print(len(records[-2]))

# Display how long Keith Cramer's email is
print(len(records[-1][3]))

list1 = [1, 2, 3]
tup1 = {'key1': 50}

# list2 = list1 + list(tup1)
list1.extend(tup1.values())
print(list1)

list2 = []
list2.append('Bob')
print(list2[0])