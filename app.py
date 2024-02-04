from flask import Flask, render_template, request, jsonify,redirect
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from decouple import config
app = Flask(__name__)
CORS(app)
app.config['SQLALCHEMY_DATABASE_URI']=config('DATABASE_URI')
db = SQLAlchemy(app)

class RandomValue(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    valeur = db.Column(db.String(50))
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/update', methods=['POST','GET'])  # Switch to POST method
def update():
    if request.method == "POST":
        value = request.form.get('button_clicked')
        new_random = RandomValue(valeur=value)
        db.session.add(new_random)
        db.session.commit()
        print("hjjjjjjjjjjjjg")
        return redirect('/')

    if request.method == "GET":
        return RandomValue.query.all()
with app.app_context():
    db.create_all()
@app.route('/add_on_value')
def add_on_value():
    print("on clicked")
    return "on clicked"

@app.route('/add_off_value')
def add_off_value():
    print("off clicked")
    return "off clicked"

if __name__ == '__main__':
    app.run(debug=True)
