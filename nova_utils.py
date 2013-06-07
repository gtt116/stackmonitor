import random
from nova import flags
from nova import db
from nova import context

CONF = flags.cfg.CONF


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


def get_network_topic():
    return CONF.network_topic


def get_compute_topic():
    return CONF.compute_topic
