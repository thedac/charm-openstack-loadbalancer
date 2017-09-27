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

import os

import charms_openstack.charm
import charms_openstack.adapters

OPENSTACK_LOADBALANCER_DIR = '/etc/haproxy'
OPENSTACK_LOADBALANCER_CONF = os.path.join(OPENSTACK_LOADBALANCER_DIR,
                                           'haproxy.conf')


class OpenstackLoadbalancerCharm(charms_openstack.charm.HAOpenStackCharm):

    ha_resources = ['vips', 'haproxy']
    packages = ['haproxy']
    release = 'icehouse'
    required_relations = ['admin-backend']

    @property
    def all_packages(self):
        return self.packages

    def configure_source(self):
        pass

    def enable_memcache(self):
        return False


def install():
    """Use the singleton from the OpenstackLoadbalancerCharm to install the
    packages on the unit
    """
    OpenstackLoadbalancerCharm.singleton.install()


def restart_all():
    """Use the singleton from the OpenstackLoadbalancerCharm to restart
    services on the unit.
    """
    OpenstackLoadbalancerCharm.singleton.restart_all()


def set_endpoint_ip(openstack_api_endpoints):
    """
    Pick correct ip
    Set it on the relation to the unit
    """
    pass


def render_configs(interfaces_list):
    """Using a list of interfaces, render the configs and, if they have
    changes, restart the services on the unit.
    """
    OpenstackLoadbalancerCharm.singleton.render_with_interfaces(
            interfaces_list)


def assess_status():
    """Just call the OpenstackLoadbalancerCharm.singleton.assess_status()
    command to update status on the unit.
    """
    OpenstackLoadbalancerCharm.singleton.assess_status()


def configure_ha_resources(hacluster):
    """Use the singleton from the OpenstackLoadbalancerCharm to run
    configure_ha_resources
    """
    OpenstackLoadbalancerCharm.singleton.configure_ha_resources(hacluster)


def configure_ssl():
    """Use the singleton from the OpenstackLoadbalancerCharm to run configure_ssl
    """
    OpenstackLoadbalancerCharm.singleton.configure_ssl()


def reload_and_restart():
    """Reload systemd and restart aodh API when override file changes
    """
    OpenstackLoadbalancerCharm.singleton.reload_and_restart()
