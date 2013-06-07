#!/usr/bin/env python
#-*- encoding: utf-8 -*-

"""
Get all network info from nova-network through RPC call to make
sure it is health.
"""

import nova_utils
import utils

DEBUG = utils.get_debug()

try:
    nova_utils.init_nova()
    network_info = nova_utils.rpccall_network('get_all_networks')
    assert network_info
    utils.log(network_info)
except Exception:
    if DEBUG:
        utils.print_traceback()
    result = 'failed'
else:
    result = 'success'

utils.print_result(result)
