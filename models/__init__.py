#!/usr/bin/python3

from os import getenv

"""
create the variable storage, an instance of FileStorage
"""
storage_t = getenv("HBNB_TYPE_STORAGE")

if getenv('HBNB_TYPE_STORAGE') == 'db':
    from models.engine.db_storage import DBStorage
    storage = DBStorage()
else:
    from models.engine.file_storage import FileStorage
    storage = FileStorage()

storage.reload()
