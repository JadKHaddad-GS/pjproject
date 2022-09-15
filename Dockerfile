FROM debian:11-slim as builder

RUN apt update
RUN apt install -y git python3 python3-pip python3-dev gcc g++ make swig

WORKDIR /home

RUN pip3 install git+https://github.com/JadKHaddad/pjproject.git

ENV LD_LIBRARY_PATH /usr/local/lib

COPY example.py /home/example.py

CMD ["/bin/bash"]

# export LD_LIBRARY_PATH=/usr/local/lib
# docker build -t debian-slim-builder-test . && docker run -it debian-slim-builder-test
