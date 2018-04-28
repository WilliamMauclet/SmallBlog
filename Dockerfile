#FROM postgres:alpine
FROM alpine:latest

EXPOSE 80

RUN apk update
RUN apk add git
 
# thanks to: https://github.com/frol/docker-alpine-python3/blob/master/Dockerfile
RUN apk add --no-cache python3 && \
    python3 -m ensurepip && \
    rm -r /usr/lib/python*/ensurepip && \
    pip3 install --upgrade pip setuptools && \
    if [ ! -e /usr/bin/pip ]; then ln -s pip3 /usr/bin/pip ; fi && \
    if [[ ! -e /usr/bin/python ]]; then ln -sf /usr/bin/python3 /usr/bin/python; fi && \
    rm -r /root/.cache

RUN apk add sqlite

RUN git clone https://github.com/WilliamMauclet/SmallBlog.git
RUN cd SmallBlog && pip3 install flask flask-sqlalchemy flask-wtf flask-admin py-gfm flask-login gunicorn

# TODO replace $password$ here LOCALLY to pass to application
CMD cd SmallBlog && python3 prefiller.py hello 

CMD cd SmallBlog && python3 app.py

# $ docker build . -t smallblog
# $ docker run -p 80:80 smallblog