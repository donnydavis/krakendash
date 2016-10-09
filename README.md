# This is a slimmed down version of KrakenDash
 I removed the Ops portion, because I just want a slick UI to get status from and pull json data from.

    I refactored this app to run in a fedora docker container, and as long as you use the commands below, your dashboard should just work.
    I changed the default ports for the app so they don't conflict with an Openstack deployment 

# KrakenCeph 
This can be used to monitor your Ceph Cluster, and hook into your NMS

## Overview

![Status dashboard](https://raw.githubusercontent.com/donnydavis/krakendash/master/screenshots/status.png "Status") 



## Installation and Roadmap


This is used to build a docker image which can be found here https://hub.docker.com/r/automatikdonn/krakenceph/

Install docker on your mon hosts, create a directory to mount the ceph configurations (I used /mnt/krakenceph as $target_dir) 
Copy over everything from /etc/ceph to $target_dir and then launch the container.
Everything should just work as long as port 5000 aren't already being used and port 8000 aren't already being used. 

## For some reason my variable doesn't work for SELinux, so just make use if you use a different directory you change it for the selinux commands. 


MON host setup is as follows
```
yum -y install docker rsync
systemctl enable docker
systemctl start docker
export target_dir=/mnt/krakenceph
mkdir $target_dir
rsync -axv /etc/ceph/ $target_dir
chmod -R 600 $target_dir
semanage fcontext -a -t svirt_sandbox_file_t "/mnt/krakenceph(/.*)?"
restorecon -Rv /mnt/krakenceph
docker run --name krakenceph -d -v $target_dir:/etc/ceph -p 9091:9091 automatikdonn/krakenceph /bin/sh -c /app/contrib/startall.sh
```
Thanks for checking out my fork of https://github.com/krakendash/krakendash

