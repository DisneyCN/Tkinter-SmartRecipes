import sqlite3
from sqlite3 import Error
# Ne conectam la baza de date]
conn = sqlite3.connect('SmartRecipeDatabase1.db')
 
# Creem un cursor cursor 
cursor = conn.cursor()

ingredients = ['potatoes','red peper','carrot','cerry tomatoes','banana']

# for ingredient in ingredients:
#     cursor.execute(f'''insert into Ingredients(inName) values('{ingredient}')''')

try:
    insertToTable = '''insert into Ingredients(inName) values(?)'''
    cursor.executemany(insertToTable,zip(ingredients)) 
except:
    pass

conn.commit()


cursor.execute('select * from Ingredients')
print(cursor.fetchall())
