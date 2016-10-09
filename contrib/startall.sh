#!/bin/bash
ceph-rest-api -c /etc/ceph/ceph.conf --cluster ceph -i admin &
python manage.py runserver  0.0.0.0:8000 &
