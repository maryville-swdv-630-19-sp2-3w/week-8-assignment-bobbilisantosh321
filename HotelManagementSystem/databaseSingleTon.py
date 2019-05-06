from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class DataBaseSession:
    __instance = None
    session = None

    def __new__(self):
        if DataBaseSession.__instance is None:
            DataBaseSession.__instance = object.__new__(self)

        return DataBaseSession.__instance

    def createSession(self):

        # Initiate DB connection to memory
        if self.session == None:
            engine = create_engine('sqlite:///:memory:', echo=False)
            Base.metadata.create_all(engine)
            Session = sessionmaker(bind=engine)
            # Capture connection Session
            self.session = Session()

        return self.session

