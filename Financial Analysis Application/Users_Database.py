import sqlite3

class User_Database:

    def __init__(self, givenDatabaseRef: str):
            # stores location of database as an attribute
            self.databaseRef = givenDatabaseRef


    def create_users_table(self):
            db = sqlite3.connect(self.databaseRef)
            db.execute("""
                       CREATE TABLE IF NOT EXISTS Users_table (
                       User_ID INTEGER PRIMARY KEY AUTOINCREMENT, 
                       Email_Address TEXT UNIQUE NOT NULL, 
                       Hashed_Password TEXT NOT NULL, 
                       Phone_Number TEXT NOT NULL);
                       """)
            db.commit()
            db.close()


    def insert_into_users_table(self, email_address, hashed_password, phone_number):
            try:
                db = sqlite3.connect(self.databaseRef)
                db.execute("PRAGMA foreign_keys = ON;")
                db.execute("INSERT INTO Users_Table (Email_Address, Hashed_Password, Phone_Number"
                           ") VALUES (?, ?, ?)",
                           (email_address, hashed_password, phone_number))
                db.commit()
                return True
                # flags up if the customer ain't unique
            except sqlite3.IntegrityError:
                return False
            finally:
                db.close()


    def read_all(self, tableName: str):
            db = sqlite3.connect(self.databaseRef)
            data = db.execute("SELECT * FROM " + tableName)
            result = data.fetchall()
            db.close()
            return result


    def verify_login(self, email_address, hashed_password):
        db = sqlite3.connect(self.databaseRef)
        data = db.execute("SELECT hashed_password FROM Users_Table WHERE Email_Address = ?",
                          (email_address,))
        result = data.fetchone()
        db.close()
        if result is None:
             return False
        else:
            database_hashed_password = result[0]

            return hashed_password == database_hashed_password


    def print_all(self, tableName: str):
            data = self.read_all(tableName)
            for line in data:
                for item in line:
                    print(str(item), end=", ")
                print()

    def display_table(self):
            self.print_all("Users_Table")

    def delete_table(self):
            db = sqlite3.connect(self.databaseRef)
            db.execute("DROP TABLE IF EXISTS Users_Table")
            db.commit()
            db.close()




if __name__ == "__main__":
    Database = User_Database("./Users.db")  # pass in the location for database instantiating the class
    Database.create_users_table()
    Database.display_table()