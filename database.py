import sqlite3
 
# Ne conectam la baza de date]
conn = sqlite3.connect('SmartRecipeDatabase1.db')
 
# Creem un cursor cursor 
cursor = conn.cursor()
 
# Creem tabel
cursor.execute('''create table if not exists Roles (
    roleId integer primary key autoincrement
    ,roleName varchar(10) not null unique
)''')
 
# Creem tabel
cursor.execute('''create table if not exists Auth (
    userId integer primary key autoincrement
    ,userName varchar(25) unique not null
    ,userPassword varchar(30) not null
    ,userEMail varchar(50) unique not null
    ,roleId integer not null DEFAULT 2
    ,foreign key (roleId) references Roles(roleId)
)''')
 
# Creem tabel
cursor.execute('''create table if not exists Ingredients(
	inId integer primary key autoincrement
    ,inName varchar(50) unique
)''')
 
 
# Creem tabel
cursor.execute('''create table if not exists RecipeNames(
	recipeId integer primary key autoincrement
    ,recipeName varchar(50) unique
    ,recipeDescribe text
)''')
 
cursor.execute('''create table if not exists Measures(
    measureId integer primary key autoincrement
    ,measureName varchar(15) not null unique
)''')

# Creem tabel
cursor.execute('''create table if not exists Meats(
	meatId integer primary key autoincrement
    ,recipeId integer not null
    ,inId integer not null unique
    ,measureId integer not null unique
    ,inCant decimal(6,2)
    ,foreign key (recipeId) references RecipeNames(recipeId)
    ,foreign key (inId) references Ingredients(inId)
    ,foreign key (measureId) references Measures(measureId)
)''')
 
 
# Creem tabel
cursor.execute('''create table if not exists FavoriteMeats(
	meatId integer not null unique
    ,userId integer not null
    ,foreign key (meatId) references Meats(meatId)
    ,foreign key (userId) references Auth(userId)
)''')
 
 
# Salvam schimbarile
conn.commit()

# Insert dates in tabel Roles
cursor.execute("insert or ignore into Roles (roleName) values ('Admin')")
cursor.execute("insert or ignore into Roles (roleName) values ('User')")
cursor.execute("insert or ignore into Roles (roleName) values ('Guest')")

# Insert dates in tabel Auth
cursor.execute("insert or ignore into Auth (userName, userPassword, userEmail, roleId) values ('admin', 'admin','admin@admin.com','1')")
# Set roleId as 1 for data in table Auth with userName = 'admin'
cursor.execute("update Auth set roleId = 1 where userName = 'admin'")



# Create view that vill select all information about recipes from table FavoriteMeats that will contain name of recipe, recipeDecribe
cursor.execute('''create view if not exists FavoriteMeatsView as
    select meatId, recipeName, recipeDecribe from FavoriteMeats inner join RecipeNames on FavoriteMeats.recipeId = RecipeNames.recipeId;
''')


cursor.execute('''create view if not exists UsersView as
    select userName,userPassword from Auth;
''')

cursor.execute('''create view if not exists UserView as
    select userName from Auth;
''')



conn.commit()

cursor.execute('''select * FROM RecipeNames''')
rows= cursor.fetchall()
for row in rows:
    print(row[1])

