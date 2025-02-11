"""
Using advice from StackOverflow to create a separate class that makes its own session
and then have every other class which interacts with the database inherit from this class.

This way, I think the code is more modular and I only need to create an engine and 
session one time. (I believe one can commit multiple times with one session.)

Advice found here: https://stackoverflow.com/questions/31681644/accessing-same-db-session-across-different-modules-in-sqlalchemy

"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


engine = create_engine("sqlite:///players_database/mydb.db", echo=True)
print("Database created")

# create a Session
Session = sessionmaker(bind=engine)

class SessionManager(object):
    def __init__(self):
        self.session = Session()

