#!/usr/bin/python3

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import  Base, State

#user_name = sys.argv[1]
#password = sys.argv[2]
#db_name = sys.argv[3]
engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(sys.argv[1],
    sys.argv[2], sys.argv[3]), pool_pre_ping=True)
Base.metadata.create_all(engine)

Session = sessionmaker()

session = Session()

states = session.query(State).order_by(State.id).all()

for index,state in enumerate(states):
    print(f"{index}: {state}")

