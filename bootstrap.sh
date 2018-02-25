#!/usr/bin/env bash

curl -sL https://deb.nodesource.com/setup_8.x | bash -
apt-get install -y python3-pip nodejs postgresql postgresql-contrib
npm install -g gulp

cd /vagrant
pip3 install -r requirements.txt

mkdir /home/vagrant/vagrant_node_modules
mount --bind /home/vagrant/vagrant_node_modules /vagrant/node_modules
npm install --unsafe-perm

su postgres -c "psql -c \"CREATE ROLE vagrant SUPERUSER LOGIN PASSWORD 'vagrant'\" "
echo "export DATABASE_HOST=localhost" >> /home/vagrant/.profile
echo "export DATABASE_USER=vagrant" >> /home/vagrant/.profile
echo "export DATABASE_PASSWORD=vagrant" >> /home/vagrant/.profile
