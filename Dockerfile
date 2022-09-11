FROM debian:11-slim as builder

RUN apt update
RUN apt install -y git gcc make g++ python3 python3-dev swig

WORKDIR /home
RUN apt install -y nano 
RUN apt install -y python3-pip

ENV LD_LIBRARY_PATH /usr/local/lib

#RUN mkdir /home/symbols

#RUN git clone https://github.com/JadKHaddad/pjproject.git --depth 1 pjproject
#WORKDIR /home/pjproject

#RUN ./configure --enable-shared && make dep && make && make install

#RUN python3 setup.py build
#RUN python3 setup.py install

COPY setup_.py /home/setup_.py
#COPY helper.mak /home/pjproject/helper.mak

CMD ["/bin/bash"]


# docker build -t debian-slim-builder-test . && docker run -it debian-slim-builder-test
# docker run -it --rm debian-slim-builder-test
# pip3 install git+https://github.com/JadKHaddad/pjproject.git

#swig -I./pjlib/include -I./pjlib-util/include -I./pjmedia/include -I./pjsip/include -I./pjnath/include -c++  -w312  -python -o pjsua2_wrap.cpp ./pjsua2.i
#swig -I./pjlib/include -I./pjlib-util/include -I./pjmedia/include -I./pjsip/include -I./pjnath/include -c++  -w312  -python -o pjsua2_wrap.cpp ./pjsua2.i