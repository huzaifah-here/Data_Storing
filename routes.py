from flask import Flask, render_template, request,flash,redirect,url_for
import crud as db
import mysql.connector
app = Flask(__name__)
app.secret_key = 'secret key'

conn = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="sql_crud"
)
# two decorators, same function
@app.route('/')
@app.route('/index.html')
def index():
    return render_template('index.html', the_title='CRUD')

@app.route('/submit_data', methods=['GET', 'POST'])
def submit_data():
    name = request.form['user-name']
    email = request.form['user-email']
    if request.method == 'POST' and name=="":
        flash('An error occurred', 'error')
        #print(name,email)
        # process the data and save it to the database or perform some other action
        return redirect(url_for('index'))
    
    flash('Record saved successfully','success')
    db.create(conn, name, email)
    print(name,email)
    return redirect(url_for('index'))
    

@app.route('/read')
def read():
    tuple=()
    return render_template('read.html', the_title='READ', tuple=tuple)
@app.route('/read_data', methods=['GET', 'POST'])
def read_data():
    name = request.form['user-name']
    data=db.read(conn,name)
    print(data)
    
    return render_template("read.html", tuple=data,name=name)


@app.route('/update', methods=['GET', 'POST'])
def update():
    ids=db.total_ids(conn)
    print("list")
    print(ids)
    print("list")
    return render_template('update.html', ids=ids,the_title='UPDATE')

@app.route('/update_data', methods=['GET', 'POST'])
def update_data():
    name = request.form['user-name']
    email = request.form['user-email']
    ids = request.form['user-id']
    print(ids)
    if request.method == 'POST' and name=="":
        flash('An error occurred', 'error')
        #print(name,email)
        # process the data and save it to the database or perform some other action
        return redirect(url_for('index'))
    
    flash('Record saved successfully','success')
    db.update(conn, name, email, ids)
    print(name,email)
    return redirect(url_for('update')) 


@app.route('/delete', methods=['GET','POST'])
def delete():
    # ids = request.form['user-id']
    return render_template('delete.html', the_title='DELETE')
@app.route('/delete_data', methods=['GET','POST'])
def delete_data():
    print("hello")
    ids = request.form['user-id']
    print(ids)
    db.delete(conn,ids)
    return redirect(url_for('read')) 

#
    
@app.route('/symbol.html')
def symbol():
    return render_template('symbol.html', the_title='Tiger As Symbol')

@app.route('/myth.html')
def myth():
    return render_template('myth.html', the_title='Tiger in Myth and Legend')

if __name__ == '__main__':
    app.run(debug=True)
