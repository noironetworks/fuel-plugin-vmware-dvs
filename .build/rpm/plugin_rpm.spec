#
# The spec is generated automatically by Fuel Plugin Builder tool
# https://github.com/stackforge/fuel-plugins
#
# RPM spec file for package fuel-plugin-vmware-dvs-2.1
#
# Copyright (c) 2016, Apache License Version 2.0, Mirantis
#

Name:           fuel-plugin-vmware-dvs-2.1
Version:        2.1.0
Url:            https://github.com/wsronek/fuel-plugin-vmware-dvs
Summary:        Neutron VMware DVS ML2 plugin
License:        Apache License Version 2.0
Source0:        fuel-plugin-vmware-dvs-2.1.fp
Vendor:         Mirantis
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Group:          Development/Libraries
Release:        1
BuildArch:      noarch

%description
Enable to use plugin vmware_dvs for Neutron

%prep
rm -rf %{name}-%{version}
mkdir %{name}-%{version}

tar -vxf %{SOURCE0} -C %{name}-%{version}

%install
cd %{name}-%{version}
mkdir -p %{buildroot}/var/www/nailgun/plugins/
cp -r fuel-plugin-vmware-dvs-2.1 %{buildroot}/var/www/nailgun/plugins/

%clean
rm -rf %{buildroot}

%pre


%post
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

/usr/bin/dockerctl shell nailgun sed -i -e "/if common_attrs.get('use_vcenter', {}).get('value') is True and/,+5 d" /usr/lib/python2.7/site-packages/nailgun/api/v1/validators/cluster.py
/usr/bin/dockerctl shell nailgun systemctl restart nailgun.service


%preun


%files
/var/www/nailgun/plugins/fuel-plugin-vmware-dvs-2.1
