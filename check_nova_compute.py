#!/usr/bin/env python
#-*- encoding: utf-8 -*-

from nova import compute
import nova_utils
import utils

try:
    nova_utils.init_nova()
    nova_utils.set_rpc_timeout()
    c = nova_utils.get_admin_context()
    compute_rcpapi = compute.rpcapi.ComputeAPI()

    host = nova_utils.get_hostname()
    utils.log(host)

    info = compute_rcpapi.get_console_pool_info(c, 'novnc', host)
    assert info
    utils.log(info)

except Exception:
    utils.print_traceback()
    result = 'failed'
else:
    result = 'success'

utils.print_result(result)
