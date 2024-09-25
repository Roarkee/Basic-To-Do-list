from flask import Flask, render_template,redirect,request,url_for




app=Flask(__name__,template_folder="templates")
todos=[{'task':'hello', 'status':False}]
@app.route("/")
def index():
    return render_template("index.html", todos=todos) 

@app.route("/add", methods=['POST'])
def add():
    todo=request.form['task']
    todos.append({'task':todo, 'status':False})
    return redirect(url_for('index'))


@app.route("/edit/<int:index>" ,methods=["POST","GET"])
def edit(index):
    todo=todos[index]
    if request.method=='POST':
        todo['task']=request.form['task']
        return redirect(url_for('index'))
    else:
        return render_template("edit.html", todo=todo, index=index)
    
@app.route("/check/<int:index>")
def check(index):
    todos[index]['status']=not todos[index]['status']
    return redirect(url_for('index'))


@app.route("/delete/<int:index>")
def delete(index):
    del todos[index]
    return redirect(url_for('index'))

if __name__=="__main__":
    app.run(debug=True)