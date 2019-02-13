from __future__ import print_function
import re
import requests
from orionsdk import SwisClient


def main():
    npm_server = solarwindws
    username = sw_username
    password = sw_password

    swis = SwisClient(npm_server, username, password)
    print("Add an SNMP v3 node:")

    # fill these in for the node you want to add!
    ip_address = node_ip
    snmp_username = snmp_username
    snmp_auth = snmp_auth
    snmp_priv = snmp_priv

    # set up property bag for the new node
    props = {
        'IPAddress': ip_address,
        'EngineID': 1,
        'ObjectSubType': 'SNMP',
        'SNMPVersion': '3',
        'SNMPV3Username': snmp_username,
        'SNMPV3AuthKey': snmp_auth,
        'SNMPV3PrivKeyIsPwd': True,
        "SNMPv3AuthKeyIsPwd": True,
        "SNMPv3PrivKey": snmp_priv,
        "SNMPv3AuthMethod":"SHA1",
        "SNMPv3PrivMethod":"AES128",
        'DNS': 'SYRUS-FW1',
        'NodeName': 'SYRUS-FW1',
        'UnManaged': False,
    }

    pollers_enabled = {
        'N.Status.ICMP.Native': False,
        'N.Status.SNMP.Native': True,
        'N.ResponseTime.ICMP.Native': False,
        'N.ResponseTime.SNMP.Native': True,
        'N.Details.SNMP.Generic': True,
        'N.Uptime.SNMP.Generic': True,
        'N.Cpu.SNMP.HrProcessorLoad': True,
        'N.Memory.SNMP.NetSnmpReal': True,
        'N.AssetInventory.Snmp.Generic': True,
        'N.Status.SNMP.Native': False,
        'N.ResponseTime.SNMP.Native': False,
        'N.Topology_Layer3.SNMP.ipNetToMedia': False,
        'N.Routing.SNMP.Ipv4CidrRoutingTable': False
    }

    results = swis.create('Orion.Nodes', **props)

    # extract the nodeID from the result
    nodeid = re.search(r'(\d+)$', results).group(0)

    pollers = []

    for k in pollers_enabled:
        pollers.append(
        {
        'PollerType': k,
        'NetObject': 'N:' + nodeid,
        'NetObjectType': 'N',
        'NetObjectID': nodeid,
        'Enabled': pollers_enabled[k]
        }
        )




    invoke_id = '{0}{1}'.format("N:", nodeid)

    swis.invoke('Orion.Nodes', 'PollNow', invoke_id)

    swis.invoke('Orion.HardwareHealth.HardwareInfo', 'EnableHardwareHealth', invoke_id, 9)  


if __name__ == '__main__':
    main()
