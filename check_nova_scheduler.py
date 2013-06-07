#!/usr/bin/env python
#-*- encoding: utf-8 -*-

import nova_utils
import utils

try:
    nova_utils.init_nova()
    host = nova_utils.get_random_host()
    utils.log(host)

    info = nova_utils.rpccall_scheduler('show_host_resources', host=host)
    assert info
    utils.log(info)

except Exception:
    utils.print_traceback()
    result = 'failed'
else:
    result = 'success'

utils.print_result(result)
