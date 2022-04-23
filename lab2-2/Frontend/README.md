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

