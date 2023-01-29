import configparser

from flask import Flask

from routes import v




app=Flask(__name__)

app.register_blueprint(v)
app.secret_key=b'26a6cc5574cd06d2fab4e7af6f140dafaa414ba99a997f5c39fb1640cfad15bf'


if __name__ == '__main__':
    app.run(debug=True, port=8080)
