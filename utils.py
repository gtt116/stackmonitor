import ConfigParser as configParser
import sys


def log(msg):
    if get_debug():
        print msg


def get_debug():
    try:
        debug = sys.argv[1].lower() == 'true'
    except IndexError:
        debug = False

    return debug


def print_traceback():
    if get_debug():
        import traceback
        traceback.print_exc()


def print_result(result):
    print ('result %(result)s != success %(script_name)s %(result)s..' %
           {'result': result, 'script_name': sys.argv[0]})


def get_token_config():
    """
    username = 'demo'
    password = 'demo'
    tenant_name = 'demo'
    keystone_url = 'http://localhost:5000/v2.0'
    """
    cc = ConfigParser('/etc/nova/api-paste.ini')
    username = cc.get('filter:authtoken', 'admin_user')
    password = cc.get('filter:authtoken', 'admin_password')
    tenant_name = cc.get('filter:authtoken', 'admin_tenant_name')
    auth_uri = cc.get('filter:authtoken', 'auth_uri', 'http://0.0.0.0:5000')

    if -1 == auth_uri.rfind('/v2.0'):
        auth_uri = '%s/v2.0' % auth_uri

    ret = (username, password, tenant_name, auth_uri)
    assert all(ret)
    return ret


def get_glance_url():
    """glance_url = 'http://localhost:9292'"""
    cc = ConfigParser('/etc/glance/glance-api.conf')
    host = cc.get('DEFAULT', 'bind_host', '0.0.0.0')
    port = cc.get('DEFAULT', 'bind_port', '9292')
    glance_url = 'http://%s:%s/' % (host, port)
    assert glance_url
    return glance_url


def get_nova_url():
    cc = ConfigParser('/etc/nova/nova.conf')
    host = cc.get('DEFAULT', 'osapi_compute_listen', '0.0.0.0')
    port = cc.get('DEFAULT', 'osapi_compute_listen_port', '8774')
    nova_url = 'http://%s:%s/' % (host, port)
    assert nova_url
    return nova_url


class ConfigParser(object):
    def __init__(self, config_path):
        self.config_path = config_path
        self.cc = configParser.ConfigParser()
        self.cc.readfp(file(config_path))

    def get(self, section, key, default_value=None):
        """
        Get value from key in section, if no such config item, return default
        value."""
        try:
            ret = self.cc.get(section, key)
        except Exception:
            ret = default_value
        return ret
