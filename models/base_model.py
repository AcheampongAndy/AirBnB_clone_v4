#!/usr/bin/python3

import uuid
from datetime import datetime
#from models import storage
from sqlalchemy import Column, String, Integer, DateTime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class BaseModel:
    """"
        This defines common attributes and methods for other classes
    """

    id = Column(String(60), primary_key=True, nullable=False, unique=False)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    updated_at = Column(DateTime, default=datetime.utcnow, nullable=False)

    def __init__(self, *args, **kwargs):
        """
            Initialize BaseModel instance.
        """
        if kwargs:
            """
                if kwargs is not empty set attributes from kwargs
            """
            for key, value in kwargs.items():
                if key != "__class__":
                    if key == 'created_at' or key == 'updated_at':
                        value = datetime.strptime(
                                value, "%Y-%m-%dT%H:%M:%S.%f")
                    setattr(self, key, value)
            if 'id' not in kwargs:
                setattr(self, 'id', str(uuid.uuid4()))
                setattr(self, 'created_at', datetime.utcnow())
                self.updated_at = self.created_at
        else:
            """
               if kwargs is empty generate the foll
            """
            self.id = str(uuid.uuid4())
            self.created_at = datetime.utcnow()
            """
                Set update_at with the value of created_at
            """
            self.updated_at = datetime.utcnow()
            """
            if it’s a new instance (not from a dictionary representation)
            add a call to the method new(self) on storage
            """

    def __str__(self):
        """
            Print [<class name>] (<self.id>) <self.__dict__> to the screen
        """
        new_dict = dict(self.__dict__)
        new_dict.pop('_sa_instance_state', None)
        return("[{}] ({}) {}".format(
            self.__class__.__name__, self.id, self.__dict__))

    def __repr__(self):
        '''
            Return string representation of BaseModel class
        '''
        return ("[{}] ({}) {}".format(self.__class__.__name__,
                                      self.id, self.__dict__))

    def save(self):
        """
        Update the updated_at to the current datetime
        """
        from models import storage
        self.updated_at = datetime.now()
        """ call save(self) method of storage """
        storage.new(self)
        storage.save()

    def to_dict(self):
        """
        Return dictionary representation of BaseModel class.
        """
        sel_dict = dict(self.__dict__)
        sel_dict["__class__"] = type(self).__name__
        sel_dict["created_at"] = sel_dict["created_at"].isoformat()
        sel_dict["updated_at"] = sel_dict["updated_at"].isoformat()
        sel_dict.pop('_sa_instance_state', None)

        return sel_dict

    def delete(self):
        '''
        delete the current instance from the storage
        '''
        storage.delete(self)
