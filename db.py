import sqlite3


db_name = "blog.db"
conn = None
cursor = None

def open():
    global conn,cursor
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
def close():
    cursor.close()
    conn.close()

def getCategories():
    open()
    cursor.execute("SELECT * FROM category")
    result = cursor.fetchall()
    close()
    return result
def getPosts():
    open()
    cursor.execute("SELECT * FROM post")
    result = cursor.fetchall()
    close()
    return result
def GetPostsInCategory(id):
    open()
    cursor.execute("SELECT * FROM post WHERE category_id == ?", [id])
    result = cursor.fetchall()
    close()
    return result
def GetCategoriesById(id):
    open()
    cursor.execute("SELECT name FROM category WHERE id == ?", [id])
    result = cursor.fetchone()
    close()
    return result
def addPost(category_id, text):
    open()
    cursor.execute('INSERT INTO post (category_id, text) VALUES (?,?)', [category_id,text])
    conn.commit()
    close()
def GetCategoriesByQuantity():
    open()
    cursor.execute("SELECT count(*) FROM post group by category_id")
    result = cursor.fetchall()
    close()
    return result
def deletePost(id):
    open()
    cursor.execute("DELETE FROM post WHERE id ==?", [id])
    conn.commit()
    close()
def getPost(id):
    open()
    cursor.execute("SELECT * FROM post WHERE id == ?", [id])
    result = cursor.fetchone()
    close()
    return result