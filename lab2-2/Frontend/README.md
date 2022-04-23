# Frontend

## Instructions
### Create the machine image from the provided `Dockerfile`
```bash
# build the image
docker build -t <dockerhub-id>/bookstore-frontend:latest .
# upload the image to your dockerhub
docker push <dockerhub-id>/bookstore-frontend:latest
```

### Setup env


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