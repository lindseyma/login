from flask import Flask, render_template, request
import hashlib

app = Flask(__name__)

@app.route('/')
def display():
    return render_template("form.html")

@app.route('/result/', methods=["POST"])
def auth():
    ##LOGIN
    a=open('data/users.csv','r').read().split('\n')
    if "login" in request.form:
        password=request.form['pass']
        x=request.form['user']+','+hashlib.sha256(password).hexdigest()
        if x in open('data/users.csv', 'r').read():
            return render_template("result.html", returnMsg="woot you're in!")
        else:
            return render_template("result.html", returnMsg="try again")
    ##REGISTER
    else:
        password=request.form['pass']
        username=request.form['user']
        u=''
        i=0
        for i in range(len(a)):
            u+=a[i].split(',')[0]
            print u
        if request.form['user'] in u:
            return render_template("result.html", returnMsg="username taken")
        else:
            addList=open('data/users.csv', 'a')
            addList.write(username+','+hashlib.sha256(password).hexdigest())
            addList.close()
            return render_template("result.html", returnMsg="success")
        
if __name__ == '__main__':
    app.debug
    app.run()
