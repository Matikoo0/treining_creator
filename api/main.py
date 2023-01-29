import configparser

from flask import Flask

from models import db

from routes import exc,tre,usr


#inicaialize config file
config = configparser.ConfigParser()
config.read('../config')

#get path to database
path = f"sqlite:///{config['DATABASE']['PATH']}"

#inicialize app
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = path
db.init_app(app)


#api views
app.register_blueprint(exc, url_prefix='/exc')
app.register_blueprint(tre, url_prefix='/trener')
app.register_blueprint(usr,url_prefix='/user')


#inicialize database
with app.app_context():
    db.create_all()


#run app
if __name__ == '__main__':
    app.run(debug=True, port=5000)
