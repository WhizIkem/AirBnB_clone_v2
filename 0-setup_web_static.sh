#!/usr/bin/env bash
# Bash script that sets up your web servers for the deployment of web_static

sudo apt-get update
sudo apt-get install nginx

sudo mkdir -p /data/
sudo mkdir -p /data/web_static/
sudo mkdir -p /data/web-static/releases/
sudo mkdir -p /data/web_static/shared/
sudo mkdir -p /data/web_static/releases/test/

file_path="/data/web_static/releases/test/index.html"
# Create the directory if it doesn't exist
sudo mkdir -p "$(dirname "$file_path")"
# Create the fake HTML file
sudo echo "<html>
<head>
</head>
<body>
<h1>Holberton School</h1>
</body>
</html>" > "file_path"

link_path="/data/web_static/current"
target_path="/data/web_static/releases/test/"
# Check if the symbolic link exists
if [ -L "$link_path" ]; then
    # Delete the existsing symbolic link
    rm "$link_path"
fi
# Create the symbolic link
sudo ln -s "$target_path" "$link_path"

sudo chown -R ubuntu:ubuntu /data/

sudo sed -i '/server_name .*;/a location /hbnb_static/ {\nalias /data/web_static/current/;\nindex index.html;\n}' /etc/nginx/sites-available/default

sudo service nginx restart

exit 0
