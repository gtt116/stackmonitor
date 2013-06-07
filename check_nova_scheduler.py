#!/usr/bin/env python
#-*- encoding: utf-8 -*-

import nova_utils
import utils
from nova.scheduler import rpcapi

try:
    nova_utils.init_nova()
    nova_utils.set_rpc_timeout()
    c = nova_utils.get_admin_context()
    sche_api = rpcapi.SchedulerAPI()

    host = nova_utils.get_random_host()
    utils.log(host)

    info = sche_api.show_host_resources(c, host)
    assert info
    utils.log(info)

except Exception:
    utils.print_traceback()
    result = 'failed'
else:
    result = 'success'

utils.print_result(result)
