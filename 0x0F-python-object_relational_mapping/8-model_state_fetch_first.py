#!/usr/bin/python3
"""prints the first State object from hbtn_0e_6_usa"""
from sys import argv
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

if __name__ == '__main__':
    engine = create_engine(f'mysql+mysqldb://{argv[1]}:{argv[2]} \
        @localhost/{argv[3]}', pool_pre_ping=True)
    start_Session = sessionmaker(bind=engine)
    session = start_Session()
    state = session.query(State).first()
    if state:
        print(f'{state.id}: {state.name}')
    else:
        print('Nothing')
    session.close()
