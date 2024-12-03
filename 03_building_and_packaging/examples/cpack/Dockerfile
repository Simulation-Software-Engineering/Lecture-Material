From ubuntu:24.04

RUN apt-get -qq update && \
    apt-get -qq -y install \
        build-essential \
        cmake \
        g++ \
        vim \
        tree \
        lintian

# This is some strang Docker problem. Normally, you don't need to add /usr/local/lib to LD_LIBRARY_PATH
ENV LD_LIBRARY_PATH $LD_LIBRARY_PATH:/usr/local/lib/

ADD . /helloworld
CMD ["/bin/bash"]
