from nova import flags
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
