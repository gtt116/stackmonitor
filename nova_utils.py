from nova import flags
from nova import context


def init_nova():
    flags.parse_args([])


def get_admin_context():
    return context.get_admin_context()
