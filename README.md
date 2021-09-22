# poor-mans-twitter
Poor Man's Twitter using Django as backend

## Requirements
Build a "Poor Man's Twitter" application in a single web page. The page consists of 2 pieces of functionality on the URL '/'.

The ability for any visitor to tweet. A tweet consists of a 50 character text input, a datetime that automatically records the time of a message and a name. Visible form fields for a tweet are the tweet and the name, which must be aligned horizontally to one another.
The ability to display all tweets (unpaginated) in a table . Show the time of the tweet, the message and the name. Sort the table using only the time and name columns.

The tweet form should appear at the top of the page. The tweets table should appear underneath the form. **The process of adding a tweet must be asynchronous**.

No login is required in order to tweet.
## Technical requirements and stack
The following stack elements MUST be used EXCLUSIVELY. If an application or library is not listed, it cannot be used.

* Django 3.0+ (backend)
* Django Rest Framework
* SQLite (django default settings)

**Note**: To achieve asynchronous I use ASGI server using uvicorn change the runserver command to run the Django application as an ASGI instead of WSGI. (For production server we can use celery and on a docker container).

## Api Root

http://127.0.0.1:8000/api/

## Admin site Access

http://127.0.0.1:8000/admin/

user: admin

password:BPsQiU3fSdQpcc7
