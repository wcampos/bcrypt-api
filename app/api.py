#!/usr/bin/python
from flask import Flask
import bcrypt

app = Flask(__name__)

@app.route('/')
def index():
    return "Hey buddy!"

@app.route('/pwdncrypt')
def pwd_alive():
    return "Password Encryption Service -- ALIVE!"

@app.route('/pwdncrypt/<string:initpwd>', methods=['GET'])
def pwd_encrypt(initpwd):
# Default rounds to 4 == Works for jenkins
  hashpwd = bcrypt.hashpw(initpwd , bcrypt.gensalt(log_rounds=4))
  return hashpwd

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')
