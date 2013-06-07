#!/usr/bin/env python
#-*- encoding: utf-8 -*-

import nova_utils
import utils

try:
    nova_utils.init_nova()
    info = nova_utils.rpccall_compute('get_console_pool_info',
                                      console_type='novnc')
    assert info
    utils.log(info)

except Exception:
    utils.print_traceback()
    result = 'failed'
else:
    result = 'success'

utils.print_result(result)
