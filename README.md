This application contains following things:
- Flask Counter application: Return the count of requests
- Client Application: This app hit the nginx loadbalancer at an interval 5 sec
- Nginx loadbalancer

To run the application
- `docker-compose build --no-cache` - To build the images
- `docker-compose up -d` -  To run the container in background

To see the logs use:
- `docker logs <client-container> -f`

