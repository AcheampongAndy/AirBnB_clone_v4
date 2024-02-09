#!/usr/bin/python3
"""
Fabric script that generates a tgz archive from the contents of the web_static
"""

from fabric.api import local
from datetime import datetime
from os.path import isdir


def do_pack():
    """ make tgz archive file """
    try:
        date = datetime.now().strftime("%Y%m%d%H%M%S")
        if not isdir('versions'):
            local("mkdir versions")
        file_name = f"versions/web_static_{date}.tgz"
        local(f"tar -cvzf {file_name} web_static")
        return file_name
    except Exception as e:
        print(f'An error occurred: {e}')
        return None
