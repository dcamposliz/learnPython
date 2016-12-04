# python 3
# mysql
# pymysql

import pymysql


"""
	SOURCE
	~~~~~~

		https://www.tutorialspoint.com/python/python_database_access.htm

	DEPENDENCIES TO THIS PROJECT
	~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

		# FIRST:

			- INSTALL MYSQL GLOBALLY
			- CREATE A USER WITH ALL PERMISSIONS

				Here is some help: 
					https://www.digitalocean.com/community/tutorials/how-to-create-a-new-user-and-grant-permissions-in-mysql

			- Install pymysql module for Python 3

		# SECOND, CREATE A TABLE

			CREATE TABLE EMPLOYEE(
				ID INT NOT NULL AUTO_INCREMENT,
				FIRST_NAME varchar(255),
				LAST_NAME varchar(255),
				AGE INT,
				SEX varchar(255),
				INCOME INT,
				PRIMARY KEY (ID)
			);
"""

###########################################################
# DATABASE CONNECTION
###########################################################

# declaring arguments for database connection
host = "localhost"
user = "sql_user"
password = "password"
database = "TESTDB"

# open database connection
db = pymysql.connect(host, user, password, database)

# prepare a cursor object using cursos() method
cursor = db.cursor()

# execute SQL query using execute() method
cursor.execute("SELECT VERSION()")

# fetch a single row using fetchone() method
data = cursor.fetchone()

print("Database version :", str(data))

# disconnect from server
db.close()

###########################################################
# CREATING A DATABASE
###########################################################

# declaring arguments for database connection
host = "localhost"
user = "sql_user"
password = "password"
database = "TESTDB"

# open database connection
db = pymysql.connect(host, user, password, database)

# prepare a cursor object using cursor() method
cursor = db.cursor()

# drop table if it already exists using the execute() method
cursor.execute("DROP TABLE IF EXISTS EMPLOYEE_2")

# create table as per requirement
sql_2 = """CREATE TABLE EMPLOYEE_2 (
			FIRST_NAME CHAR(20) NOT NULL,
			LAST_NAME CHAR(20),
			AGE INT,
			SEX CHAR(1),
			INCOME FLOAT
)"""

cursor.execute(sql_2)

# disconnect from server
db.close()

###########################################################
# INSERT OPERATION
###########################################################

# declaring arguments for database connection
host = "localhost"
user = "sql_user"
password = "password"
database = "TESTDB"

# open database connection
db = pymysql.connect(host, user, password, database)

# prepare a cursor object using cursos() method
cursor = db.cursor()

# prepare SQL query to insert a record into the database
sql_3 = """INSERT INTO EMPLOYEE_2(FIRST_NAME,
			LAST_NAME, AGE, SEX, INCOME)
			VALUES ('Mac', 'Mohan', 20, 'M', 2000)"""

try:
	# Execute the SQL command
	cursor.execute(sql_3)
	# Commit your changes in the database
	db.commit()
except:
	# Rollback in case there is any error
	db.rollback()

# disconnect from server
db.close()

# declaring a person object with the hopes of inputing its attribute data into the database
person = {
	"first_name": "David",
	"last_name" : "Campos",
	"age" : 26,
	"sex" : "M",
	"income" : 5000
}

# declaring arguments for database connection
host = "localhost"
user = "sql_user"
password = "password"
database = "TESTDB"

# open database connection
db = pymysql.connect(host, user, password, database)

# prepare a cursor object using cursos() method
cursor = db.cursor()

# prepare SQL query to insert a record into the database
sql_4 = """INSERT INTO EMPLOYEE_2(FIRST_NAME,
			LAST_NAME, AGE, SEX, INCOME)
			VALUES ('David', 'Campos', 26, 'M', 5000)"""

try:
	# Execute the SQL command
	cursor.execute(sql_4)
	# Commit your changes in the database
	db.commit()
except:
	# Rollback in case there is any error
	db.rollback()

# disconnect from server
db.close()


###########################################################
# READ OPERATION
###########################################################
"""
	Once a database connection has been established, you are ready to make queries to such database. You can either use the `fetchone()` or `fetchall()` methods, depending on how much data we are looking to fetch.

		fetchone():

			it fetches the next row of a query result set. A result set is an object that is returned when a cursor object is used to query a table.

		fetchall():

			it fetches all the rows in a result set. If some rows have already been extracted from the result set, then it retrieves the remaining rows from the result set.

		rowcount:

			This is a read-only attribute and returns the number of rows that were affected by an execute() method.
"""
# declaring arguments for database connection
host = "localhost"
user = "sql_user"
password = "password"
database = "TESTDB"

# open database connection
db = pymysql.connect(host, user, password, database)

# prepare a cursor object using cursos() method
cursor = db.cursor()

# prepare SQL query to SELECT data from database
sql_5 = """SELECT * FROM EMPLOYEE_2
			WHERE FIRST_NAME = 'DAVID'"""

try:
	# execute the SQL command
	cursor.execute(sql_5)
	# fetch all the rows in a list of lists
	results = cursor.fetchall()
	for row in results:
		fname = row[0]
		lname = row[1]
		age = row[2]
		sex = row[3]
		income = row[4]
		# now print fetched result
		print("First name:", fname, ", ",lname, ", ",age, ", ",sex, ", ",income)
except:
	print("Error: unable to fetch data.")

# disconnect from server
db.close()


###########################################################
# UPDATE OPERATION
###########################################################

# declaring arguments for database connection
host = "localhost"
user = "sql_user"
password = "password"
database = "TESTDB"

# open database connection
db = pymysql.connect(host, user, password, database)

# prepare a cursor object using cursos() method
cursor = db.cursor()

#prepare SQL to update required records
sql_6 = """UPDATE EMPLOYEE_2 SET FIRST_NAME = 'Sarah' WHERE FIRST_NAME = 'Mac'"""

sql_7 = """UPDATE EMPLOYEE_2 SET LAST_NAME = 'Seagrave' WHERE LAST_NAME = 'Mohan'"""

sql_8 = """UPDATE EMPLOYEE_2 SET AGE = '22' WHERE AGE = '20'"""

sql_9 = """UPDATE EMPLOYEE_2 SET SEX = 'F' WHERE FIRST_NAME = 'Sarah'"""

sql_10 = """UPDATE EMPLOYEE_2 SET INCOME = 0 WHERE FIRST_NAME = 'Sarah'"""

sql_array = [sql_6, sql_7, sql_8, sql_9, sql_10]

for seq in sql_array:
	try: 
		# Execute the SQL command
		cursor.execute(seq)
		# commit your changes in the database
		db.commit()
	except:
		# rollback in case there is any error
		db.rollback()

#disconnect from server
db.close()


###########################################################
# DELETE OPERATION
###########################################################
# declaring arguments for database connection
host = "localhost"
user = "sql_user"
password = "password"
database = "TESTDB"

# open database connection
db = pymysql.connect(host, user, password, database)

# prepare a cursor object using cursos() method
cursor = db.cursor()

# prepare SQL to delete Erik's record cuz he a fag
sql_7 = """DELETE FROM EMPLOYEE WHERE FIRST_NAME ='Erik'"""

try: 
	# Execute the SQL command
	cursor.execute(seq)
	# commit your changes in the database
	db.commit()
except:
	# rollback in case there is any error
	db.rollback()

#disconnect from server
db.close()

###########################################################
# PERFORMING TRANSACTIONS
###########################################################
"""
Transactions are a mechanism that ensures data consistency. Transactions have the following four properties:

	Atomicity:

		Either a transaction completes or nothing at all.

	Consistency:

		A transaction must start in a consistent state and leave the system in a consistent state.

	Isolation:

		Intermediate results of a transaction are not visible ourside the currect transaction.

	Durability:

		Once a transaction was committed, the effects are persistent, even after system failure.
"""

# prepare SQL query to DELETE required records
sql_8 = "DELETE FROM EMPLOYEE_2 WHERE AGE > 30"

try:
	# Execute the SQL command
	cursor.execute(sql_8)
	# Commit your changes in the database
	db.commit()
except:
	# Rollback in case there is any error
	db.rollback()

###########################################################
# COMMIT OPERATION
###########################################################
"""
Commit is the operation that gives a green signal to the database to finalize changes. After this operation nochange can be reverted back.

Here is a simple example to call commit method:

	db.commit()

And that's it for committing stuff to the database.
"""
###########################################################
# ROLLBACK OPERATION
###########################################################
"""
If you are not satisfied with one or more of the changes and you want to revert back those changes completely, then use rollback() method.

Here is a simple example to call rollback() method.

	db.rollback()

Yay!
"""
###########################################################
# DISCONNECTING DATABASE
###########################################################
"""
To disconnect database connection, use close() method.

	db.close()

If the connection to a database is closed by the user with the close() method, any outstanding transactions are rolled back by the database. However, instead of depending on any database lower level implementation details, your application would be better off calling commit or rollback explicitly.
"""
###########################################################
# HANDLING ERRORS
###########################################################
"""
There are many sources of errors. A few examples are syntax error in an executed SQL statement, a connection failure, or calling the fetch method for an already canceled or finished statement handle.

Here are a few errors you may encounter:

	Warning:

		Used for non-fatal issues. Must subclass StandardError.

	Error:

		Base class for errors. Must subclass StandardError.

	IntefaceError:

		Used for errors in the database module, not the database itself. Must subclass Error.

	DatabaseError:

		Used for errors in the database. Must subclass Error.

	DataError:

		Subclass of DatabaseError that refers to errors in the data.

	OperationalError:

		Subclass of DatabaseError that refers to errors such as the loss of a connection to the database. These errors are generally outside of the control of the Python scripter.

	IntegrityError:

		Subclass of DatabaseError for situations that would damage the relational integrity, such as uniqueness constaints or foreign keys.

	InternalError:

		Subclass of DatabaseError that refers to errors internal to the databse module, such as a cursor no longer being active.

	ProgrammingError:

		Subclass of DatabaseError that refers to errors such as a bad table name and other things that can safely be blamed on you.

	NotSupportedError:

		Subclass of DatabaseError that refers to trying to call unsupported functionality.














