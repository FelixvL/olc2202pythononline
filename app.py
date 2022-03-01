from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/tweede")
def hello_world3():
    var1 = 3
    var2 = var1 * var1
    return "<p>Hier komt nog " + str(var2) + "ner</p>"

@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hoi.html', name=name)