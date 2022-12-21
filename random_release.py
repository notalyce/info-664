# import config
import pandas as pd
import schedule
import time
import discogs_client
import os
# Discogs client documentation: https://github.com/joalla/discogs_client
# https://python3-discogs-client.readthedocs.io/en/latest/

# User Authorization using config file
# d = discogs_client.Client('my_user_agent/1.0', user_token = config.api_token)

# User Authorization using GitHub workflow secrets
d = discogs_client.Client('my_user_agent/1.0', user_token = os.environ['API_TOKEN'])

# csv file name
filename = "release_data_styles.csv"

# filter and clean CSV data

df = pd.read_csv(filename)
df = df[df['style'].str.contains('Techno', na=False)]
df.dropna(inplace = True)
df.drop_duplicates(inplace = True)

# select one column
df = df.sample()

# print(df)

random_release_id = df['release_id'].values[0]
print(random_release_id)

random_release_url = "https://www.discogs.com/release/" + str(random_release_id)
print(random_release_url)

release_artist = d.release(random_release_id).artists[0].name
release_title = d.release(random_release_id).title
release_genres = d.release(random_release_id).genres
release_image = d.release(random_release_id).images[0]['uri']

# Creating an HTML file
# to open/create a new html file in the write mode
f = open('random_release.html', 'w')

# the html code which will go in the file GFG.html
html_template = f"""<html>
<head>
<link rel="stylesheet" href="style.css">
<title>Random Techno Release</title>
</head>
<body>
<div style="margin: 0 auto;" width="100%">
<h3><a href="{random_release_url}" target="_blank">{release_artist} - <em>{release_title}</em></a></h3>
<p><img src="{release_image}" height="400" /></p>
<p>{release_genres}</p>
</div>
</body>
</html>
"""

# writing the code into the file
f.write(html_template)

# close the file
f.close()