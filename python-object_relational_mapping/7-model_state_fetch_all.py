#!/usr/bin/python3

"""Imports state from Base and lists all states from database"""


import sys
from model_state import Base, State
from sqlalchemy import create_engine, select
from sqlalchemy.orm import Session


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)

    with Session(engine) as session:
        for state in session.query(State).order_by(State.id).all():
            print("{}: {}".format(state.id, state.name))
