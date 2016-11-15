#-*- coding: utf-8 -*-
# Authors: Gael Varoquaux, Nelle Varoquaux
# License: BSD 3 clause


from flask import Flask,request,render_template

app=Flask(__name__)


@app.route('/',methods=['GET','POST'])
def home():
    return render_template('home.html')

@app.route('/signin',methods=['GET'])
def signin_form():
    return render_template('form.html')

@app.route('/signin',methods=['POST'])
def sign():
    username=request.form['username']
    password=request.form['password']
    if uasername=='username' and password=='password':
        return render_template('signin.html',username=username)
    return render_template('form.html', message='Bad username or password', username=username)

if __name__=='__main__':
    app.run()