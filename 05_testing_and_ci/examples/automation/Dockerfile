FROM alpine:3.15.0

# Install Python and make sure that we can call it 
# as `python` instead of `python3`
RUN apk add --no-cache python3 \
    && ln -sf python3 /usr/bin/python

# pip should be installed and used as a user. Therefore we 
# create a new user "testuser" and change to this user.
RUN addgroup -g 1000 testuser \
    && adduser -u 1000 -G testuser -D testuser
USER testuser

# Install pip, make sure it can be called as `pip` instead of
# `pip3``. The installation location of `pip` has to be added
# to the path. Afterwards, we can install missing tools via 
# `pip`.
ENV PATH=/home/testuser/.local/bin:${PATH}
RUN python -m ensurepip --upgrade \
    && ln -sf /home/testuser/.local/bin/pip3 /home/testuser/.local/bin/pip \
    && pip install --upgrade pip
RUN pip install black

ENTRYPOINT ["/bin/sh"]
