import _sqlite3

conn = _sqlite3.connect('test123.db')
cursor = conn.cursor()

print("Connected")

cursor.execute('''
        Create table if not exists test(id integer primary key autoincrement, cases text, age integer)
    '''
)

#cursor.execute('''Insert into test values(1,\'case 1\' , 12)''')
cursor.execute('''Insert into test(cases,age) values(\'case 2\' , 13)''')
cursor.execute('''Select * from test''')
results = cursor.fetchall()
conn.commit()

print(results)

