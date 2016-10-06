from flask import Flask, render_template, request, hashlib, csv

app = Flask(__name__)

@app.route('/')
def display():
    return render_template("home.html")

@app.route('/login/')
def dispLogin():
    return render_template("form.html")

@app.route('/result/', methods = ["POST"])
def auth():
    ##login
    if request.form["action"]=="login":
        username=request.form["user"]
        password=request.form["pass"]
        h=hashlib.md5(password)
        x=open('data/users.csv','r')
        for acc in x:
            if username == acc[0]:
                if h.hexdigest()==acc[1]:
                    return render_template("result.html", returnMsg="woot you're in")
                return render_template("result.html", returnMsg="it didn't work")
    else:
        username=request.form["user"]
        password=request.form["pass"]
        x=open('data/users.csv', 'a')
        for acc in data:
            if username==acc[0]:
                return render_template("result.html", returnMsg="username taken")
        newUser=csv.writer('data/users.csv')
        newUser.writerow([username,hashlib.md5(password).hexdigest()])
        return render_template("result.html", returnMsg="you're in"

if __name__ ==  '__main__':
    app.debug = True
    app.run()
    
