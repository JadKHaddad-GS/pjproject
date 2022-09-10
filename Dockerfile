FROM debian:11-slim as builder

RUN apt update
RUN apt install -y git gcc make g++ python3 python3-dev swig

WORKDIR /home
RUN git clone https://github.com/JadKHaddad/pjproject.git --depth 1 pjproject
WORKDIR /home/pjproject/pjsip-apps/src/swig/python
RUN apt install -y nano 
RUN apt install -y python3-pip

ENV LD_LIBRARY_PATH /usr/local/lib

COPY pjsip-apps/src/swig/python/setup.py /home/pjproject/pjsip-apps/src/swig/python/setup.py
COPY pjsip-apps/src/swig/python/setup_.py /home/pjproject/pjsip-apps/src/swig/python/setup_.py
COPY pjsip-apps/src/swig/python/Makefile /home/pjproject/pjsip-apps/src/swig/python/Makefile


#RUN python3 setup.py build
#RUN python3 setup.py install

CMD ["/bin/bash"]


# docker build -t debian-slim-builder-test .
# docker run -it --rm debian-slim-builder-test

#swig -I../../../../pjlib/include -I../../../../pjlib-util/include -I../../../../pjmedia/include -I../../../../pjsip/include -I../../../../pjnath/include -c++  -w312  -python -o pjsua2_wrap.cpp ../pjsua2.i