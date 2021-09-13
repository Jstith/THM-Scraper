__THM Scraper__
===============

By: _Jstith_

This is a small script to scrape information about TryHackMe users created to aid the process of checking what rooms have been completed by students in a classroom setting.

### Dependences
- Google Chrome
- python3
- selenium
- webdriver-manager

### Run
To run, first install python3, pip, and the necessary dependences
```
pip install -r requirements.txt
```
Once the dependencies are installed, run the python script with
```
python3 thmScraper.py
```

### Functionality
Current functionality includes:
- Reading Users and Usernames from a CSV
- Selecting one or all users to scrape
- Dispaly on CLI output all rooms each user has completed on THM

### Future Goals
- Sort by room and/or user
- Progress bar
- Colored output for easier reading
- CSV file output
