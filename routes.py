from flask import Flask, render_template, request,flash,redirect,url_for
app = Flask(__name__)
app.secret_key = 'secret key'
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
        print(name,email)
        
       
        # process the data and save it to the database or perform some other action
        return redirect(url_for('index'))
    
    flash('Record saved successfully','success')
    print(name,email)
    return redirect(url_for('index'))
        
    



@app.route('/symbol.html')
def symbol():
    return render_template('symbol.html', the_title='Tiger As Symbol')

@app.route('/myth.html')
def myth():
    return render_template('myth.html', the_title='Tiger in Myth and Legend')

if __name__ == '__main__':
    app.run(debug=True)
