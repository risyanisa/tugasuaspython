import mysql.connector

class Database:
    def __init__(self):
        self.config = {
            "host": "localhost",
            "user": "root",
            "password": "",
            "database": "uas"
        }
        self.create_table()

    def connect(self):
        return mysql.connector.connect(**self.config)

    def create_table(self):
        conn = self.connect()
        cursor = conn.cursor()

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS food_beverage (
                id INT AUTO_INCREMENT PRIMARY KEY,
                name VARCHAR(100) NOT NULL,
                category VARCHAR(50) NOT NULL,
                price DOUBLE NOT NULL,
                stock INT NOT NULL
            )
        """)

        conn.commit()
        conn.close()
