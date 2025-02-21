from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

class SQLClass:

    """
        This class provide the connection between database and program
    """
    def __init__(self, username, password, hostname, port, database):

        self.username = username
        self.__password = password
        self.hostname= hostname
        self.port = port
        self.database = database

        self.engine = create_engine(
            url = "mysql+pymysql://{0}:{1}@{2}:{3}/{4}".format(
                self.username,
                self.__password,
                self.hostname,
                self.port,
                self.database
            )
        )

        self.Session = sessionmaker(bind = self.engine)
        self.session = self.Session()
    
    def insert_query(self, *args ):
        """
            Inserting data from your database
            Use the models that you want to insert
        """
        for arg in args:
            print(f"ID: sucessfully added to the database")
            self.session.add(arg)
            self.session.commit()
    
    def select_all(self, models):
        """_summary_

        Args:
            models (models Class): Choose the table you want to return the data
        """

        return self.session.query(models).all()
    
    def search(self, models, *args):
        """_summary_

        Args:
            models (models_class): Choose the table you want to return the data
            *args: create the where statement

        Returns:
            session
        """
        return self.session.query(models).filter(*args).all()
    

    def update_one(self, model, *args, **kwargs):
        instance = self.session.query(model).filter(*args).first()
        if instance:
            for key, val in kwargs.items():
                print(key, val)
                setattr(instance, key, val)
            self.session.commit()
            print("Update Successfully")
        else:
            print("No data Found")


    def update_many(self, model, *args,  **kwargs):
        instances = self.session.query(model).filter(*args).all()

        if instances:
            for instance in instances:
                for key, val in kwargs.items():
                    setattr(instance, key, val)
                self.session.commit()
            print("Update Successfully")
        else:
            print("No Data Found")







        
