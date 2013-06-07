#!/usr/bin/env python
#-*- encoding: utf-8 -*-

"""
Get all network info from nova-network through RPC call to make
sure it is health.
"""

from nova import network
import nova_utils
import utils

DEBUG = utils.get_debug()

try:
    nova_utils.init_nova()
    ctxt = nova_utils.get_admin_context()
    network_api = network.api.API()
    assert network_api.get_all(ctxt)
except Exception:
    if DEBUG:
        utils.print_traceback()
    result = 'failed'
else:
    result = 'success'

utils.print_result(result)
