#connect to the database and create a table


import sqlite3
conn=sqlite3.connect('table1.db')
print('opened database successfully')
conn.execute('''create table company
            (id int primary key NOT NULL,
            name  text NOT NULL,
            age int NOT NULL,
            address char(50),
            salary real )''')
print('table created successfully')
conn.close()

