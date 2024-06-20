import mysql.connector
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)
app.secret_key = "os.urandom(24)" #Important for sessions

# Database connection details
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '' # Your XAMPP MySQL password (likely empty)
app.config['MYSQL_DB'] = 'dev_environment' # Your database name

mysql = mysql.connector.connect(
    host=app.config['MYSQL_HOST'],
    user=app.config['MYSQL_USER'],
    password=app.config['MYSQL_PASSWORD'],
    database=app.config['MYSQL_DB']
)
cursor = mysql.cursor(dictionary=True)

@app.route('/', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        cursor.execute("SELECT * FROM users WHERE username = %s AND password = %s", (username, password))
        user = cursor.fetchone()
        if user:
            return redirect(url_for('home'))
        else:
            error = 'Invalid Credentials. Please try again.'
    return render_template('login.html', error=error)

@app.route('/home')
def home():
    return 'Welcome to the Home Page!'

if __name__ == '__main__':
    app.run(debug=True)