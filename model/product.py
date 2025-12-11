from database.db import Database

class ProductModel:
    def __init__(self):
        self.db = Database()

    def add_product(self, name, category, price, stock):
        conn = self.db.connect()
        cursor = conn.cursor()

        query = """
            INSERT INTO food_beverage (name, category, price, stock)
            VALUES (%s, %s, %s, %s)
        """

        cursor.execute(query, (name, category, price, stock))
        conn.commit()
        conn.close()

    def get_all(self):
        conn = self.db.connect()
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM food_beverage")
        rows = cursor.fetchall()

        conn.close()
        return rows

    def get_by_id(self, product_id):
        conn = self.db.connect()
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM food_beverage WHERE id=%s", (product_id,))
        row = cursor.fetchone()

        conn.close()
        return row

    def update_product(self, product_id, name, category, price, stock):
        conn = self.db.connect()
        cursor = conn.cursor()

        query = """
            UPDATE food_beverage 
            SET name=%s, category=%s, price=%s, stock=%s
            WHERE id=%s
        """
        cursor.execute(query, (name, category, price, stock, product_id))

        conn.commit()
        conn.close()

    def delete_product(self, product_id):
        conn = self.db.connect()
        cursor = conn.cursor()

        cursor.execute("DELETE FROM food_beverage WHERE id=%s", (product_id,))
        conn.commit()
        conn.close()
