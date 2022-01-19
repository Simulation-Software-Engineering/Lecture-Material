#!/usr/bin/env bash


apt-get update
apt-get install -y vim tmux fonts-powerline git

# Get config
git clone https://github.com/ajaust/dotfiles.git "${HOME}/dotfiles"
pushd ${HOME}/dotfiles && ./setup_dotfiles.sh && popd

# Docker
apt-get install -y ca-certificates curl gnupg lsb-release
# Add key
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg
# Set up stable repository
echo \
    "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu \
      $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

# Install Docker engine
apt-get update
apt-get install -y docker-ce docker-ce-cli containerd.io

# Add user to docker group for sudoless Docker
# Note: The change in usergroup is only picked up after
# the VM has been stopped and restarted, i.e., run
#
# vagrant halt
# vagrant up
#
# after the setup finished. The `docker` commands below
# work since we have super user # right during the
# bootstrapping.
usermod -aG docker vagrant

# Test installation
docker run hello-world

# Install act
curl https://raw.githubusercontent.com/nektos/act/master/install.sh | sudo bash

# Install GitLab runner
docker run -d --name gitlab-runner --restart always \
           -v /srv/gitlab-runner/config:/etc/gitlab-runner \
           -v /var/run/docker.sock:/var/run/docker.sock \
           gitlab/gitlab-runner:latest
