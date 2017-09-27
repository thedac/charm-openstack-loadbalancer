# Copyright 2016 Canonical Ltd
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#  http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import charms.reactive as reactive

# This charm's library contains all of the handler code associated with
# openstack-loadbalancer
import charm.openstack.openstack_loadbalancer as openstack_loadbalancer


# Minimal inferfaces required for operation
MINIMAL_INTERFACES = ['admin-backend']


# use a synthetic state to ensure that it get it to be installed independent of
# the install hook.
@reactive.when_not('charm.installed')
def install_packages():
    openstack_loadbalancer.install()
    reactive.set_state('charm.installed')


@reactive.when('admin-backend.connected')
def set_endpoint_ips(openstack_api_endpoints):
    openstack_api_endpoints.set_endpoint_ip(openstack_api_endpoints)


def render(*args):
    openstack_loadbalancer.render_configs(args)
    openstack_loadbalancer.assess_status()


@reactive.when('charm.installed')
@reactive.when(*MINIMAL_INTERFACES)
def render_unclustered(*args):
    render(*args)


@reactive.when('charm.installed')
@reactive.when('cluster.available',
               *MINIMAL_INTERFACES)
def render_clustered(*args):
    render(*args)


@reactive.when('ha.connected')
@reactive.when_not('ha.available')
def cluster_connected(hacluster):
    openstack_loadbalancer.configure_ha_resources(hacluster)


@reactive.hook('upgrade-charm')
def upgrade_charm():
    openstack_loadbalancer.install()
