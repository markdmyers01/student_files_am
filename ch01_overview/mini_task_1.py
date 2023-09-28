"""

       Mini-task 1 - f-strings and slicing

       Task: Display the following output given the string below:
            OS: Windows NT 10.0

"""
ua = 'Mozilla/5.0 (Windows NT 10.0)'

# put your solution here
start = ua.find('(') + 1
end = ua.find(')')
print(start, end)
print('OS: ' + ua[start: end])