#!/usr/bin/python

from nailgun.db import db
from nailgun.db.sqlalchemy import models
import json

releases = db().query(models.Release)
for r in releases:
       r.wizard_metadata = json.loads('{"Compute": {"hypervisor": {"bind": "settings:common.libvirt_type.value", "values": [{"bind": [{"wizard:Storage.ceph": "disable"}, {"wizard:Network.manager": "neutron-vlan"}], "data": "kvm", "description": "dialog.create_cluster_wizard.compute.kvm_description", "label": "dialog.create_cluster_wizard.compute.kvm"}, {"bind": [{"wizard:Storage.ceph": "disable"}, {"wizard:Network.manager": "neutron-vlan"}], "data": "qemu", "description": "dialog.create_cluster_wizard.compute.qemu_description", "label": "dialog.create_cluster_wizard.compute.qemu"}], "weight": 5, "value": "qemu", "type": "radio"}, "vcenter": {"bind": [{"wizard:Storage.ceph": "disable"}, {"wizard:Network.manager": "nova-network"}, "settings:common.use_vcenter.value"], "type": "checkbox", "description": "dialog.create_cluster_wizard.compute.vcenter_description", "weight": 10, "label": "dialog.create_cluster_wizard.compute.vcenter"}}, "Network": {"manager": {"values": [{"bind": [{"cluster:net_provider": "neutron"}, {"cluster:net_segment_type": "vlan"}], "data": "neutron-vlan", "description": "dialog.create_cluster_wizard.network.neutron_vlan_description", "label": "common.network.neutron_vlan"}, {"bind": [{"cluster:net_provider": "neutron"}, {"cluster:net_segment_type": "tun"}], "data": "neutron-tun", "description": "dialog.create_cluster_wizard.network.neutron_tun_description", "label": "common.network.neutron_tun"}, {"restrictions": [{"Compute.vcenter == false": "dialog.create_cluster_wizard.network.nove_network_vcenter_alert"}], "bind": [{"cluster:net_provider": "nova_network"}], "data": "nova-network", "description": "dialog.create_cluster_wizard.network.nova_network_description", "label": "dialog.create_cluster_wizard.network.nova_network"}], "type": "radio"}}, "Storage": {"ceph": {"values": [{"bind": [{"settings:storage.volumes_lvm.value": true}, {"settings:storage.volumes_ceph.value": false}, {"settings:storage.objects_ceph.value": false}, {"settings:storage.ephemeral_ceph.value": false}, {"settings:storage.images_ceph.value": false}], "data": "disable", "label": "dialog.create_cluster_wizard.storage.ceph_disable"}, {"bind": [{"settings:storage.volumes_ceph.value": true}, {"settings:storage.objects_ceph.value": true}, {"settings:storage.ephemeral_ceph.value": true}, {"settings:storage.images_ceph.value": true}, {"settings:storage.volumes_lvm.value": false}], "data": "enable", "label": "dialog.create_cluster_wizard.storage.ceph_enable"}], "type": "radio"}}, "AdditionalServices": {"murano": {"bind": "settings:additional_components.murano.value", "type": "checkbox", "description": "dialog.create_cluster_wizard.additional.install_murano_description", "weight": 20, "label": "dialog.create_cluster_wizard.additional.install_murano"}, "ceilometer": {"bind": "settings:additional_components.ceilometer.value", "type": "checkbox", "description": "dialog.create_cluster_wizard.additional.install_ceilometer_description", "weight": 30, "label": "dialog.create_cluster_wizard.additional.install_ceilometer"}, "sahara": {"bind": "settings:additional_components.sahara.value", "type": "checkbox", "description": "dialog.create_cluster_wizard.additional.install_sahara_description", "weight": 10, "label": "dialog.create_cluster_wizard.additional.install_sahara"}}, "Mode": {"mode": {"bind": "cluster:mode", "values": [{"data": "ha_compact", "label": "cluster.mode.ha_compact"}], "type": "radio"}, "metadata": {"restrictions": [{"action": "hide", "condition": "true"}]}}, "Ready": {}}')

db().commit()
