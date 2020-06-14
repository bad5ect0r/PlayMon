import sqlite3
import play_scraper


db =  sqlite3.connect('db.db')
c = db.cursor()
app_array = []

c.execute("DROP TABLE IF EXISTS apps")
c.execute("CREATE TABLE apps(id INT, app_id TEXT, version TEXT)")

with open('apps.txt') as f:
    for index, line in enumerate(f):
        app = play_scraper.details(line.strip())
        app_array.append((index+1, app['app_id'], app['current_version']))

c.executemany("INSERT INTO apps VALUES(?, ?, ?)", app_array)

db.commit()
db.close()

