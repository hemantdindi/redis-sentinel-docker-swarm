sudo apt-get update -y && sudo apt-get upgrade -y
sudo apt-get install apt-transport-https software-properties-common ca-certificates -y
sudo wget https://download.docker.com/linux/ubuntu/gpg && sudo apt-key add gpg
sudo echo "deb [arch=amd64] https://download.docker.com/linux/ubuntu xenial stable" >> /etc/apt/sources.list
sudo apt-get update -y
sudo apt-get install docker-ce -y
sudo systemctl start docker && sudo systemctl enable docker
sudo ufw disable
sudo systemctl restart docker
sudo apt install python-pip -y
sudo pip install redis
