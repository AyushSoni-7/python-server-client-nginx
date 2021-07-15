FROM python:3.7-alpine
WORKDIR app
COPY . . 
RUN pip3 install flask
ENTRYPOINT [ "python3" ]
CMD [ "app.py" ]
