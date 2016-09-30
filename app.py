from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
@app.route('/login/')
def display():
    return render_template("form.html")

@app.route('/result/', methods = ["POST"])
def auth():
    ##set something equal to request.form
    if request.form['user'] == "lma" and request.form['pass']=="cool":
        ##returnMsg="it worked"
        return render_template("result.html", returnMsg="woot you're in")
    ##returnMsg="it didn't work"
    return render_template("result.html", returnMsg="it didn't work")

if __name__ ==  '__main__':
    app.debug = True
    app.run()
    
