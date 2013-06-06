from keystoneclient.v2_0 import client as keyclient


class Keystone(object):
    def __init__(self, username, password, tenant_name, keystone_url):
        self.username = username
        self.password = password
        self.tenant_name = tenant_name
        self.keystone_url = keystone_url
        self.keystone = keyclient.Client(username=self.username,
                                         password=self.password,
                                         tenant_name=self.tenant_name,
                                         auth_url=self.keystone_url)

    def get_token(self):
        return self.keystone.auth_token

    def get_tenant_id(self):
        return self.keystone.tenant_id
