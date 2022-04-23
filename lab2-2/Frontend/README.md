# Frontend
On the other VPC...
## Instructions
### Create the machine image from the provided `Dockerfile`
```bash
# build the image
docker build -t <dockerhub-id>/bookstore-frontend:latest .
# upload the image to your dockerhub
docker push <dockerhub-id>/bookstore-frontend:latest
```

### Create first machine
- Create a new GCP Compute Engine Virtual Machine using the image `generic-docker-image`. And name it `frontend-1`.
- SSH into it and run:
    ```bash
    docker run --env-file .env --name bookstore-frontend -p 80:80 -d --restart unless-stopped -t <dockerhub-id>/bookstore-frontend:latest
    ```
- Hooray! Your first frontend is running now
- Create an image based on the machine:  
    ![Machine row](Images/machine-row.jpg)  
    ![Context Menu](Images/create-image.jpg)  
    Name it `backend-image`  
    Click `Create`  
    ![Create button](Images/create-button.jpg)  
- Wait for the image to create and hit the refresh button to check its status.
- Congrats! your image is now created.
### Create second machine
- Create a new GCP Compute Engine Virtual Machine using the image `frontent-image`. And name it `frontent-2`.
- That's it! Yay!

### Load balancer
- Create a new GCP Compute Engine Virtual Machine using the image `generic-docker-image`. And name it `frontend-balancer`.
- Reserve the external IP for this machine so it becomes static.
- Get a domain, create a dns register for `www.domain.com` (and optionally `domain.com`) pointing to the external ip of this machine and follow [this tutorial](https://github.com/st0263eafit/st0263-2261/tree/main/docker-nginx-wordpress-ssl-letsencrypt) to get a certificate and enable ssl on this machine. 
- SSH into it and run:
    ```bash
    sudo apt install docker-compose
    mkdir balancer
    cd balancer
    ```
- Edit the `nginx.conf` to enable load balancing, we need to specify the internal IPs for the two frontend nodes. For this config we are using a main server and a failover. Replace the `<FRONTEND_NODE_1_IP>`, `<FRONTEND_NODE_1_IP>` and `<https://back.domain.com/api/>` variables.
    ```bash
    worker_processes auto;
    error_log /var/log/nginx/error.log;
    pid /run/nginx.pid;

    events {
        worker_connections  1024;  ## Default: 1024
    }
    http {

        upstream frontend {
            server <FRONTEND_NODE_1_IP>:80 down;
            server <FRONTEND_NODE_1_IP>:80 backup;
        }

        server {
            listen 80;
            listen [::]:80;

            server_name _;
            rewrite ^ https://$host$request_uri permanent;
        }

        server {
            listen 443 ssl http2 default_server;
            listen [::]:443 ssl http2 default_server;

            server_name _;

            # enable subfolder method reverse proxy confs
            #include /config/nginx/proxy-confs/*.subfolder.conf;

            # all ssl related config moved to ssl.conf
            include /etc/nginx/ssl.conf;

            client_max_body_size 0;

            location / {
                proxy_pass http://frontend;
                proxy_redirect off;
                proxy_set_header Host $host;
                proxy_set_header X-Real-IP $remote_addr;
                proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
                proxy_set_header X-Forwarded-Host $host;
                proxy_set_header X-Forwarded-Server $host;
                proxy_set_header X-Forwarded-Proto $scheme;
            }

            location /api/ {
                proxy_pass <https://back.domain.com/api/>;
            }
        }
    }
    ```
- create a `docker-compose.yml` file and paste the following
- run:
    ```bash
    docker-compose up
    ```