#!/usr/bin/python3
"""deletes all States that contain the letter a from hbtn_0e_6_usa"""
from sys import argv
from model_state import Base, State
from model_city import City
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

if __name__ == '__main__':
    engine = create_engine(f'mysql+mysqldb://{argv[1]}:{argv[2]} \
        @localhost/{argv[3]}', pool_pre_ping=True)
    start_Session = sessionmaker(bind=engine)
    session = start_Session()
    table = session.query(City, State).join(State)
    for city, state in table:
        print(f'{state.name}: ({city.id}) {city.name}')
    session.close()
