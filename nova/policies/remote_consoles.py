# Copyright 2016 Cloudbase Solutions Srl
# All Rights Reserved.
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

from nova.policies import base


BASE_POLICY_NAME = 'os_compute_api:os-remote-consoles'


remote_consoles_policies = [
    base.create_rule_default(
        BASE_POLICY_NAME,
        base.RULE_ADMIN_OR_OWNER,
        "Generates a URL to access remove server console",
        [
            {
                'method': 'POST',
                'path': '/servers/{server_id}/action (os-getRDPConsole)'
            },
            {
                'method': 'POST',
                'path': '/servers/{server_id}/action (os-getSerialConsole)'
            },
            {
                'method': 'POST',
                'path': '/servers/{server_id}/action (os-getSPICEConsole)'
            },
            {
                'method': 'POST',
                'path': '/servers/{server_id}/action (os-getVNCConsole)'
            },
            {
                'method': 'POST',
                'path': '/servers/{server_id}/remote-consoles'
            },
        ]),
]


def list_rules():
    return remote_consoles_policies
