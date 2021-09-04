# /etc/nginx/sites-available/web_rl

server {
    # server_name example.com www.example.com;
    server_name localhost;

    location = /favicon.ico {
        alias /home/gonzalo/dj_web_base/app/staticfiles/favicon.ico; 
        access_log off; 
        log_not_found off; 
        }

    location /static/ {
        autoindex on;
        alias /home/gonzalo/dj_web_base/app/staticfiles/;
        }
    
    location /media/ {
        autoindex on;
        alias /home/gonzalo/dj_web_base/app/media/;
        }

    location / {
        include proxy_params;
        proxy_pass http://unix:/run/web_rl.sock;
    }
}