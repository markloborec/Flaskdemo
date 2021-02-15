import os

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

if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True, port = int(os.environ.get("PORT", 17995)), use_reloader=True)