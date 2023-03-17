#!/usr/bin/python3
"""
prints all City objects from the database hbtn_0e_14_usa
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State
from model_city import City

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

    result = session.query(City, State)\
        .filter(State.id == City.state_id).order_by(City.id).all()

    if result:
        for state, city in result:
            print(f"{state.name}: ({city.id}) {city.name}")
