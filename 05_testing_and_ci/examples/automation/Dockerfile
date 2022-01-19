# Use Alpine Linux to get images of minimal size. Alpine is
# optimized for containerized applications and normally creates
# container much smaller than other base images/Linux distributions.
FROM alpine:3.15.0

# Install Python and make sure that we can call it
# as `python` instead of `python3`
RUN apk add --no-cache python3 sudo \
    && ln -sf python3 /usr/bin/python

# pip should be installed and used as a user. Therefore we
# create a new user "testuser" and change to this user.
ARG USER_NAME=testuser
RUN addgroup -g 1000 $USER_NAME \
    && adduser -u 1000 -G $USER_NAME -D $USER_NAME
RUN echo "$USER_NAME" ALL=\(root\) NOPASSWD:ALL > "/etc/sudoers.d/$USER_NAME" && \
    chmod 0440 "/etc/sudoers.d/$USER_NAME"
USER $USER_NAME

# Install pip, make sure it can be called as `pip` instead of
# `pip3``. The installation location of `pip` has to be added
# to the path. Afterwards, we can install missing tools via
# `pip`.
ENV PATH=/home/$USER_NAME/.local/bin:${PATH}
RUN python -m ensurepip --upgrade \
    && ln -sf /home/$USER_NAME/.local/bin/pip3 /home/$USER_NAME/.local/bin/pip \
    && pip install --upgrade pip
RUN pip install --user black

CMD ["/bin/sh"]
