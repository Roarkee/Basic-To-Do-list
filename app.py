from flask import Flask, render_template,redirect,request,url_for
from flask_sqlalchemy import SQLAlchemy


app=Flask(__name__,template_folder="templates")
app.config[ 'SQLALCHEMY_DATABASE_URI']='sqlite:///db.sqlite'
app.config[ 'SQLALCHEMY_TRACK_MODIFICATIONS']=False

db=SQLAlchemy(app)

class Todo(db.Model):

    task_id=db.Column(db.Integer, primary_key=True )
    task=db.Column(db.String, nullable=False)
    status=db.Column(db.Boolean, default=False)

with app.app_context():
    db.create_all()



# todos=[{'task':'hello', 'status':False}]
@app.route("/")
def index():
    todos=Todo.query.all()
    return render_template("index.html", todos=todos) 

@app.route("/add", methods=['POST'])
def add():
    todo=request.form.get('task')
    new_todo=Todo(task=todo, status=False)
    db.session.add(new_todo)
    db.session.commit()
    

    # todos.append({'task':todo, 'status':False})
    return redirect(url_for('index'))


@app.route("/edit/<int:task_id>" ,methods=["POST","GET"])
def edit(task_id):
    todo=Todo.query.get(task_id)
    todo.status=not todo.status
    db.session.commit()
    # todo=todos[index]
    # if request.method=='POST':
    #     todo['task']=request.form['task']
    #     return redirect(url_for('index'))
    # else:
    return redirect(url_for("index.html"))
    
# @app.route("/check/<int:index>")
# def check(index):
#     todos[index]['status']=not todos[index]['status']
#     return redirect(url_for('index'))


@app.route("/delete/<int:task_id>")
def delete(task_id):
    todo=Todo.query.get(task_id)
    db.session.delete(todo)
    db.session.commit()
    return redirect(url_for('index'))

if __name__=="__main__":
    app.run(debug=True)