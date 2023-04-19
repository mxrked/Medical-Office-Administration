"""
data_manager.py - A abstract class that handles listeners for other DM's to
    work with. Be sure to use .close or __del__ methods to break connections
Author: Jessica Weeks, Christian Fortin
"""
from sqlalchemy.orm import sessionmaker
import sqlalchemy as sa
from contextlib import contextmanager
class DataManager():

    def __init__(self):


        try:
            from connection_string import DB
        except ImportError:
            try:
                from backend.connection_string import DB
            except ImportError:
                assert False, "connection_string.py not found!"

        self.__engine = sa.create_engine(f"mssql+pyodbc:///?odbc_connect={DB}")


        self.session_maker = sessionmaker(bind=self.__engine)

    @contextmanager
    def session_scope(self):
        session = self.session_maker()
        try:
            yield session
            session.commit()
        except AssertionError as error:
        
            assert False, str(error)

        except Exception as error:
            session.rollback()
            raise error

        finally:
            session.close()


    def close(self):
        self.__engine.dispose()

    def __del__(self):
        self.close()





    








