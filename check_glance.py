#!/usr/bin/env python
# configs
username = 'demo'
password = 'demo'
tenant_name = 'demo'
keystone_url = 'http://localhost:5000/v2.0'
glance_url = 'http://localhost:9292'

from glanceclient.v1 import client as glanceclient
from glanceclient import exc as glanceexc
from keystoneclient.v2_0 import client as keyclient


keystone = keyclient.Client(username=username, password=password,
                            tenant_name=tenant_name, auth_url=keystone_url)
token = keystone.auth_token

glance = glanceclient.Client(endpoint=glance_url, token=token)

data = 'balbal' * 100
image = glance.images.create(name='__nvs_monitor__', data=data,
                             disk_format='qcow2', container_format='ovf',
                             is_public=False)

if image.status != 'active':
    print 'create image error. %s' % image
print 'create image success ..'

image.delete()

try:
    image.get()
except glanceexc.HTTPNotFound:
    pass
print 'delete image success ..'
