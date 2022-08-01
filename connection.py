import psycopg2

connection = psycopg2.connect('dbname=innocent')

cursor = connection.cursor()

cursor.execute('DROP TABLE IF EXISTS table1;')

cursor.execute('''
  CREATE TABLE table1 (
    id INTEGER PRIMARY KEY,
    completed BOOLEAN NOT NULL DEFAULT False
  );
''')

cursor.execute('INSERT INTO table1 (id, completed) VALUES (%s, %s);', (1, True))

SQL = 'INSERT INTO table1 (id, completed) VALUES (%(id)s, %(completed)s);'

data = {
  'id': 2,
  'completed': False
}
cursor.execute(SQL, data)

connection.commit()

connection.close()
cursor.close()