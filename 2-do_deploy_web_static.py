#!/usr/bin/python3
"""
Fabric script that distributes an archive to your web servers
using the function do_deploy
"""
from fabric.api import env, put, run
from os.path import exists

env.hosts = ['100.25.117.48', '54.146.58.123']
env.user = 'ubuntu'
env.key_filename = '~/.ssh/id_rsa'

def do_deploy(archive_path):
    if not exists(archive_path):
        return False

    try:
        # Upload the archive to the /tmp/ directory of the web server
        put(archive_path, '/tmp/')

        # Extract the archive to the folder /data/web_static/releases/<archive filename without extension>
        filename = archive_path.split('/')[-1]
        folder_name = '/data/web_static/releases/' + filename.split('.')[0]
        run('mkdir -p {}'.format(folder_name))
        run('tar -xzf /tmp/{} -C {}'.format(filename, folder_name))
        
        # Remove the archive from the web server
        run('rm /tmp/{}'.format(filename))
        
        # Delete the symbolic link /data/web_static/current
        run('rm -f /data/web_static/current')

        # Create a new symbolic link /data/web_static/current to the new version of the code
        run('ln -s {} /data/web_static/current'.format(folder_name))

        print("New version deployed!")
        return True
    except:
        return False
