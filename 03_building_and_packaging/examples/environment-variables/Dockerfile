From ubuntu:22.04

COPY inittimezone /usr/local/bin/inittimezone

# Run inittimezone and install a few dependencies
RUN apt-get -qq update && \
    inittimezone && \
    apt-get -qq -y install \
        build-essential \
        g++ \
        vim

ADD print_my_environment_variable.sh .
CMD ["/bin/bash"]
