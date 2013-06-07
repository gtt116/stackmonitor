#!/usr/bin/env python
#-*- encoding: utf-8 -*-

from glanceclient.v1 import client as glanceclient
from glanceclient import exc as glanceexc

import utils
import keystone

DEBUG = utils.get_debug()


def main():
    try:
        username, password, tenant_name, keystone_url = \
                                                    utils.get_token_config()
        glance_url = utils.get_glance_url()

        if DEBUG:
            print username, password, tenant_name, keystone_url, glance_url

        user = keystone.Keystone(username, password,
                                 tenant_name, keystone_url)
        token = user.get_token()

        glance = glanceclient.Client(endpoint=glance_url, token=token)

        image = glance.images.create(name='__nvs_monitor__',
                                     data='a' * 1024,
                                     disk_format='qcow2',
                                     container_format='ovf',
                                     is_public=False)

        if image.status != 'active':
            print 'create image error. %s' % image

        image.delete()

        try:
            image.get()
        except glanceexc.HTTPNotFound:
            pass

    except Exception:
        if DEBUG:
            utils.print_traceback()
        result = 'failed'
    else:
        result = 'success'

    utils.print_result(result)

if __name__ == '__main__':
    main()
