from flask import Flask, render_template, request, session, url_for, redirect
import hashlib, os

app = Flask(__name__)
app.secret_key = os.urandom(32)

@app.route('/')
def display():
    if len(session.keys())==0:
        return render_template("form.html")
    else:
        return redirect(url_for('home'))

@app.route('/home/')
def home():
    return render_template('home.html', user=session['userkey'])

@app.route('/logout/')
def logout():
    session.pop('userkey')
    return render_template('result.html', returnMsg="you logged out!")

@app.route('/result/', methods=["POST"])
def auth():
    ##LOGIN
    a=open('data/users.csv','r').read().split('\n')
    if "login" in request.form:
        password=request.form['pass']
        x=request.form['user']+','+hashlib.sha256(password).hexdigest()
        if x in open('data/users.csv', 'r').read():
            session['userkey']=request.form['user']
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
    app.debug=True
    app.run()
