"""
data_manager.py - A abstract class that handles listeners for other DM's to
    work with. Be sure to use .close or __del__ methods to break connections

    A connect_string.py is required and cannot be hosted on github. 
        this is shared internally

Author: Jessica Weeks, Christian Fortin
"""
from sqlalchemy.orm import sessionmaker
import sqlalchemy as sa
from contextlib import contextmanager

try:
    from backend.connection_string import DB
except ModuleNotFoundError:
    try:
        from backend.connection_string import DB
    except ModuleNotFoundError:
        assert False, "connection_string.py not found!"
class DataManager():
    """
        The superclass of all Data Managers that handle interactions with the database
        
        To insure sessions aren't left lingering and are closed as soon as a query is over,
        we use a session_maker() that generates a session to handle DB interactions
    """
    def __init__(self):


        try:
            from backend.connection_string import DB
        except ModuleNotFoundError:
            try:
                from backend.connection_string import DB
            except ModuleNotFoundError:
                assert False, "connection_string.py not found!"

        self.__engine = sa.create_engine(f"mssql+pyodbc:///?odbc_connect={DB}", pool_pre_ping=True)
        self.session_maker = sessionmaker(bind=self.__engine)

    @contextmanager
    def session_scope(self):
        """
            Used for making sure DB connections are allways closed
        """
        session = self.session_maker()
        try:
            yield session
            session.commit()
        except AssertionError as error:
            # We want some of our error codes to pop up on the frontend
            # So we elevate them
            assert False, str(error)

        except Exception as error:
            session.rollback()
            raise error
            # Otherwise we wanna see the error

        finally:
            session.close()


    def close(self):
        """ Disposes of all db connections """
        self.__engine.dispose()

    def __del__(self):
        """ Disposes of all db connections"""
        self.close()





    








