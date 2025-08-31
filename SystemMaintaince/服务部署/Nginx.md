# Nginx

## Installation and Config

### **Install**

```bash
sudo apt update
sudo apt install nginx
```

**Check status**

```bash
sudo systemctl status nginx
```

You can enable auto luanch when system on

```bash
sudo systemctl enable --now nginx
```

### **Configuration**

The config files path is `/etc/nginx`, here you can see core config files of nginx.

```bash
cacc@purgatory-v /etc/nginx
0 % ll
total 68K
drwxr-xr-x 2 root root 4.0K Feb 15  2025 conf.d
-rw-r--r-- 1 root root 1.1K May 31  2023 fastcgi.conf
-rw-r--r-- 1 root root 1.1K May 31  2023 fastcgi_params
-rw-r--r-- 1 root root 2.8K May 31  2023 koi-utf
-rw-r--r-- 1 root root 2.2K May 31  2023 koi-win
-rw-r--r-- 1 root root 3.9K May 31  2023 mime.types
drwxr-xr-x 2 root root 4.0K Feb 15  2025 modules-available
drwxr-xr-x 2 root root 4.0K Aug 20 14:08 modules-enabled
-rw-r--r-- 1 root root 1.5K May 31  2023 nginx.conf
-rw-r--r-- 1 root root  180 May 31  2023 proxy_params
-rw-r--r-- 1 root root  636 May 31  2023 scgi_params
drwxr-xr-x 2 root root 4.0K Aug 20 14:30 sites-available
drwxr-xr-x 2 root root 4.0K Aug 20 13:57 sites-enabled
drwxr-xr-x 2 root root 4.0K Aug 20 13:17 snippets
-rw-r--r-- 1 root root  664 May 31  2023 uwsgi_params
-rw-r--r-- 1 root root   43 Aug 20 13:59 webdav.passwd
-rw-r--r-- 1 root root 3.0K May 31  2023 win-utf
```

The websites configs are in `sites-available` directory, and if you wanna enable the specific site you just need to create a link to the `sites-enabled` and restart the nginx server.

```bash
sudo ln -s /etc/nginx/sites-available/your_site_config /etc/nginx/sites-enabled/
```



## Site Configuration

### Basic HTTP Site

A common http web site looks like

```ini
# /etc/nginx/sites-available/default (or your own .conf file)
server {
    listen 80;                     # Listen on port 80 for HTTP
    server_name example.com www.example.com;  # Your domain

    root /var/www/html;            # Root directory for your site
    index index.html index.htm;    # Default files to serve

    # Logging
    access_log /var/log/nginx/access.log;
    error_log /var/log/nginx/error.log;

    # Main location block
    location / {
        try_files $uri $uri/ =404;  # Try to serve file or directory, else 404
    }

    # Optional: Redirect / to /index.html
    # location = / {
    #     index index.html;
    # }

    # Optional: Custom error pages
    error_page 404 /404.html;
    location = /404.html {
        internal;
    }

    error_page 500 502 503 504 /50x.html;
    location = /50x.html {
        internal;
    }
}
```

### Webdav

```ini
server {
    listen 80;
    server_name example.com;

    root /var/www/webdav;   # The folder you want to share
    autoindex on;           # Optional: show directory listing

    # Enable WebDAV methods
    dav_methods PUT DELETE MKCOL COPY MOVE;
    dav_ext_methods PROPFIND OPTIONS;

    create_full_put_path on;  # Create directories if PUT path doesn't exist
    client_max_body_size 100M; # Max upload size

    auth_basic "Restricted";           # Enable basic authentication
    auth_basic_user_file /etc/nginx/.htpasswd; # Password file

    location / {
        # Handle WebDAV requests
        dav_access user:rw group:rw all:r;
    }

    # Optional: logging
    access_log /var/log/nginx/webdav.access.log;
    error_log /var/log/nginx/webdav.error.log;
}

```

