#!/bin/sh
#    Copyright 2015 Mirantis, Inc.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

#/usr/bin/dockerctl shell nailgun sed -i -e "/if common_attrs.get('use_vcenter', {}).get('value') is True and/,+5 d" /usr/lib/python2.7/site-packages/nailgun/api/v1/validators/cluster.py
#/usr/bin/dockerctl shell nailgun systemctl restart nailgun.service
cd /var/www/nailgun/plugins/fuel-plugin-vmware-dvs-2.1
dockerctl copy sqlpatch.py nailgun:/root/.
dockerctl shell nailgun /root/sqlpatch.py
dockerctl  copy cluster.patch nailgun:/root/.
/usr/bin/dockerctl shell nailgun yum -y install patch
dockerctl shell nailgun bash -c "/usr/bin/patch -p4 -N  /usr/lib/python2.6/site-packages/nailgun/api/v1/validators/cluster.py /root/cluster.patch" || true
dockerctl  copy start.patch nailgun:/root/.
dockerctl shell nailgun bash -c "/usr/bin/patch -p4 -N /usr/local/bin/start.sh /root/start.patch" || true
