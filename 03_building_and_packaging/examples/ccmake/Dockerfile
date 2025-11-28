From ubuntu:24.04

RUN apt-get -qq update && \
    apt-get -qq -y install \
        build-essential \
        cmake \
        g++ \
        vim \
        tree \
        git \
        cmake-curses-gui \
        libeigen3-dev \
        libxml2-dev \
        libboost-all-dev \
        petsc-dev \
        python3-dev \
        python3-numpy

# This is some strang Docker problem. Normally, you don't need to add /usr/local/lib to LD_LIBRARY_PATH
ENV LD_LIBRARY_PATH $LD_LIBRARY_PATH:/usr/local/lib/

RUN git clone https://github.com/precice/precice.git

CMD ["/bin/bash"]
