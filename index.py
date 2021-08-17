from flask import Flask, render_template,redirect,request,make_response
from functools import wraps

app = Flask(__name__)

auth_token = "asdfkjlg"

#Function to generate unique token based on user or/and pwd
def generate_token(user,pwd):
    return user + ":" + pwd

#Home route - always redirect to login
@app.route('/')
def home():
    return redirect('/login')

def auth(request):
    token = request.cookies.get('login-info')
    try:
        user, pwd = token.split(':')
    except:
        return False
    if (user == 'admin' and pwd == 'admin'):
        return True
    else:
        return False
#Route for basic login function
@app.route('/login',methods = ['GET','POST'])
def login():
    if request.method =='GET':
        return render_template('login.html')
    else :
        user = request.form.get('user')
        pwd = request.form.get('password')
        if(user == 'admin' and pwd == 'admin'):
            token = generate_token(user,pwd)
            resp = make_response(redirect('/index'))
            resp.set_cookie('login-info', token)
            return resp
        else :
            return redirect('/login'),403

@app.route('/index')
def index():
    if auth(request) :
        return render_template('index.html')
    else :
        return redirect('/')

def auth_required(f):
    @wraps(f)
    def check(*arg, **kwargs):
        if(auth(request)):
            return f(*arg, **kwargs)
        else :
            return redirect('/')
    return check

@app.route('/index2')
@auth_required
def index2():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host = 'localhost',port = 5000,debug = True)
