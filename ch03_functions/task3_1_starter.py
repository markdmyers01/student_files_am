"""

      task3_1_starter.py   -   Modules and Functions

      This was the solution from task2_1.py.  If you run it, you will see it
      currently runs as is.

      Work from this file or replace it with your own previous solution.

      Your task: Create a load_data() function in the ch03_functions/baseball.py file
                 that loads the data from the two provided files and returns a data structure
                 that can be displayed in this file.


      Step 1. Either use this file or make a copy of your own task2_1_starter.py file.
              Create a load_data() function in baseball.py

      Step 2. Migrate the code that reads from the files into the load_data() function.

      Step 3. Remove unnecessary code from this file now.

      Step 4. Import baseball.py into this file.
              (You should be able to say "import baseball" if the current directory is listed
               in your sys.path.  Then baseball.load_data() should work)
              Invoke the load_data() function from that file.

      Step 5. Test your solution to ensure it works.

"""
import os
from ch03_functions import baseball

working_dir = '../resources/baseball/'
people_filename = 'People.csv'
salaries_filename = 'Salaries.csv'

input_year = 0


sal_filepath = os.path.join(working_dir, salaries_filename)
people_filepath = os.path.join(working_dir, people_filename)


year_str = '2016' # input('Enter a year (1985-2016): ')
top_sals = baseball.load_data(sal_filepath, people_filepath, year_str)
# print(baseball.what_is_my_name)


how_many = 10
print_header = ['Name', 'Salary', 'Year']
print('{0:35}{1:>20}{2:>10}'.format(*print_header))
print('{0:-<75}'.format(''))

for salary_info in top_sals[:how_many]:
    first_name = salary_info[0]
    last_name = salary_info[1]
    name = first_name + ' ' + last_name
    salary = f'${salary_info[2]:,}'
    year = salary_info[3]

    print(f'{name:35}{salary:>20}{year:>10}')

sal_tot = f'${sum([salary_info[2] for salary_info in top_sals[:how_many]]):,}'
print('{0:-<75}'.format(''))
print('{0:>35}{1:>20}'.format('Total Salary:', sal_tot))