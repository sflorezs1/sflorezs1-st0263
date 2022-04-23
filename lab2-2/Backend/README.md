# Backend
## Introduction
Some modifications were done to the source code to enable CORS.
## Instructions
### Create the machine image from the provided `Dockerfile`
```bash
# build the image
docker build -t <dockerhub-id>/bookstore-backend:latest .
# upload the image to your dockerhub
docker push <dockerhub-id>/bookstore-backend:latest
```

### Setup env
Create a `.env` file in the home of the user and set the following variable.
```bash
URL_DB_CONNECTION=mongodb://bookmaster:password@<MONGO_PRIMARY_IP>:27017,<MONGO_SECONDARY_1_IP>:27017,<MONGO_SECONDARY_2_IP>:27017/bookstore?replicaSet="dev-rs0"
```
Here we use the internal IPs for the mongo machines as they are in the same VPC.

### Create first machine
- Create a new GCP Compute Engine Virtual Machine using the image `generic-docker-image`. And name it `backend-1`.
- SSH into it and run:
    ```bash
    docker run --env-file .env --name bookstore-backend -p 80:80 -d --restart unless-stopped -t <dockerhub-id>/bookstore-backend:latest
    ```
- Test the api
    ```bash
    curl 0.0.0.0:80
    ```  
    It should respond with `API is running...`.  
- Hooray! Your first backend is running now
- Create an image based on the machine:  
    ![Machine row](Images/machine-row.jpg)  
    ![Context Menu](Images/create-image.jpg)  
    Name it `backend-image`  
    Click `Create`  
    ![Create button](Images/create-button.jpg)  
- Wait for the image to create and hit the refresh button to check its status.
- Congrats! your image is now created.

### Create second machine
- Create a new GCP Compute Engine Virtual Machine using the image `backend-image`. And name it `backend-2`.
- That's it! Yay!

### Load balancer
- Create a new GCP Compute Engine Virtual Machine using the image `generic-docker-image`. And name it `backend-balancer`.
- Reserve the external IP for this machine so it becomes static.
- Get a domain, create a dns register for `back.domain.com` pointing to the external ip of this machine and follow [this tutorial](https://github.com/st0263eafit/st0263-2261/tree/main/docker-nginx-wordpress-ssl-letsencrypt) to get a certificate and enable ssl on this machine. 
- SSH into it and run:
    ```bash
    sudo apt install docker-compose
    mkdir balancer
    cd balancer
    ```
- Edit the `nginx.conf` to enable load balancing, we need to specify the internal IPs for the two backend nodes. For this config we are using a main server and a failover. Replace the `<BACKEND_NODE_1_IP>` and `<BACKEND_NODE_1_IP>` variables.
    ```bash
    worker_processes auto;
    error_log /var/log/nginx/error.log;
    pid /run/nginx.pid;

    events {
        worker_connections  1024;  ## Default: 1024
    }

    http {

        upstream backend {
            server <BACKEND_NODE_1_IP>:80 down;
            server <BACKEND_NODE_1_IP>:80 backup;
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
                proxy_pass http://backend;
                proxy_redirect off;
                proxy_set_header Host $host;
                proxy_set_header X-Real-IP $remote_addr;
                proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
                proxy_set_header X-Forwarded-Host $host;
                proxy_set_header X-Forwarded-Server $host;
                proxy_set_header X-Forwarded-Proto $scheme;
            }
        }
    }
    ```
- create a `docker-compose.yml` file and paste the following
- run:
    ```bash
    docker-compose up
    ```