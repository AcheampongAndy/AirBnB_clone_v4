#!/usr/bin/python3
"""
Fabric script that generates a tgz archive from the contents of the web_static
"""

from fabric.api import local, env, put, run
from datetime import datetime
from os.path import isdir, exists
env.hosts = ['54.160.88.241', '54.197.75.39']


def do_pack():
    """ make tgz archive file """
    try:
        date = datetime.now().strftime("%Y%m%d%H%M%S")
        if not isdir('versions'):
            local("mkdir versions")
        file_path = f"versions/web_static_{date}.tgz"
        local(f"tar -cvzf {file_path} web_static")
        return file_path
    except Exception as e:
        print(f'An error occurred: {e}')
        return None


def do_deploy(archive_path):
    """ deploy the archive file """
    if exists(archive_path) is False:
        return False
    try:
        ''' Upload a tar archive of an application '''
        put(archive_path, "/tmp/")

        ''' Extract only the file name from the path '''
        file_name = archive_path.split("/")[-1]

        ''' Extract file name without extension '''
        no_exten = file_name.split(".")[0]

        ''' Create the archive to the folder '''
        path = "/data/web_static/releases/"
        static_path = f"{path}{no_exten}"
        run(f"mkdir -p {static_path}")

        ''' Uncompress the archive to the folder '''
        run(f"tar -xzf /tmp/{file_name} -C {static_path}")
        run(f"mv {static_path}/web_static/* {static_path}")
        run(f"rm -rf {static_path}/web_static")

        ''' Delete the archive from the web server '''
        run(f"rm /tmp/{file_name}")

        ''' Delete the symbolic link /data/web_static/current '''
        run("rm -rf /data/web_static/current")

        ''' Create a new the symbolic link /data/web_static/current '''
        run(f"ln -s {static_path} /data/web_static/current")

        return True
    except:
        return False


def deploy():
    """Launches deploy processes"""
    archive_path = do_pack()
    if not archive_path:
        return False
    return do_deploy(archive_path)
