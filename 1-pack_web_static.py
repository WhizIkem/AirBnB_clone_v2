#!/usr/bin/python3
# Fabric script that generates a .tgz archive from the contents of the web_static folder of your AirBnB Clone repo, using the function do_pack

from fabric.api import run, local, sudo
from datetime import datetime

n = datetime.now()


def do_pack():
    """Packs"""

    fn = 'versions/web_static_{}{}{}{}{}{}.tgz'\
        .format(n.year, n.month, n.day, n.hour, n.minute, n.second)
    local('mkdir -p versions')
    command = local("tar -cvzf " + fn + " ./web_static/")
    if command.succeeded:
        return fn
    return None
