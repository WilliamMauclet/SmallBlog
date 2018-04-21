# RUN <=> CMD

# build from Dockerfile: 
# docker build -t smallblog -f Dockerfile .
# afterwards: 
# docker run smallblog -p 80:80
# winpty docker exec -it <idOrName>


FROM postgres:latest

EXPOSE 80

RUN apt update -y
RUN apt install -y python3-pip git


RUN git clone https://github.com/WilliamMauclet/SmallBlog.git
RUN cd SmallBlog && pip3 install flask flask-sqlalchemy flask-wtf flask-admin py-gfm flask-login gunicorn

CMD cd SmallBlog && python3 app.py