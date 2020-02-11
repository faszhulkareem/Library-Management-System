import sqlite3


class Database:
    def __init__(self, db):
        self.conn = sqlite3.connect(db)
        self.cur = self.conn.cursor()
        self.cur.execute(
            "CREATE TABLE IF NOT EXISTS books (id INTEGER PRIMARY KEY, bookName text, bookID text, author text, publisher text, edition text)")
        self.conn.commit()
        self.cur.execute("CREATE TABLE IF NOT EXISTS stock (id INTEGER PRIMARY KEY,'book name' TEXT,count	INTEGER)")
        self.conn.commit()
        self.cur.execute("CREATE TABLE IF NOT EXISTS student (id INTEGER PRIMARY KEY,studentName TEXT, registerNo TEXT,dept TEXT)")
        self.conn.commit()

    def fetch_book(self):
        self.cur.execute("SELECT * FROM books")
        rows = self.cur.fetchall()
        return rows

    def insert_book(self, bookName, bookID, author,  publisher, edition):
        self.cur.execute("INSERT INTO books VALUES (NULL, ?, ?, ?, ?,?)",
                         (bookName, bookID, author,  publisher, edition))
        self.conn.commit()

    def remove_book(self, id):
        self.cur.execute("DELETE FROM books WHERE bookID=?", (id,))
        self.conn.commit()

    def update_book(self, id, bookName, bookID, author,  publisher, edition):
        self.cur.execute("UPDATE books SET bookName = ?, bookID = ?, author = ?, publisher = ?, editon=? WHERE bookID = ?",
                         (bookName, bookID, author,  publisher, edition, id))
        self.conn.commit()

    def fetch_student(self, regno):
        self.cur.execute("SELECT * FROM student WHERE registerNo =?",(regno,))
        self.conn.commit()
        row = self.cur.fetchall()
        return row

    def __del__(self):
        self.conn.close()

#
# db = Database('database.db')
# db.insert("web technology", "0001", "jackson",  "oxford", "second")
