# Plotting Discogs Data in Plotly

[![schedule-random-release](https://github.com/notalyce/info-664/actions/workflows/schedule-random-release.yml/badge.svg?branch=main)](https://github.com/notalyce/info-664/actions/workflows/schedule-random-release.yml)

Final project for INFO-664: Programming for Cultural Heritage at Pratt Institute. This project offers a starting point for visualizing music data from Discogs. The data is first cleaned using Pandas, then visualized using Plotly Express and exporting the graphs to an HTML file. For the example graphs, I visualized the techno genre, and saw some interesting trends in how formats have changed over time. Others could easily repurpose this code to explore broader datasets or even more genres.

A live example can be viewed at:
[https://notalyce.github.io/info-664/](https://notalyce.github.io/info-664/)

## Using This Code

To get started, you'll need to download [the data set, courtesy of Sohrab Daemi on Kaggle](https://www.kaggle.com/datasets/sohrabdaemi/discogs-database-all-release-data), last updated in September 2020. Download the data and place the `release_data_styles.csv` file in your local repository.

If you want to change the scope of the data being plotted, edit the genre in line 17 of `plot.py`. You can also change `style` to `genre` here depending on which column you want to work with, or change the scope of the data entirely using [Pandas dataframes](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html).

`df = df[df['style'].str.contains('Techno', na=False)]

## Behind The Project

For my final project for INFO-664, I had hoped to explore music data from [Discogs](https://www.discogs.com/developers), an open source, crowdsourced database of music. I'm interested in electronic music genres such as techno, and Discogs has what feels like an exhaustive database of music in this realm, without being limited by licensing like other APIs associated with listening platforms like Spotify.

### First Efforts

Initially, I tried pulling data using [python3-discogs-client](https://python3-discogs-client.readthedocs.io/en/latest/) and storing “dub techno” artists in a SQLite database locally. While I was able to successfully create a database and scrape some data, I ran into issues with downloading all of the data at once, and was only able to download about 400 out of over 30,000 records. The file `test-2.py` in the `archive` folder of the project reflects the code for this attempt. This format would have allowed me flexibility in deciding which data made it into my database - I could easily include columns such as the URL on Discogs (which could have opened up possibilities for scraping with a tool like [Beautiful Soup](https://beautiful-soup-4.readthedocs.io/en/latest/)).

### Data Dumps

Since downloading data with the above method wasn't working out, I turned to the [Discogs data dumps](https://discogs-data-dumps.s3.us-west-2.amazonaws.com/index.html) and downloaded all 4 xml files to explore - releases, artists, labels, and masters, and also found the [discogs-dump-parser](https://github.com/mjb2010/Discogs-dump-parser) and [discogs-xml2db](https://github.com/philipmat/discogs-xml2db) to potentially help manage the data. However, given my own time constraints and skill level for this project, I felt that the data structures were too unwieldy and had been hoping to work with a more simple table structure. 

### A New Data Set

When I turned to Kaggle, I was initially ready to ditch Discogs and move on to another data set. Instead, I managed to find a [Discogs data set](https://www.kaggle.com/datasets/sohrabdaemi/discogs-database-all-release-data) with a more manageable structure, although it has not been updated since September 2020.

This csv data set includes columns for **release_id, country, year, genre, style, format**.

### Visualization

For visualization, I consulted several blog posts like [this one](https://towardsdatascience.com/top-6-python-libraries-for-visualization-which-one-to-use-fe43381cd658) to decide which tool to use, and landed on [Plotly Express](https://plotly.com/python/plotly-express/) which allows [easy exporting of graphs to HTML](https://plotly.com/python/interactive-html-export/). I used [Pandas](https://pandas.pydata.org/) to manage and [clean](https://www.w3schools.com/python/pandas/pandas_cleaning.asp) the data.

Because I didn't initially include a `.gitignore` file, some of the experiments above are not documented in GitHub, though I did include the most promising first attempt to create a SQLite database in the `archive` folder.

### Gathering Further Data By Release

I started working on a file called `random_release.py` to pull a random release and display it on  `index.html` every 5 minutes. This uses the [python3-discogs-client](https://python3-discogs-client.readthedocs.io/en/latest/) to pull further data on a specific release based on the `release_id` in the csv file. This required learning how to [hide my Discogs API key](https://medium.com/black-tech-diva/hide-your-api-keys-7635e181a06c) before uploading the new files to GitHub.

To use this file, you'll need to add a `config.py` file to your base directory which includes your Discogs API key as follows:

`api_token = ""`

I referenced two guides for this step: [one for writing an HTML file in Python](https://www.geeksforgeeks.org/how-to-write-to-an-html-file-in-python/), and [one for scheduling the function to run every 5 minutes with a GitHub action](https://canovasjm.netlify.app/2020/11/29/github-actions-run-a-python-script-on-schedule-and-commit-changes/). I also discovered that I needed to use a [GitHub secret token](https://medium.datadriveninvestor.com/accessing-github-secrets-in-python-d3e758d8089b) for the repository to store my Discogs API token here.
