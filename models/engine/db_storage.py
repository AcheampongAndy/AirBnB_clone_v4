#!/usr/bin/python3

from os import getenv
from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import Base, BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

classes = {"BaseModel": BaseModel, "State": State, "City": City,
           "User":User, "Place":Place, "Review":Review, "Amenity":Amenity}

class DBStorage:
    __engine = None
    __session = None

    def __init__(self):

        """Create the engine and configure the session for the MySQL database."""
        db_user = getenv('HBNB_MYSQL_USER')
        db_pwd = getenv('HBNB_MYSQL_PWD')
        db_host = getenv('HBNB_MYSQL_HOST', default='localhost')
        db_name = getenv('HBNB_MYSQL_DB')

        connection_str = f'mysql+mysqldb://{db_user}:{db_pwd}@{db_host}/{db_name}'
        self.__engine = create_engine(connection_str, pool_pre_ping=True)

        if getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

        Base.metadata.create_all(self.__engine)
        Session = scoped_session(sessionmaker(bind=self.__engine, expire_on_commit=False))
        self.__session = Session()

    def all(self, cls=None):
        """
        Query all objects from the current database session.
        """
        from models import storage
        new_dict = {}

        if cls is not None:
            if isinstance(cls, str):  # Check if cls is a string
                cls = classes.get(cls)  # Use get to avoid KeyError

            if cls is not None and issubclass(cls, BaseModel):
                objs = self.__session.query(cls).all()
                for obj in objs:
                    key = "{}.{}".format(type(obj).__name__, obj.id)
                    new_dict[key] = obj

            return new_dict
        else:
            for key, value in classes.items():
                if key != "BaseModel":
                    objs = self.__session.query(value).all()
                    if len(objs) > 0:
                        for obj in objs:
                            key = "{}.{}".format(obj.__class__.__name__,
                                                 obj.id)
                            new_dict[key] = obj
            return new_dict



    def new(self, obj):
        """
        Add the object to the current database session.
        """
        self.__session.add(obj)

    def get(self, cls, id):
        """retrieves an object of a class with id"""
        if cls in classes.values() and id and type(id) is str:
            d_obj = self.all(cls)
            for key, value in d_obj.items():
                if key.split(".")[1] == id:
                    return value
        return None

    def count(self, cls=None):
        """retrieves the number of objects of a class or all (if cls==None)"""
        if cls is not None and cls in classes.values():
            return len(self.all(cls))
        else:
            return len(self.all())

    def save(self):
        """
        Commit all changes of the current database session.
        """
        self.__session.commit()

    def delete(self, obj=None):
        """
        Delete obj from the current database session if not None.
        """
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """
        Create all tables in the database and the current database session.
        """
        from models.base_model import BaseModel
        Base.metadata.create_all(self.__engine)
        Session = scoped_session(sessionmaker(bind=self.__engine,
            expire_on_commit=False))
        self.__session = Session()

    def close(self):
        """call remove() method on the private session attribute"""
        self.__session.close()
