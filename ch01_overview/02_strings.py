"""

    02_strings.py
    String handling basics

"""

# ------------------------------------
#       String Literal Notation
#
my_str = 'Python\'s great fun'
print(id(my_str))
my_str2 = "Python's great fun"
print(id(my_str2))
my_str = """Python's 
     great 
fun"""

my_str = 'Python\'s ' \
         'great ' \
         'fun!'
print(my_str)
print(id(my_str))

x = 10
y = x
print(x is y)


# ------------------------------------
#       String Random Access and Slicing
#
my_str = 'Python is fun'

print(my_str[0])         # 'P'

print(my_str[0:9])       # 'Python is'

print(my_str[:3])        # 'Pyt'

print(my_str[3:])        # 'hon is fun'

print(my_str[-3:])     # 'fun'


# ------------------------------------------
#        String Features and Methods
#
my_str = 'Python is '
new_str = my_str + 'fun'
print(new_str)

my_str = "Python is great and is super fun!"
my_list = my_str.split(' ')
print(my_list)

x = (1, 2, 3)

print(my_str.replace('is', 'is still', 1))   # yields: 'Python is still great'

places = ['First', 'Second', 'Third']
print(' | '.join(places))                    # Results in: 'First_Second_Third'


# ------------------------------------------
#        Additional String Methods
#
new_str = '    Whitespace will be removed.     '.strip()
print('X'+new_str+'X')

my_str = 'Python is great'
print(my_str.find('is'))      # returns 7
print(my_str.find('not'))     # returns -1

# ------------------------------------------
#        Using str.format()
#
s = 'It has been raining for {0:.2f} {1} and {0:.4f} {2}'
print(s)
new_str = s.format(40.001, 'days', 'nights')
print(new_str)

s = '{0} is over {age:0.2f} {1} old.'.format('Python', 'my_string', time='years', age=25)
print(s)


print('{0:10}{1:10}{income:>10,.2f}'.format('John', 'Smith', income=37_000))      # John      Smith             37
print('{0:-^20}'.format('hello'))                                    # center in a field-width of 20

name, age = 'Tom', 42
s = f'Hello {name}.  Ten years ago, you were {age - 10:.1f} years old.'
print(s)
