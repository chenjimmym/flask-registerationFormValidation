from flask import Flask, render_template, request, redirect, session, flash
import re
app = Flask(__name__)
app.secret_key = 'aSecret'
emailREGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

@app.route('/')
def formPage():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submitted():
    email = request.form['email']
    firstName = request.form['firstName']
    lastName = request.form['lastName']
    password = request.form['password']
    passwordC = request.form['passwordConfirm']
    state = True
    if len(email) < 1 or len(firstName) < 1 or len(lastName) < 1 or len(password) < 1 or len(passwordC) < 1:
        flash("All field must be filled")
        return redirect('/')
    if password != passwordC:
        flash("Password must match")
        state = False
    if len(password) < 9:
        flash("Password must be longer than 8 characters")
        state = False
    if not firstName.isalpha() or not lastName.isalpha():
        flash("First and last name must be all alphabets")
        state = False
    if not emailREGEX.match(email):
        flash("Invalid Email Address!")
        state = False
    if state == True:
        flash("Successfully Submitted")
        print "Success"
        return redirect('/')
    else:
        print "Not Success"
        return redirect('/')

app.run(debug=True)