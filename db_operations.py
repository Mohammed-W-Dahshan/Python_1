import sqlite3

class Students:
    def __init__(self):
        global conn,cur
        try:
            conn = sqlite3.connect("Database/AppDB")
            cur = conn.cursor()
            print("Success Connect")
        except sqlite3.Error as e:
            print("Error: %s" %e)

    def insert_std(self,fname,lname,age,email):
        global conn,cur
        try:
            sql = '''Insert Into students(fname,lname,age,email) Values(?,?,?,?)'''
            cur.execute(sql,(fname,lname,age,email))
            conn.commit()
            return "Insert Done"
        except sqlite3.Error as e:
            print("Error: %s" % e)

    def get_all_std(self):
        global conn,cur
        try:
            cur.execute("Select * From students")
            rows = cur.fetchall()
            return rows
        except sqlite3.Error as e:
            print("Error: %s" % e)

    def update_attr(self,id,at,val):
        global conn,cur
        try:
            cur.execute('''UPDATE students SET {} = ? WHERE s_id = ?'''.format(at),(val,id))
            conn.commit()
            return "Update Done"
        except sqlite3.Error as e:
            print("Error: %s" % e)

    def delete_std(self,id):
        global conn,cur
        try:
            cur.execute('''DELETE FROM students WHERE s_id = ?''',(id,))
            conn.commit()
            return "Delete Done"
        except sqlite3.Error as e:
            print("Error: %s" % e)

