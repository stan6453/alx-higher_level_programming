#!/usr/bin/python3
"""
adds the State object “Louisiana”
to the database hbtn_0e_6_usa
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State

if __name__ == "__main__":
    '''
    user_name = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    '''
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'
        .format(sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    state_update = session.query(State).filter(State.id == 2).first()

    if state_update:
        state_update.name = "New Mexico"
        session.commit()
