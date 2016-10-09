#!/bin/bash
cat >> /etc/ceph/ceph.conf << EOF
[client.admin]
keyring = /etc/ceph/ceph.client.admin.keyring
public addr = 0.0.0.0:15678
EOF
ceph-rest-api -c /etc/ceph/ceph.conf --cluster ceph -i admin &
python /app/manage.py runserver  0.0.0.0:9091 
