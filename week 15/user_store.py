import sqlite3


class UserStore:
    def __init__(self, db_path):
        self.db_path = db_path
        self.init_db()

    def init_db(self):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id TEXT PRIMARY KEY,
                name TEXT NOT NULL,
                email TEXT NOT NULL
            )
        """)
        conn.commit()
        conn.close()

    def _get_conn(self):
        conn = sqlite3.connect(self.db_path)
        conn.row_factory = sqlite3.Row
        return conn

    def load(self):
        conn = self._get_conn()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users")
        rows = cursor.fetchall()
        conn.close()
        return [dict(row) for row in rows]

    def save(self, user):
        conn = self._get_conn()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO users (id, name, email) VALUES (?, ?, ?)",
            (user["id"], user["name"], user["email"])
        )
        conn.commit()
        conn.close()

    def find_by_id(self, user_id):
        conn = self._get_conn()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE id = ?", (user_id,))
        row = cursor.fetchone()
        conn.close()
        if row:
            return dict(row)
        return None

    def update_user(self, user_id, updated_data):
        # build the SET clause from whatever fields came in
        fields = ", ".join(f"{k} = ?" for k in updated_data.keys())
        values = list(updated_data.values()) + [user_id]
        conn = self._get_conn()
        cursor = conn.cursor()
        cursor.execute(f"UPDATE users SET {fields} WHERE id = ?", values)
        conn.commit()
        affected = cursor.rowcount
        conn.close()
        return affected > 0

    def delete_user(self, user_id):
        conn = self._get_conn()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM users WHERE id = ?", (user_id,))
        conn.commit()
        affected = cursor.rowcount
        conn.close()
        return affected > 0
