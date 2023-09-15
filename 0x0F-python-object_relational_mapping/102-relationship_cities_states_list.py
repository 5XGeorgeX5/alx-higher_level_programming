#!/usr/bin/python3
"""lists all City objects from the database"""
from sys import argv
from relationship_state import State
from relationship_city import City, Base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

if __name__ == '__main__':
    engine = create_engine(f'mysql+mysqldb://{argv[1]}:{argv[2]} \
        @localhost/{argv[3]}', pool_pre_ping=True)
    start_Session = sessionmaker(bind=engine)
    session = start_Session()
    cities = session.query(City)
    for city in cities:
        print(f'{city.id}: {city.name} -> {city.state.name}')
    session.close()
