# This is a slimmed down version of KrakenDash
 I removed the Ops portion, because I just want a slick UI to get status from and pull json data from .

# KrakenCeph 
This can be used to monitor your Ceph Cluster, and hook into your NMS

## Overview

![Status dashboard](https://raw.githubusercontent.com/donnydavis/krakendash/master/screenshots/status.png "Status") 



## Installation and Roadmap


This is used to build a docker image which can be found here https://hub.docker.com/r/automatikdonn/krakenceph/

Install docker on your mon hosts, create a directory to mount the ceph configurations (I used /mnt/kraken as $target_dir) 
Copy over everything from /etc/ceph to $target_dir and then launch the container.
Everything should just work. 

Currently SELinux has to be disabled on the host machine for this container to work. I will get this fixed as soon as I can. 

MON host setup is as follows
'''
export target_dir=/mnt/krakenceph
mkdir $target_dir
rsync -axv /etc/ceph/ $target_dir
setenforce 0 #(Do not make this config permenant, I will be enabling SELinux when I get it sorted out)
'''
Thanks for checking out my fork of https://github.com/krakendash/krakendash

## Milestone One
- [x] Cluster status
- [x] Cluster data usage
- [x] MON status
- [x] OSD status
- [x] PG status
- [x] Better UI
- [x] Multi-MON support
- [x] Migrate from requests to [python-cephclient](https://github.com/dmsimard/python-cephclient/)

## Milestone Two
- [] MON operations
- [] OSD operations
- [] Pool operations
- [] List pools, size
- [] Pool status
- [] View CRUSH map

### Milestone Three
- [] Auth system
- [] User session tracking

### Milestone Four
- [] Collectd integration
- [] Graphite integration
- [] Multi-cluster support
