from db_connection import get_database_connection

cursor, db = get_database_connection()


cursor.execute("show tables from expenses")
tables = cursor.fetchall()
print(tables)

cursor.execute("select * from expenses.expense")
rows = cursor.fetchall()
print(rows)


cursor.execute("show tables from parameters")
tables = cursor.fetchall()
print(tables)

cursor.execute("select * from expenses.parameters")
rows = cursor.fetchall()
print(rows)
