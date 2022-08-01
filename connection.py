import psycopg2


connection = psycopg2.connect('dbname= innocent')

cursor = connection.cursor()

cursor.execute(

    '''
        CREATE TABLE table1(
            id INTEGER PRIMARY KEY,
            completed BOOLEAN NOT NULL DEFAULT FALSE
        );
    '''
)


cursor.execute('INSERT INTO  table1(id,completed) VALUES(1,true);')

connection.commit()

connection.close()
cursor.close()