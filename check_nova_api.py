#!/usr/bin/env python
#-*- encoding: utf-8 -*-

from novaclient.v1_1 import client as novaclient
import utils
import keystone


DEBUG = utils.get_debug()

try:
    user = keystone.Keystone(*utils.get_token_config())
    username, password, tenant_name, keystone_url = utils.get_token_config()
    nova_url = '%s/v1.1/%s' % (utils.get_nova_url(), user.get_tenant_id())
    # keystone_url = 'http://localhost:5000/v2.0'
    # nova_url = 'http://localhost:8774'
    nova = novaclient.Client(username, password, tenant_name,
                                    keystone_url, nova_url, no_cache=True)

    if DEBUG:
        print username, password, tenant_name, keystone_url, nova_url

    vms = nova.servers.list()

    if DEBUG:
        print vms
except Exception:
    utils.print_traceback()
    result = 'failed'
else:
    result = 'success'

utils.print_result(result)
