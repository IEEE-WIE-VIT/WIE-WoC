# About Flask


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
