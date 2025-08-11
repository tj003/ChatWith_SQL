import sqlite3

## connect to sqllite

connection = sqlite3.connect("student.db")

## create a cursor object to insert record, create table

cursor = connection.cursor()

# create table

table_info = """

create table STUDENT(NAME VARCHAR(25), CLASS VARCHAR(25), SECTION VARCHAR(25), MARKS INT)

"""

# cursor.execute(table_info)

# Insert some more records

cursor.execute('''Insert into STUDENT values('Tushar','AI', 'A', '100')''')
cursor.execute('''Insert into STUDENT values('Karan','Java', 'A', '90')''')
cursor.execute('''Insert into STUDENT values('Shriyash','Python', 'B', '95')''')
cursor.execute('''Insert into STUDENT values('Sukant','Blockchain', 'A', '90')''')
cursor.execute('''Insert into STUDENT values('Sushant','AI', 'A', '85')''')

# Display all the records
print("The inserted records are")
data = cursor.execute('''Select*from STUDENT''')
for row in data:
    print(row)

connection.commit()
connection.close()