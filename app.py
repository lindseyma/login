from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
@app.route('/login/')
def display():
    return render_template("form.html")

@app.route('/authenticate/', methods = ["POST"])
def auth():
    ##set something equal to request.form
    if request.form['user'] == "lma" and request.form['pass']=="cool":
        return render_template("it worked")
    return render_template("ouch")

if __name__ ==  '__main__':
    app.debug = True
    app.run()
    
