from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


DB_PATH = 'project.db'
engine = create_engine("sqlite:///" + DB_PATH)

Base = declarative_base()
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)