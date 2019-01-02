from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_session import Session
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from werkzeug.security import generate_password_hash, check_password_hash
from flask_bootstrap import Bootstrap

app = Flask(__name__)
DATABASE_URL = os.getenv("DATABASE_URL")
#secure forms
app.config['SECRET_KEY'] = 'gs3D#00kR3@*^'
# Configure session to use filesystem
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)
bootstrap = Bootstrap(app)

engine = create_engine(DATABASE_URL)

DbEngine = scoped_session(sessionmaker(bind=engine))

Base = declarative_base()

db = DbEngine()

from booknetwork import routes