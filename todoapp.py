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


'''
class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    task = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=True)
    priority = db.Column(db.Integer, nullable=True)

    def __repr__(self):
        return f'{self.task} assigned to {self.email}'
'''
'''
class AddTaskForm(FlaskForm):
    task = StringField(label='Task', validators=[DataRequired()])
    email = StringField(label='Email', validators=[DataRequired()])
    priority = SelectField(label='Priority', choices=[(1, 'Low'), (2, 'Medium'), (3, 'High')], coerce=int)
    submit = SubmitField(label='Submit')



'''


'''
@app.route('/add', methods=['GET', 'POST'])
def add():
    form = AddTaskForm()
    if form.validate_on_submit():
        t = Task(task=form.task.data, email=form.task.data, priority=form.task.data)
        db.session.add(t)
        db.session.commit()
        return redirect(url_for('todo'))
    return render_template('add.html', form=form)
'''
'''
@app.route('/edit/<int:task_id>', methods=['GET', 'POST'])
def edit(task_id):
    task = Task.query.get(task_id) # using .get() to get task associated with primary key
    form = AddTaskForm()
    if task:
        if form.validate_on_submit():
            task.task = form.task.data
            task.email = form.task.data
            task.priority = form.task.data
            db.session.commit()
            return redirect(url_for('todo'))
        form.task.data = task.task
        return render_template('edit.html', form=form, task_id=task_id)
    return redirect(url_for('todo'))
'''
'''
@app.route('/delete/<int:task_id>', methods=['GET', 'POST'])
def delete(task_id):
    task = Task.query.get(task_id) # using .get() to get task associated with primary key
    form = DeleteTaskForm()
    if task:
        if form.validate_on_submit():
            db.session.delete(task)
            db.session.commit()
            return redirect(url_for('todo'))
        return render_template('delete.html', form=form, task_id=task_id, task=task.task)
    return redirect(url_for('todo'))
'''


if __name__ == '__main__':
    app.run(debug=True)

"""
_______________________________________________________________

















if __name__ == '__main__':
    app.run(debug=True)
"""