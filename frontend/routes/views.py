from flask import Blueprint,url_for,render_template,request,session
import requests as r

from passlib.hash import pbkdf2_sha512


v = Blueprint('view', __name__)

#get path to database
APIPATH="http://127.0.0.1:5000"

def hash_password(password:str)->str:
    return pbkdf2_sha512.hash(password)

def veryfi_password(password:str,hash:str)->bool:
    return pbkdf2_sha512.verify(password,hash)


@v.route('/')
def index():
    if 'username' in session:
        return f'Logged in as {session["username"]}, {[s for s in session]}'
    return 'You are not logged in'


@v.route('/login',methods=['GET','POST'])
def login():
    if request.method=='POST' and request.headers.get('Content-Type')=='application/json':
        data = request.json
        email=data["email"]
        entered_password=data["password"]
        userType='user'
        resp=r.get(APIPATH+'/user/email',headers={'email':email})
        if resp.status_code==204:
            resp=r.get(APIPATH+'/trener/email/',headers={'email':email})
            userType='trener'
        if resp.status_code==200:
            data=resp.json()
            if data['password']==hash_password(entered_password):
                #add to sesion all data
                session['email']=data['email']
                session['id']=data['id']
                session['name']=data['name']
                session['surname']=data['surname']
                if data['trener_id']!='null':
                    session['trener_id']==data['trener_id']
                url_for('index')
            else:
                return render_template('login.html',error='Invalid login data')
        
        return render_template('login.html',error='Invalid login data')
    return render_template('login.hmtl',error=None)