import random
from nova import flags
from nova import db
from nova import context
from nova.openstack.common import rpc

CONF = flags.cfg.CONF
rpc_timeout = 10


def init_nova():
    flags.parse_args([])


def get_admin_context():
    return context.get_admin_context()


def get_hostname():
    return CONF.host


def set_rpc_timeout():
    """Make sure it is invoked after `init_nova`. otherwise
    I will failed"""
    CONF.rpc_response_timeout = 10


def get_hosts():
    c = get_admin_context()
    return [service.host for service in db.service_get_all(c)]


def get_random_host():
    hosts = get_hosts()
    random.shuffle(hosts)
    assert hosts
    return hosts[0]


def get_network_topic(host=None):
    c = get_admin_context()
    if host:
        return rpc.queue_get_for(c, CONF.network_topic, host)
    return CONF.network_topic


def get_compute_topic(host=None):
    c = get_admin_context()
    if host:
        return rpc.queue_get_for(c, CONF.compute_topic, host)
    return CONF.compute_topic


def rpccall_network(method, **kwargs):
    c = get_admin_context()
    host = get_hostname()
    return rpc.call(c, get_network_topic(host),
                    {'method': method, 'args': kwargs},
                    timeout=rpc_timeout)


def rpccall_compute(method, **kwargs):
    c = get_admin_context()
    host = get_hostname()
    return rpc.call(c, get_compute_topic(host),
                    {'method': method, 'version': '2.0', 'args': kwargs},
                    timeout=rpc_timeout)
