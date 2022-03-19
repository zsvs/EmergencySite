#!/bin/bash
apt update && apt upgrade -y
apt install nginx -y

cat <<EOF > /var/www/html/index.html
<html>
<h1> Most important emergency info</h1>
<p> I love you</p>
<p> Sincerely yours ${f_name} ${f_time} </p>
EOF

service nginx start
