# Log Analysis Report
This repo creates a reports for news database. Below are the reports created. To run this code, you need to install vagrant and download VM which is configured for you.

1. **What are the most popular three articles of all time**?
Example: 
"Princess Shellfish Marries Prince Handsome" — 1201 views
"Baltimore Ravens Defeat Rhode Island Shoggoths" — 915 views
"Political Scandal Ends In Political Scandal" — 553 views

2. **Who are the most popular article authors of all time**?
Example:
Ursula La Multa — 2304 views
Rudolf von Treppenwitz — 1985 views
Markoff Chaney — 1723 views
Anonymous Contributor — 1023 views


3.  **On which days did more than 1% of requests lead to errors**? 
Example:
July 29, 2016 — 2.5% errors

Installation:
=============
1. Install Vagrant. (https://www.vagrantup.com/downloads.html).
2. Download VM configuration. (https://github.com/udacity/fullstack-nanodegree-vm)

Creating News Database:
=======================
1. Go to directory where you have downloaded above VM configuration.
2. Start vagrant using command ```vagrant up```.
3. Using ```vagrant ssh``` you can login into VM.
4. Download news data from (https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip) where vagrantfile is present, so that this file can be accessed from VM.
5. Run ```psql -f newsdata.sql```


Output:
=======

Output of report will displayed on console, as well as creates report file with ".txt" format in same directory.

1. _3_popular_articles.txt_
2. _popular_author.txt_
3. _day_on_which_more_request_errors.txt_

Running:
========

To execute this report.

1. Make sure you create new log_analysis directory inside vagrant folder. ```mkdir log_analysis```
2. git clone this repo inside log_analysis directory.
3. Run ```python log_analysis.py```. 
4. Report log should be created in same directory.
