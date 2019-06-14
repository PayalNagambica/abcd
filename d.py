#data inserting in a table


import sqlite3
conn=sqlite3.connect('table1.db')
print('opened database successfully')
conn.execute('''insert into company (id,name,age,address,salary)
             values(1,'zaheena',21,'hyd',20000.00)''')
conn.execute('''insert into company (id,name,age,address,salary)
             values(2,'chandini',23,'vij',30000.00)''')
conn.commit()
print("records created successfully")
conn.close()