from flask import render_template, redirect, url_for, request
from app import app, db
from app.models import Todo


@app.route('/')
def index():
    incomplete = Todo.query.filter_by(status=False).all()
    complete = Todo.query.filter_by(status=True).all()
    return render_template('index.html', complete=complete, incomplete=incomplete)


@app.route('/add', methods=['POST'])
def add():
    todo = Todo(text=request.form['todoitem'], status=False)
    db.session.add(todo)
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/complete/<id>')
def complete(id):
  
    todo = Todo.query.filter_by(id=int(id)).first()
    todo.status = True
    db.session.commit()
  
    return redirect(url_for('index'))

@app.route('/incomplete/<id>')
def incomplete(id):
  
    todo = Todo.query.filter_by(id=int(id)).first()
    todo.status = False
    db.session.commit()
  
    return redirect(url_for('index'))