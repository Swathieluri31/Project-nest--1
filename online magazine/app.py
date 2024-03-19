from flask import Flask, render_template , request , redirect ,url_for
from pymongo import MongoClient

app = Flask(__name__, template_folder="templates")

# MongoDB configuration
client = MongoClient("mongodb://localhost:27017/")  # Replace with your MongoDB connection URI
db = client["signup"]  # Replace with your database name
collection = db['users']

@app.route('/')
def mainpage():
    return render_template('Mainpage.html')

@app.route('/homepage')
def Home():
    return render_template('homepage.html')

@app.route('/article')
def Article():
    return render_template('Article.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']

        # Insert data into MongoDB
        user_data = {
            'name': name,
            'email': email,
            'password': password
        }
        collection.insert_one(user_data)

        return redirect(url_for('Mainpage'))

    return render_template('signup.html')



@app.route('/contact')
def Contact():
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)
