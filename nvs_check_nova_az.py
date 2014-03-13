"""
The script used to see whether there is some unavailable zone in openstack.
"""
import argparse

from novaclient.v1_1 import client as novaclient


parser = argparse.ArgumentParser()
parser.add_argument("-H", "--host",
                    help="keystone url. e.g. http://localhost:5000/v2.0",
                    default='http://localhost:5000/v2.0')
parser.add_argument("-U", "--username",
                    help="Username of keystone")
parser.add_argument("-P", "--password",
                    help="Password of keystone")
parser.add_argument("-T", "--tenant-name",
                    help="Tenant name of keystone")
args = parser.parse_args()

nova = novaclient.Client(args.username, args.password, args.tenant_name,
                         args.host, no_cache=True)

error_azs = []
for az in nova.availability_zones.list(detailed=False):
    if not az.zoneState['available']:
        error_azs.append(az)

print("unavailable %s > 1 There are unavailable AZ: %s." %
      (len(error_azs), error_azs))
