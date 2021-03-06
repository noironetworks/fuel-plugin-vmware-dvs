Installing the VMware DVS plugin
--------------------------------

Make sure that:

* you have the installed the
  `Fuel Master node <https://docs.mirantis.com/openstack/fuel/fuel-7.0/user-guide.html>`__

* all the nodes of your future environment are discovered and functional.

* there is a connectivity to correctly configured vCenter with VDS'es and clusters created.
  Please, see the
  `Mirantis OpenStack Planning Guide <https://docs.mirantis.com/openstack/fuel/fuel-7.0/mos-planning-guide.html#plan-the-vsphere-integration>`_,
  `User Guide <https://docs.mirantis.com/openstack/fuel/fuel-7.0/user-guide.html#vmware-integration-notes>`_
  and
  `this plugin's specification <https://github.com/wsronek/fuel-plugin-vmware-dvs/blob/master/specs/fuel-plugin-vmware-dvs.rst>`_
  for information on configuring vCenter.

#. Copy the plugin into Fuel Master node:
   ::

      $ scp fuel-plugin-vmware-dvs-2.0-2.0.0-1.noarch.rpm <Fuel Master node ip>:/tmp

#. Log into the Fuel Master node and install the plugin:
   ::

      $ ssh root@<Fuel Master node ip>
      [root@nailgun ~]# fuel plugins --install /
      /tmp/fuel-plugin-vmware-dvs-2.0-2.0.0-1.noarch.rpm
      [root@nailgun  ]# fuel plugins
      DEPRECATION WARNING: /etc/fuel/client/config.yaml exists and will
      be used as the source for settings. This behavior is deprecated.
      Please specify the path to your custom settings file in the
      FUELCLIENT_CUSTOM_SETTINGS environment variable.

      +------+--------------------------+-----------+--------------------+
      | id   | name                     | version   | package\_version   |
      +------+--------------------------+-----------+--------------------+
      | 2    | fuel-plugin-vmware-dvs   | 2.0.0     | 3.0.0              |
      +------+--------------------------+-----------+--------------------+

.. raw:: latex

   \pagebreak
