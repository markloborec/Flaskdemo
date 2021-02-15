from flask import Flask
from flask import render_template
app = Flask(__name__)
St_uporabnikov = 0
@app.route('/')
def index():
    global St_uporabnikov
    St_uporabnikov += 1
    return render_template('index.html',stu = St_uporabnikov )

@app.route('/bio')
def bio():
    global St_uporabnikov
    St_uporabnikov += 1
    return render_template('bio.html')

@app.route('/contact')
def contact():
    global St_uporabnikov
    St_uporabnikov += 1
    return render_template('contact.html')


@app.route('/test')
def test():
    return 'Test rout'

