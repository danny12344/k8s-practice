FROM ubuntu:latest

# Install Nginx and other necessary packages
RUN apt-get update && apt-get install -y nginx

# Copy HTML and JavaScript files to the Nginx document root
# COPY index.html /var/www/html/
# COPY script.js /var/www/html/

# Remove the default NGINX configuration
RUN rm -f /etc/nginx/conf.d/default.conf

# Copy your modified Nginx configuration file
COPY nginx.conf /etc/nginx/nginx.conf

# Copy your HTML and JS files to the appropriate directory
COPY index.html /usr/share/nginx/html/
COPY script.js /usr/share/nginx/html/

# Expose port 8080 for accessing the web server
EXPOSE 8080

# Start Nginx service
CMD ["nginx", "-g", "daemon off;"]
