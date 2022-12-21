import discogs_client
from discogs_client import Client, Condition, Status, Sort
# Discogs client documentation: https://github.com/joalla/discogs_client
# https://python3-discogs-client.readthedocs.io/en/latest/

import json
import time

import sqlite3
from sqlite3 import Error
# sqlite3 documentation: https://docs.python.org/3/library/sqlite3.html

conn = sqlite3.connect("techno.db")
c = conn.cursor()
# c.execute("CREATE TABLE IF NOT EXISTS releases(id, title, artists, country, url, img, year)")

c.execute("""CREATE TABLE IF NOT EXISTS releases(
            "id" INTEGER PRIMARY KEY,
            "title" TEXT,
            "artists" BLOB,
            "country" TEXT,
            "url" TEXT,
            "img" TEXT,
            "year" TEXT
            )
    """)

# User Authorization
d = discogs_client.Client('my_user_agent/1.0', user_token='nWEpLxojZVxFJSUMJGWaPPVtykJNrdnevMQmnQES')

release_id = None
release_title = None
release_artists = []
release_country = None
release_url = None
release_img = None
release_year = None

results = d.search(style='Techno')

print(len(results))

for release in results:

    time.sleep(1)

    # print(release.data.keys())

    # print(d.release(release.id).data)
    
    release_id = release.id
    print(release_id)

    release_title = d.release(release.id).title
    print(release_title)

    for artist in d.release(release.id).artists:
        release_artists.append(artist.name)
        print(release_artists)

    release_country = d.release(release.id).country
    print(release_country)

    release_url = f"https://www.discogs.com/release/{release.id}"
    print(release_url)

    release_img = d.release(20017387).images[0]['uri']
    print(release_img)

    release_year = release.year
    print(release_year)

    print('-----')

    # Check if a release with this ID is already in the database.

    current_row = None

    current_row = c.execute(f"""
        SELECT * FROM releases
        WHERE id = {release_id}
    """)

    current_row = c.fetchone()

    print(current_row)

    if current_row == None:

        print('The row does not exist')

        c.execute("INSERT INTO releases VALUES(?, ?, ?, ?, ?, ?, ?)",(release_id, release_title, str(release_artists), release_country, release_url, release_img, release_year))
    
        conn.commit()

    else:

        print('The row exists.')

    # If not already in the database, add it there.

c.close()
conn.close()