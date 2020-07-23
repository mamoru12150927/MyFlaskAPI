from flask import Flask
from flask_jwt import JWT, jwt_required, current_identity
from werkzeug.security import safe_str_cmp

class User(self) :
    def __init__(self, id, username, password):
        self.id = id
        self.username = username
        self.password = password
    
    def __str__ (self) :
        return "User(id='%s')" % self.id

users = [
    User(1 , 'marumo' , 'tannzyoubi0927'),
    User(2 , 'marumo2' , 'tannzyoubi927'),
]

username_table = {u.username : u for u in users}
userid_table = {u.id : u for u in users}

def auth(username, password) :
    user = username_table.get(username , None)
    if user and safe_str_cmp(user.password.encode('utf-8') , password.encode('utf-8')) : 
        return user

app = Flask(__name__)
app.debug = True

@app.route('production')
@jwt_required()
def production() :
    return '%s' %current_identity

if name == '__main__':
    app.run()