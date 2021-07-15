This application contains following things:
- Flask Counter application: Return the count of requests
- Client Application: This app hit the nginx loadbalancer at an interval 5 sec
- Nginx loadbalancer

To run the application
- `docker-compose build --no-cache`
- `docker-compose up`

To see the logs use:
- `docker logs <client-container> -f`

