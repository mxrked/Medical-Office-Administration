from sqlalchemy.orm import sessionmaker
import sqlalchemy as sa

class DataManger():

    def __init__(self):


        try:
            from connection_string import DB
        except ImportError:
            try:
                from backend.connection_string import DB
            except ImportError:
                assert False, "connection_string.py not found!"

        engine = sa.create_engine(f"mssql+pyodbc:///?odbc_connect={DB}")

        session_maker = sessionmaker(bind=engine)

        self.session = session_maker()

    def close(self):
        self.session.close()
        self.session.bind.dispose()

    def __del__(self):
        self.close()





    








