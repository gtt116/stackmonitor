from keystoneclient.v2_0 import client as keyclient


def get_token(username, password, tenant_name, keystone_url):
    keystone = keyclient.Client(username=username, password=password,
                                tenant_name=tenant_name, auth_url=keystone_url)
    return keystone.auth_token
