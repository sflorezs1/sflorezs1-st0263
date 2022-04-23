# Backend

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
- create a `docker-compose.yml` file and paste the following