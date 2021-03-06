# /etc/nginx/sites-available/redlinegs

server {
    server_name redlinegs.com www.redlinegs.com;
    
    location = /favicon.ico {
        alias /root/web_rl/app/staticfiles/favicon.ico; 
        access_log off; 
        log_not_found off; 
        }

    location /static/ {
        autoindex on;
        alias /root/web_rl/app/staticfiles/;
        }
    
    location /media/ {
        autoindex on;
        alias /root/web_rl/app/media/;
        }

    location / {
        include proxy_params;
        proxy_pass http://unix:/run/web_rl.sock;
    }
}
