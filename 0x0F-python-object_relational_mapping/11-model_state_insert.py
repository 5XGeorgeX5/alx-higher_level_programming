#!/usr/bin/python3
"""adds the State object 'Louisiana' to hbtn_0e_6_usa"""
from sys import argv
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

if __name__ == '__main__':
    engine = create_engine(f'mysql+mysqldb://{argv[1]}:{argv[2]} \
        @localhost/{argv[3]}', pool_pre_ping=True)
    start_Session = sessionmaker(bind=engine)
    session = start_Session()
    new_state = State(name='Louisiana')
    session.add(new_state)
    session.commit()
    print(new_state.id)
    session.close()
