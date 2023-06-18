# NGINX K8s Learnning

## Build docker image

```Dockerfile
FROM ubuntu:latest

# Install Nginx and other necessary packages
RUN apt-get update && apt-get install -y nginx

# Remove the default NGINX configuration
RUN rm -f /etc/nginx/conf.d/default.conf

# Copy your HTML and JS files to the appropriate directory
COPY index.html /usr/share/nginx/html/
COPY script.js /usr/share/nginx/html/

# Expose port 8080 for accessing the web server
EXPOSE 8080

# Start Nginx service
CMD ["nginx", "-g", "daemon off;"]
```

Build & run docker image:

```bash
docker build -t nginx-webhost .
```

```bash
docker build -t websiteapi .
docker run -d -p 8080:8080 websiteapi
```


```bash
docker run -d -p 8080:80 webhost-test6
```
```bash
docker run -d -p 8080:80 --platform linux/amd64 latest-ubuntu-test-2
```


To enter the docker container:

```bash
docker exec -it 0a7215479110b7d43737169cee1e6f8121eaf7367b82b1aaf359b6bf824c07ee /bin/bash
```



To delete docker container:

```bash
docker stop 0a7215479110b7d43737169cee1e6f8121eaf7367b82b1aaf359b6bf824c07ee && docker rm 0a7215479110b7d43737169cee1e6f8121eaf7367b82b1aaf359b6bf824c07ee
```


TO CHECK PORT IS OPEN ON LOCAL MACHINE:
```bash
nc -zv localhost 8080
```


## 




### Errors / Debugging
This commannd runs the docker container & connects the ports internal container 80 to the external port 8080 of local machine - in theory allowing you to connected to container by navigating to localhost:8080 on local machine - currently getting connection was reset error on the webpage
```bash
docker run -d -p 8080:80 nginx-webhost-test
```