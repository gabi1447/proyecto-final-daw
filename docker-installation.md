# Commands for docker installation

## Install Docker Daemon
```bash
sudo apt install docker.io
sudo apt install docker-compose
```

## Add permissions to current user to execute docker commands without using sudo
```bash
# Add group if it doesn't exist
sudo groupadd docker
# Add user to group
sudo usermod -aG docker $USER
# Apply changes
newgrp docker
```
