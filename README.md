This repo creates a reports for news database. Below are the reports created.

1. What are the most popular three articles of all time?
Example: 
"Princess Shellfish Marries Prince Handsome" — 1201 views
"Baltimore Ravens Defeat Rhode Island Shoggoths" — 915 views
"Political Scandal Ends In Political Scandal" — 553 views

2. Who are the most popular article authors of all time?
Example:
Ursula La Multa — 2304 views
Rudolf von Treppenwitz — 1985 views
Markoff Chaney — 1723 views
Anonymous Contributor — 1023 views


3.  On which days did more than 1% of requests lead to errors? 
Example:
July 29, 2016 — 2.5% errors

Requirements:
=============

1. Make sure you have python 2.7 installed.
2. psql should be installed with news database.


Output:
=======

Output of report will displayed on console, as well creates report file with
".txt" format in same directory.

1. 3_popular_articles.txt
2. popular_author.txt
3. day_on_which_more_request_errors.txt

Execute:
========

To execute this report.

1. Make sure you create new log_analysis directory.
2. git clone this repo inside log_analysis directory.
3. Run "python log_analysis.py". 
4. Report log should be created in same directory.
