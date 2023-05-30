#!/usr/bin/python3
"""
Fabric script that generates a .tgz archive from the contents of the web_static folder of your AirBnB Clone repo, using the function do_pack
"""

from fabric.api import local
from datetime import datetime

"""def do_pack():
    Generates a .tgz archive from the contents of the web_static folder.
    
    now = datetime.now()
    timestamp = now.strftime("%Y%m%d%H%M%S")
    archive_name = "web_static_{}.tgz".format(timestamp)
    archive_path = "versions/{}".format(archive_name)

    local("mkdir -p versions")
    result = local("tar -czvf {} web_static".format(archive_path), capture=True)
    
    if result.failed:
        return None
    else:
        return archive_path"""

from time import strftime
from datetime import date

def do_pack():
    """ A script that generates archive the contents of web_static folder"""

    filename = strftime("%Y%m%d%H%M%S")
    try:
        local("mkdir -p versions")
        local("tar -czvf versions/web_static_{}.tgz web_static/"
              .format(filename))

        return "versions/web_static_{}.tgz".format(filename)

    except Exception as e:
        return None
