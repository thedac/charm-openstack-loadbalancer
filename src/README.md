# Overview

This charm provides load balancing service to OpenStack APIs.

# Usage

    juju deploy keystone
    juju deploy mysql
    juju add-relation keystone mysql

    juju deploy openstack-loadbalancer
    juju add-relation keystone openstack-loadbalancer:public-backend
    juju add-relation keystone openstack-loadbalancer:internal-backend
    juju add-relation keystone openstack-loadbalancer:admin-backend

# Bugs

Please report bugs on [Launchpad](https://bugs.launchpad.net/charm-openstack-loadbalancer/+filebug).

For general questions please refer to the OpenStack [Charm Guide](http://docs.openstack.org/developer/charm-guide/).
