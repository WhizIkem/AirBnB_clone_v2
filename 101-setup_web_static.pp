class web_servers {
  package { 'nginx':
    ensure => installed,
  }

  file { '/data/':
    ensure  => directory,
    owner   => 'ubuntu',
    group   => 'ubuntu',
    recurse => true,
  }

  file { '/data/web_static/':
    ensure  => directory,
    owner   => 'ubuntu',
    group   => 'ubuntu',
  }

  file { '/data/web_static/releases/':
    ensure  => directory,
    owner   => 'ubuntu',
    group   => 'ubuntu',
  }

  file { '/data/web_static/shared/':
    ensure  => directory,
    owner   => 'ubuntu',
    group   => 'ubuntu',
  }

  file { '/data/web_static/releases/test/':
    ensure  => directory,
    owner   => 'ubuntu',
    group   => 'ubuntu',
  }

  file { '/data/web_static/releases/test/index.html':
    ensure  => file,
    owner   => 'ubuntu',
    group   => 'ubuntu',
    content => '<html><head></head><body>Holberton School</body></html>',
  }

  file { '/data/web_static/current':
    ensure => link,
    target => '/data/web_static/releases/test/',
    force  => true,
  }

  file { '/etc/nginx/sites-available/default':
    ensure  => file,
    owner   => 'root',
    group   => 'root',
    mode    => '0644',
    content => "
      server {
        listen 80 default_server;
        listen [::]:80 default_server;

        server_name _;

        location /hbnb_static/ {
          alias /data/web_static/current/;
        }

        location / {
          return 404;
        }
      }
    ",
    notify  => Service['nginx'],
  }

  service { 'nginx':
    ensure    => running,
    enable    => true,
    hasstatus => true,
    require   => Package['nginx'],
    subscribe => File['/etc/nginx/sites-available/default'],
  }
}

include web_servers

