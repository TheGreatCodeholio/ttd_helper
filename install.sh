# installer Helper for ttd helper requires sudo

read -p "Would you like to install nginx, mysql and php? " -n 1 -r
echo    # (optional) move to a new line
if [[ ! $REPLY =~ ^[Yy]$ ]]
then
    exit 1
else
  sudo apt install nginx mariadb-server php7.3-fpm php7.3-mysql
fi
read -p "Would you like to configure mysql and nginx for ttd_helper calls? " -n 1 -r
echo    # (optional) move to a new line
if [[ ! $REPLY =~ ^[Yy]$ ]]
then
    exit 1
else
  sudo mysql -e "create database ttd_helper"
  sudo mysql -e "create user 'ttd_helper'@'localhost' identified by 'reThd68eVVC9YQVc'"
  sudo mysql -e "grant all privileges on ttd_helper.* to ttd_helper@localhost"
  sudo mysql -e "flush privileges"
  sudo mysql ttd_helper < mysql_nginx_config/ttd_calls.sql
  sudo rm -rf /etc/nginx/sites-available/default
  sudo cp mysql_nginx_config/default /etc/nginx/sites-available/default
  cd public_html
  sudo rm -rf /var/www/html
  sudo ln -s "$(pwd -P)" /var/www/html
  sudo service nginx restart
fi