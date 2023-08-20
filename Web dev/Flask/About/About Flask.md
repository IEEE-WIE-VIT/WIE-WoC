# About Flask

## Table of contents
- [About Flask](#about-flask)
  - [Table of contents](#table-of-contents)
  - [What is Flask?](#what-is-flask)
  - [How it compares to other frameworks](#how-it-compares-to-other-frameworks)
    - [What should you use?](#what-should-you-use)
  - [How to get started](#how-to-get-started)
    - [Setup](#setup)
    - [Quick start](#quick-start)
  - [Project layout](#project-layout)

## What is Flask?

Flask is a web application framework in Python. It is minimal enough to call it as a *micro framework*. It provides basics core functionalities and has a lot of extensions like Flask SQLAlchemy, Flask Mail, Flask-RESTPlus, etc.

Here's a list of [flask resources and extensions](https://github.com/humiaozuzu/awesome-flask)

## How it compares to other frameworks

One popular question that comes across many developer's minds is "Flask or Django?".

Flask is really lightweight compared to django. It lacks functionalities like built in ORM(Object-relational mapping), authentication and admin panel.

### What should you use?

Flask is popular for small and medium size projects like Single Page Applications(SPAs), portfolio website and personal blog.

Whereas, Django is more suitible for applications like an e-commerce website.

If you're just starting in python and programming in general, then Flask is a great choice as it has a much lesser learning curve compared to django.

## How to get started

### Setup

Here I'm setting up a virtual env to install the `flask` module

Terminal - **bash** (command for activating virtualenv differs in cmd)

1. Set up virtualenv
    ```bash
    $ virtualenv venv
    ```
2. Activate venv

    cmd
    ```cmd
    venv\Scripts\activate
    ```
    bash
    ```bash
    $ source venv/scripts/activate
    ```
3. Install required modules
    ```bash
    pip install flask flask-sqlalchemy
    ```

### Quick start

Here's a minimal 10 line Flask app

```py
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello world"

if __name__ == "__main__":
    app.run(debug=True) 
```

What is the code?

1. We imported the `Flask` class. 
2. We created an instance of this class. `__name__` is a global varibale which has the value of `"__main__"` when the code is executed.
3. We then use `@app.route('/')` to assign a route to the defined fuction `index`.
4. The index returns a string `"Hello world"`. This will show up the text in the web app when you open `http://127.0.0.1:5000/` in the browser. 
5. Then `app.run(debug=True)` is used to start the flask server.

Now save the above code  and run!

You should see something like this. Open the link to see the web page.
```
 * Serving Flask app 'main' (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: on
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 440-888-939
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
 ```

## Project layout

Flask does not define any particular layout. 

A Flask application can be as simple as a single file as you saw above.

However, managing a single file can become very tedious as you scale your app. 

It's your decision as a developer how you want to structure your project.

<details>
          <summary>This is a structure for a small sized project</summary>
```txt
project-name
├─── static/
│    └─── style.css
├─── templates/
│    ├─── base.html
│    └─── index.html
├─── .gitignore
├─── app.py
├─── README.md
├─── requirements.txt
└─── test_client.py
```
</details>

<details>
          <summary>As you scale up, you'll need something more like which supports larger projects</summary>
          
```txt
learn-flask
├─── app/
│   ├─── __init__.py
│   ├─── app.py
│   ├─── templates/
│   │    ├─── base.html
│   │    ├─── index.html
│   └─── static/
│        └─── style.css
├─── tests/
│    ├─── test_client.py
├─── setup.py
├─── README.md
└─── requirements.txt
```
</details>