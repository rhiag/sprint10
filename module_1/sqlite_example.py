import sqlite3
import queries as q

#Step1: Connect to DB
#Check spelling of DB.Sqlite creates a new DB if it doesnt find the DB file name

connection = sqlite3.connect('rpg_db.sqlite3')

#Step2: Create a cursor. Cursor is like middleman between you and DB

cursor = connection.cursor()

#Step3: Write our query
#Moved to queries.py


#Step4: Execute query on the cursor and fetch the results aka pulling the results

results = cursor.execute(q.SELECT_ALL).fetchall()


if __name__ == '__main__':
    print(results[:5])

