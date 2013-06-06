#-*- encoding: utf-8 -*-
import sys
import ConfigParser

from glanceclient.v1 import client as glanceclient
from glanceclient import exc as glanceexc
from keystoneclient.v2_0 import client as keyclient

try:
    DEBUG = sys.argv[1].lower() == 'true'
except IndexError:
    DEBUG = False


def read_keystone_rc():
    cc = ConfigParser.ConfigParser()
    cc.readfp(file('/etc/nova/api-paste.ini'))

    username = cc.get('filter:authtoken', 'admin_user')
    password = cc.get('filter:authtoken', 'admin_password')
    tenant_name = cc.get('filter:authtoken', 'admin_tenant_name')
    try:
        auth_uri = cc.get('filter:authtoken', 'auth_uri')
    except Exception:
        auth_uri = 'http://0.0.0.0:5000'

    if -1 == auth_uri.rfind('/v2.0'):
        auth_uri = '%s/v2.0' % auth_uri

    cc.readfp(file('/etc/glance/glance-api.conf'))
    try:
        host = cc.get('DEFAULT', 'bind_host')
    except Exception:
        host = '0.0.0.0'

    try:
        port = cc.get('DEFAULT', 'bind_port')
    except Exception:
        port = '9292'

    glance_url = 'http://%s:%s/' % (host, port)

    return (username, password, tenant_name, auth_uri, glance_url)

username, password, tenant_name, keystone_url, glance_url = read_keystone_rc()

if DEBUG:
    print username, password, tenant_name, keystone_url, glance_url

#username = 'demo'
#password = 'demo'
#tenant_name = 'demo'
#keystone_url = 'http://localhost:5000/v2.0'
#glance_url = 'http://localhost:9292'

result = 'success'

try:
    keystone = keyclient.Client(username=username, password=password,
                                tenant_name=tenant_name, auth_url=keystone_url)
    token = keystone.auth_token
    glance = glanceclient.Client(endpoint=glance_url, token=token)

    image = glance.images.create(name='__nvs_monitor__', data='a' * 1024,
                                disk_format='qcow2', container_format='ovf',
                                is_public=False)

    if image.status != 'active':
        print 'create image error. %s' % image

    image.delete()

    try:
        image.get()
    except glanceexc.HTTPNotFound:
        pass
except Exception, ex:
    if DEBUG:
        import traceback
        traceback.print_exc()
    result = 'failed'

print ('result %(result)s != success %(script_name)s %(result)s..' %
       {'result': result, 'script_name': sys.argv[0]})
