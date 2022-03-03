# How to build projects in Flask

## Prerequisites

This tutorial requires you to have some basic knowledge of python and a bit of html.


## Setup

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
    pip install flask 
    ```
4. (Optional) Save the dependencies in `requirements.txt`
    `requirements.txt` is osmething that you'll see commonly used. 

    ```bash
    pip freeze > requirements.txt
    ```

    to install dependencies from `requirements.txt`
    ```bash
    pip install -r requirements.txt
    ```

## Quick start

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

## Templates

> Templates are files that contain static data as well as placeholders for dynamic data. A template is rendered with specific data to produce a final document. Flask uses the [Jinja](https://jinja.palletsprojects.com/templates/) template library to render templates.
> 
> from [official docs](https://flask.palletsprojects.com/en/2.0.x/tutorial/templates/)

We use templates to render html files which is visible to the end user.

We are now going to create a html file and return in the root route (`/`).

Follow the steps below

1. create `index.html` inside the directory `/templates`
   
2. Enter some message in the html file. This is what my file looks like
    ```html
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>flask-helloworld</title>
    </head>
    <body>
        <h1>Hello World from index.html</h1>
    </body>
    </html>
    ```

3. Rendering the `index.html`
   1. Import `render_template` from flask 
   
        It should look like this

        `from flask import Flask, render_template`
   2. Change the return value of `index` function to `return render_template("index.html")`. 

4. Save the changes and reload the site (`http://127.0.0.1:5000/`)

You should now see the changes.

## Defining routes

Routes are the links to various pages of the web app.

Now, you'll learn how create a new route `/page2`

1. Create `page2.html` in `/templates` dir.
    
    Here's how mine looks like
    ```html
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>page 2</title>
    </head>
    <body>
        <h1>This is the page 2 of your flask web app</h1>
    </body>
    </html>
    ```
2. Define a new function in `app.py` that renders `page2.html`

    ```py
    @app.route('/page2')
    def index():
        return render_template("page2.html")
    ```

3. Save the changes and head to `http://127.0.0.1:5000/page2`

## Conclusion

Congrats! You reached the end of the tutorial. You learned how to setup the environment for flask, write a hello world program, render html files and define routes.

This was a walkthrough the basics of flask. 

You can learn more from the following resources:

- [flask docs](https://flask.palletsprojects.com/en/2.0.x/)
- [Learn Flask Web Development for Python in this Free 1-hour Course](https://www.freecodecamp.org/news/learn-flask-for-python-full-tutorial/)