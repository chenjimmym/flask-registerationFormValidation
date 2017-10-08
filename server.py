from flask import Flask, render_template, request, redirect, session, flash
app = Flask(__name__)
app.secret_key = 'aSecret'

@app.route('/')
def formPage():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submitted():
    print "success"
    return redirect('/')

app.run(debug=True)