import psycopg2
import bleach

from datetime import datetime

DBNAME = "news"

def get_views():
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute("select title, count(*) as views from log join articles on articles.slug = split_part(log.path, '/', 3) group by title order by views desc limit 3;")
    views = c.fetchall()
    db.close()
    return views

def get_authors():
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute("select name, count(*) as views from log join articles on articles.slug = split_part(log.path, '/', 3) join authors on articles.author = authors.id group by name order by views desc; ")
    authors = c.fetchall()
    db.close()
    return authors

def error_percentage():
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute("select * from main where error_percentage > 1.0;")
    error = c.fetchall()
    db.close
    
    return error