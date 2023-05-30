#!/usr/bin/env bash
# Bash script that sets up your web servers for the deployment of web_static

# Install Nginx if not already installed
if ! command -v nginx &> /dev/null; then
	sudo apt-get -y update
	sudo apt-get -y install nginx
fi

# Create the necessary folders
web_static_dir="/data/web_static"
releases_dir="${web_static_dir}/releases"
shared_dir="${web_static_dir}/shared"
test_dir="${releases_dir}/test"
index_file="${test_dir}/index.html"

mkdir -p "${web_static_dir}"
mkdir -p "${releases_dir}"
mkdir -p "${shared_dir}"
mkdir -p "${test_dir}"

# Create the fake HTML file
sudo echo "<html>
<head>
</head>
<body>
<h1>Holberton School</h1>
</body>
</html>" > "${index_file}"

# Create symbolic link
current_dir="${web_static_dir}/current"

# Check if the symbolic link exists
if [ -L "${current_dir}" ]; then
    # Delete the existsing symbolic link
    rm "${current_dir}"
fi
# Create the symbolic link
sudo ln -s "${test_dir}" "${current_dir}"

# Set ownership
sudo chown -R ubuntu:ubuntu /data/

# Update Nginx configuration
config_file="/etc/nginx/sites-available/default"
nginx_alias="location /hbnb_static/ { alias ${current_dir}/; }"
if ! grep -q "${nginx_alias}" "${config_file}"; then
	sudo sed -i "/server_name _;/a ${nginx_alias}" "${config_file}"
fi

# Restart Nginx
sudo service nginx restart

exit 0
