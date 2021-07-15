FROM python:3.7-alpine
WORKDIR app
COPY . .
RUN pip3 install requests
ENTRYPOINT [ "python3" ]
CMD [ "-u", "client.py" ]
