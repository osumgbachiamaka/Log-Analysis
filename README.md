# Log-Analysis
An internal reporting tool that will use information from the database to discover what kind of articles the site's readers like.

## Project Description
Your task is to create a reporting tool that prints out reports (in plain text) based on the data in the database. 
This reporting tool is a Python program using the psycopg2 module to connect to the database.

## Questions
What are the most popular three articles of all time? Which articles have been accessed the most? Present this information as a sorted list with the most popular article at the top

Who are the most popular article authors of all time? That is, when you sum up all of the articles each author has written, which authors get the most page views? Present this as a sorted list with the most popular author at the top.

On which days did more than 1% of requests lead to errors? The log table includes a column status that indicates the HTTP status code that the news site sent to the user's browser.

## How to run
load the data onto the database
```python
psql -d news -f newsdata.sql
```
connect to the database
```python
psql -d news
```
## Create Views

```python
create view total_web_view as select date(time), count (*) as views from log 
group by date(time) order by date(time);
```

```python
create view error_web_view as select date(time), count (*) as views from log 
where status != '200 OK' group by date(time) order by date(time);
```
```python
create view main as select total_web_view.date, (100.00 * error_web_view.views / total_web_view.views) 
as error_percentage from total_web_view 
join error_web_view 
on total_web_view.date = error_web_view.date 
order by date; 
```
## Running the web app:
Run the app using:
```python
  $ python app.py
```
```python
  open http://localhost:8000/
```
