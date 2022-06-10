import json
import sqlite3


sqlite_con = sqlite3.connect('../db.sqlite3')
cursor = sqlite_con.cursor()

with open('posts.json') as jsonFile:
    jsonObject = json.load(jsonFile)
    jsonFile.close()


for post in jsonObject:
    userId = post['userId']
    id = post['id']
    title = post['title']
    body = post['body']


    insert_posts = """INSERT OR IGNORE INTO api_post (userId, id, title, body) VALUES (?,?,?,?)"""

    with sqlite_con as connection:
        cursor.execute(insert_posts, [userId, id, title, body])
        connection.commit()
