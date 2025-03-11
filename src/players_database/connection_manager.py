from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os


#Get the absolute path to the `players_database` folder
db_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'mydb.db')
engine = create_engine(f"sqlite:///{db_path}", echo=True)

Session = sessionmaker(bind=engine)

class SessionManager(object):
    """
    Create a separate class that makes its own session and then have every other class
    which interacts with the database inherit from this class.

    This way, the code is more modular and one only needs to create an engine and
    session one time. (One can commit multiple times with one session.)
    """

    def __init__(self):
        self.session = Session()

