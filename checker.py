import pushover
import sqlite3
import play_scraper


db = sqlite3.connect('db.db')
c = db.cursor()
c.execute("SELECT * FROM apps")
rows = c.fetchall()

for row in rows:
    row_id = row[0]
    app_id = row[1]
    version = row[2]

    app = play_scraper.details(app_id)
    current_version = app['current_version']
    
    if current_version != version:
        title = '{} Released a New Version of {}!'
        message = '{} => {}'

        pushover.send_message(
            title.format(app['developer'], app['title']),
            message.format(version, current_version)
        )

        c = db.cursor()
        c.execute("UPDATE apps SET version=? WHERE id=?", (current_version, row_id))
        c.commit()

db.close()

