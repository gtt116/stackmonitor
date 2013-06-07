#!/usr/bin/env python
#-*- encoding: utf-8 -*-

"""
Get all network info from nova-network through RPC call to make
sure it is health.
"""

from nova.openstack.common import rpc
import nova_utils
import utils

DEBUG = utils.get_debug()

try:
    nova_utils.init_nova()
    ctxt = nova_utils.get_admin_context()

    net_topic = nova_utils.get_network_topic()
    host = nova_utils.get_hostname()
    utils.log(net_topic)
    utils.log(host)

    network_info = rpc.call(ctxt,
                            rpc.queue_get_for(ctxt, net_topic, host),
                            {'method': 'get_all_networks'})
    assert network_info
    utils.log(network_info)
except Exception:
    if DEBUG:
        utils.print_traceback()
    result = 'failed'
else:
    result = 'success'

utils.print_result(result)
