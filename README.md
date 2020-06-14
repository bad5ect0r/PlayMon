# PlayMon

A simple collection of python scripts used to track Google Playstore app versions.

## Setup

Pretty much all it needs is play\_scraper to scrape the Google Playstore. Then,
just run init.py to create the SQLite database file. You should also set the
constants in pushover.py to your pushover settings. Finally, have the checker.py
script running every 5 minutes or so using a cronjob.

