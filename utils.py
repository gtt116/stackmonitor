import ConfigParser


def get_token_config():
    """
    username = 'demo'
    password = 'demo'
    tenant_name = 'demo'
    keystone_url = 'http://localhost:5000/v2.0'
    """
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

    return (username, password, tenant_name, auth_uri)


def get_glance_url():
    """glance_url = 'http://localhost:9292'"""
    cc = ConfigParser.ConfigParser()
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
    return glance_url
