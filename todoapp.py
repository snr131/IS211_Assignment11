from flask import Flask, render_template, redirect, url_for, flash, request
import re
import pickle


app = Flask(__name__)
app.secret_key = 'secretkey'


todo_list = []


@app.route('/')
def display_list():

    global todo_list

    try:
        with open('todoapp.pickle', 'rb') as f:
            todo_list = pickle.load(f)
        return render_template('todo.html', todo_list=todo_list)

    except:
        return render_template('todo.html', todo_list=todo_list)


@app.route('/submit', methods=["GET", "POST"])
def submit():

    global todo_list

    email_regex = r'^(\w|\.|\_|\-)+[@](\w|\_|\-|\.)+[.]\w{2,3}$'

    task = request.form['task']
    email = request.form['email']
    priority = request.form['priority']
    if (re.search(email_regex, email)):
        if priority == 'Low' or priority == 'Medium' or priority == 'High':
            todo_list.append((task, email, priority))
            flash('New task added to list')
        else:
            flash('Invalid priority, try again')
    else:
        flash('Invalid email, try again')

    return redirect('/')


@app.route('/clear')
def clear():
   
    global todo_list

    todo_list = []

    return render_template('todo.html', todo_list=todo_list)


@app.route('/save')
def save():

    with open ('todoapp.pickle', 'wb') as f:
        pickle.dump(todo_list, f)

    flash('List saved')
    
    return redirect('/')


@app.route('/load')
def load():

    with open('todoapp.pickle', 'rb') as f:
        todo_list = pickle.load(f)

    return render_template('todo.html', todo_list=todo_list)


if __name__ == '__main__':
    app.run(debug=True)