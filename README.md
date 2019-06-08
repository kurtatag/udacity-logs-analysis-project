# Udacity Logs Analysis Project

We've been asked to build an **internal reporting tool** for a newspaper site. The tool will use information from the database to discover what kind of articles the site's readers like.

The database contains newspaper articles, as well as the web server log for the site. The log has a database row for each time a reader loaded a web page.

The program we write in this project will run from the command line. It won't take any input from the user. Instead, it will connect to that database, use SQL queries to analyze the log data, and print out the answers to the following questions:
* What are the most popular three articles of all time?
* Who are the most popular article authors of all time?
* On which days did more than 1% of requests lead to errors?

## Requirements
* Ubuntu 16.04 or later
* Postgresql 9.5 or later
* Python 3.5 or later

## Install
```console
$ git clone ...
$ sudo pip3 install -r requirements.txt
```

## Database Setup
```console
$ # create test database in postgres
$ createdb news

$ # download and unzip test data for postgres
$ wget https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip
$ unzip newsdata.zip

$ # load test data into postgres
$ psql -d news -f newsdata.sql
```

## Run
```console
$ python3 report.py
```

## Output
```console
Problem:
What are the most popular three articles of all time?

Solution:
"Candidate is jerk, alleges rival" -- 338,647 views
"Bears love berries, alleges bear" -- 253,801 views
"Bad things gone, say good people" -- 170,098 views


========================================================================


Problem:
Who are the most popular article authors of all time?

Solution:
Ursula La Multa -- 507,594 views
Rudolf von Treppenwitz -- 423,457 views
Anonymous Contributor -- 170,098 views
Markoff Chaney -- 84,557 views


========================================================================


Problem:
On which days did more than 1% of requests lead to errors?

Solution:
JULY 17, 2016 -- 2.26% errors


========================================================================
```
