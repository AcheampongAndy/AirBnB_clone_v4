#!/usr/bin/python3

from models.engine.db_storage import classes
import json
import models
from os.path import isfile
from collections import OrderedDict


class FileStorage:
    """
    a class taht serializes and deserializes instances to a JSON file
    """
    __file_path = "file.json"
    __objects = {}

    def all(self, cls=None):
        """returns the dictionary __objects"""
        if cls is not None:
            new_dict = {}
            for key, value in self.__objects.items():
                if isinstance(value, cls) or value.__class__.__name__ == cls:
                    new_dict[key] = value
            return new_dict
        return self.__objects

    def get(self, cls, id):
        """retrieves an object of a class with id"""
        if cls in classes.values() and id and type(id) is str:
            d_obj = self.all(cls)
            for key, value in d_obj.items():
                if key.split(".")[1] == id:
                    return value
        return None

    def count(self, cls=None):
        from sqlalchemy import func
        """retrieves the number of objects of a class or all (if cls==None)"""
        if cls is not None and cls in classes.values():
            return len(self.all(cls))
        else:
            return len(self.all())

    def new(self, obj):
        """
        sets in __objects the obj with key <obj class name>.id
        """
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        """
        serializes __objects to the JSON file (path: __file_path)
        """
        serializes_objects = {}
        for key, obj in self.__objects.items():
            serializes_objects[key] = obj.to_dict()
        json_str = json.dumps(serializes_objects)

        with open(self.__file_path, "w", encoding='utf-8') as file:
            file.write(json_str)

    def reload(self):
        """
        Deserializes the JSON file to __objects
        (only if the JSON file (__file_path) exists; otherwise, do nothing.
        If the file doesn’t exist, no exception should be raised)
        """
        from models.base_model import Base, BaseModel
        from models.user import User
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.place import Place
        from models.review import Review
        try:
            with open(self.__file_path, 'r', encoding='utf-8') as file:
                loaded_objects = json.load(file)
                for obj in loaded_objects.values():
                    class_name = obj["__class__"]
                    self.new(eval("{}({})".format(class_name, "**obj")))
        except FileNotFoundError:
            pass

    def delete(self, obj=None):
        """
        Deletes obj from __objects if it's inside
        """
        if obj is not None:
            key = '{}.{}'.format(type(obj).__name__, obj.id)
            if key in self.__objects:
                del self.__objects[key]
                self.save()

    def close(self):
        """call reload() method for deserializing the JSON file to objects"""
        self.reload()


if __name__ == "__main__":
    main()
