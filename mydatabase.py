from sqlite3 import connect

class Database:
    db = None

    @staticmethod
    def connectDatabase():
        Database.db = connect("number.db")
        cursor = Database.db.cursor()
        cursor.execute(
            "CREATE TABLE IF NOT EXISTS users(id integer PRIMARY KEY, email text  NOT NULL, password text NOT NULL)"
        )
        cursor.execute(
            "CREATE TABLE IF NOT EXISTS fact_table(id integer PRIMARY KEY, email text  NOT NULL, fact text NOT NULL)"
        )
        Database.db.commit()
        print("Connected")

    @staticmethod
    def insertdata(email,password):
        sql = "INSERT INTO users (email, password) VALUES(?,?)"
        val = (f"{email}", f"{password}")
        cursor =  Database.db.cursor()
        cursor.execute(sql,val)
        Database.db.commit()
        print("Inserted")

    @staticmethod
    def isValid(email):
        sql = f"SELECT * FROM users where email='{email}' "
        cursor = Database.db.cursor()
        cursor.execute(sql)
        result = cursor.fetchall()
        print(result)
        if (result):
            return True
        else:
            return False

    @staticmethod
    def isExist(email, password):
        sql = f"SELECT * FROM users where email='{email}' and password = '{password}'"
        cursor = Database.db.cursor()
        cursor.execute(sql)
        result = cursor.fetchall()
        print(result)
        if(result):
            return True
        else:
            return False

    @staticmethod
    def insertFact(email,fact):
        sql = "INSERT INTO fact_table (email, fact) VALUES(?,?)"
        val = (f"{email}", f"{fact}")
        cursor =  Database.db.cursor()
        cursor.execute(sql,val)
        Database.db.commit()
        print("Inserted")

    @staticmethod
    def getFact(email):
        sql = f"SELECT * FROM fact_table where email='{email}' "
        cursor = Database.db.cursor()
        cursor.execute(sql)
        result = cursor.fetchall()
        return result
