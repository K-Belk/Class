from distutils.log import error
import psycopg2
import csv

class DB:

    def __init__(self) -> None:
        self.conn = None
        self.cur = None
        

    def initialize_connection(self):
        self.conn = psycopg2.connect("dbname=chicago_salaries user=kevinlbelk")
        self.cur = self.conn.cursor()
        
    def close_connection(self):
        self.cur.close()
        self.conn.close()

    def create_table(self):
        self.cur.execute("DROP TABLE IF EXISTS employees CASCADE")
        self.cur.execute("CREATE TABLE employees (id serial PRIMARY KEY, first_name varchar(30), middle_initial varchar(10), last_name varchar(30),  job_title varchar(100), full_or_part_time varchar(1), department varchar(30), annual_salary decimal);")
        

    def clean_data(self, row):
        cleaned = {}
        name_split = row['Name'].split(',  ')
        first_name_split = name_split[1].split(' ')
        cleaned['first_name'] = first_name_split[0]
        if len(first_name_split) > 1:
            cleaned['middle_initial'] = first_name_split[1]
        else:
            cleaned['middle_initial'] = ''
        cleaned['last_name'] = name_split[0]
        cleaned['job_title'] = row['Job Titles']
        cleaned['full_or_part_time'] = row['Full or Part-Time']
        cleaned['department'] = row['Department']
        if row['Salary or Hourly'] == 'Salary':
            cleaned['annual_salary'] = float(row['Annual Salary'])
        else:
            cleaned['annual_salary'] = round(float(row['Typical Hours']) * float(row['Hourly Rate']) * 50,2)        
        return cleaned

    def read_csv(self):
        with open('Current_Employee_Names__Salaries__and_Position_Titles.csv') as csvfile:
            reader = csv.DictReader(csvfile)
            for r in reader:
                cleaned = self.clean_data(r)
                self.insert_data(cleaned)

    def insert_data(self, data):
        self.cur.execute("INSERT INTO employees (first_name, middle_initial, last_name, job_title, full_or_part_time, department, annual_salary) VALUES (%s, %s, %s, %s, %s, %s, %s)", (data['first_name'], data['middle_initial'], data['last_name'], data['job_title'], data['full_or_part_time'], data['department'], data['annual_salary']))

    def main(self):
        try:
            self.initialize_connection()
            self.create_table()
            self.read_csv()
            self.conn.commit()
        except error:
            print("Ahh shit, someting didn't work")
            print(error)
        finally:
            self.close_connection()

test = DB()
test.main()

# # Query the database and obtain data as Python objects
# >>> cur.execute("SELECT * FROM test;")
# >>> cur.fetchone()
# (1, 100, "abc'def")

# # Make the changes to the database persistent
# >>> conn.commit()

# # Close communication with the database
# >>> cur.close()
# >>> conn.close()