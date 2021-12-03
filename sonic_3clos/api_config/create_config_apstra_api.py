"""
---------------------------------
 Author: Gilberto Rampini
 Date: 12/2021
---------------------------------
"""
import requests
import json
import ct_config_base as ct
from time import sleep

requests.packages.urllib3.disable_warnings()


from apstra_gets import *
from apstra_resources import *
from apstra_devices import *
from apstra_design import *
from blueprint_staged import *
from logical_data import create_logical_devices_dic
from int_map_data import create_interface_map_dic
from rack_data import create_rack_type_dic
from templates_data import create_templates_dic
from device_profiles_data import create_device_profiles_dic

"""
Resources Dictionaries
"""
asn_dic = {'DC1-ASN-POOL': {'asn_name': 'DC1-ASN-POOL', 'asn_start': '100', 'asn_stop': '199'},}

vni_dic = {'LAB-VNI-POOL': {'vni_name': 'LAB-VNI-POOL', 'vni_start': '5000', 'vni_stop': '7000'}, }

ip_pool_dic = {'DC1-EXTERNAL-ROUTER': {'ip_name': 'DC1-EXTERNAL-ROUTER', 'network': '10.1.1.0/24'},
               'DC1-LEAF-LOOPBACK': {'ip_name': 'DC1-LEAF-LOOPBACK', 'network': '10.20.30.0/24'},
               'DC1-SPINE-LEAF': {'ip_name': 'DC1-SPINE-LEAF', 'network': '10.10.0.0/22'},
               'DC1-SPINE-LOOPBACK': {'ip_name': 'DC1-SPINE-LOOPBACK', 'network': '10.20.31.0/24'},
               'DC1-VIRTUAL-LEAF-LOOPBACK': {'ip_name': 'DC1-VIRTUAL-LEAF-LOOPBACK', 'network': '10.100.100.0/24'},
               'DC1-SVI-SUBNET-MLAG': {'ip_name': 'DC1-SVI-SUBNET-MLAG', 'network': '10.101.101.0/24'}, }

"""
Create Blueprint Dictionaries
"""

blueprint_dic = {'DC1': {'bl_name': 'DC1', 'template_name': 'SONIC-3-STAGE-TEMPLATE'}, }


"""
DC1 Blueprint Routing Zones Dictionaries
"""

dc1_routing_zones_dic = {'customer-1': {'bl_name': 'DC1', 'rz_name': 'customer-1', 'vni_id': 10010},
                         'customer-2': {'bl_name': 'DC1', 'rz_name': 'customer-2', 'vni_id': 10020}, }

dc1_svi_subnets_mlag_dic = {'customer-1': {'bl_name': 'DC1', 'lb_ip': 'DC1-SVI-SUBNET-MLAG'},}


dc1_vtep_ips_dic = {'customer-1': {'bl_name': 'DC1', 'lb_ip': 'DC1-LEAF-LOOPBACK'},}


dc1_routing_zones_loopback_dic = {'customer-1': {'bl_name': 'DC1', 'rz_name': 'customer-1',
                                                 'lb_ip': 'DC1-VIRTUAL-LEAF-LOOPBACK'},
                                  'customer-2': {'bl_name': 'DC1', 'rz_name': 'customer-2',
                                                 'lb_ip': 'DC1-VIRTUAL-LEAF-LOOPBACK'}, }


dc1_virtual_network_dic = {'VLAN10': {'bl_name': 'DC1', 'vn_name': 'VLAN10', 'rz_name': 'customer-1',
                                      'network': '192.168.10.0/24', 'gw': '192.168.10.1', 'vlan_id': 10, 'vni_id': 5010},
                           'VLAN20': {'bl_name': 'DC1', 'vn_name': 'VLAN20', 'rz_name': 'customer-1',
                                      'network': '192.168.20.0/24', 'gw': '192.168.20.1', 'vlan_id': 20, 'vni_id': 5020},
                           'VLAN100': {'bl_name': 'DC1', 'vn_name': 'VLAN100', 'rz_name': 'customer-2',
                                       'network': '192.168.100.0/24', 'gw': '192.168.100.1', 'vlan_id': 100, 'vni_id': 5100},
                           'VLAN200': {'bl_name': 'DC1', 'vn_name': 'VLAN200', 'rz_name': 'customer-2',
                                       'network': '192.168.200.0/24', 'gw': '192.168.200.1', 'vlan_id': 200, 'vni_id': 5200}, }

dc1_ct_virtual_network_dic = {'CT-VLAN10': {'bl_name': 'DC1', 'policy_id': 'vlan10-ct-policy-id',
                                            'ct_name': 'CT-VLAN10', 'vn_name': 'VLAN10'},
                              'CT-VLAN20': {'bl_name': 'DC1', 'policy_id': 'vlan20-ct-policy-id',
                                            'ct_name': 'CT-VLAN20', 'vn_name': 'VLAN20'},
                              'CT-VLAN100': {'bl_name': 'DC1', 'policy_id': 'vlan100-ct-policy-id',
                                             'ct_name': 'CT-VLAN100', 'vn_name': 'VLAN100'},
                              'CT-VLAN200': {'bl_name': 'DC1', 'policy_id': 'vlan200-ct-policy-id',
                                             'ct_name': 'CT-VLAN200', 'vn_name': 'VLAN200'}, }

dc1_ct_int_assign_dic = {'PortChannel1': {'bl_name': 'DC1', 'ct_name': 'CT-VLAN10',
                                 'leaf_name': 'sonic_mclag_leaf_001', 'int_name': 'PortChannel1'},
                         'Ethernet5': {'bl_name': 'DC1', 'ct_name': 'CT-VLAN10',
                                      'leaf_name': 'sonic_single_leaf_001', 'int_name': 'Ethernet5'},
                         'Ethernet6_CT-VLAN20': {'bl_name': 'DC1', 'ct_name': 'CT-VLAN20',
                                                'leaf_name': 'sonic_single_leaf_001', 'int_name': 'Ethernet6'},
                         'Ethernet6_CT-VLAN100': {'bl_name': 'DC1', 'ct_name': 'CT-VLAN100',
                                                 'leaf_name': 'sonic_mclag_leaf_001', 'int_name': 'Ethernet6'},
                         'Ethernet7': {'bl_name': 'DC1', 'ct_name': 'CT-VLAN200',
                                    'leaf_name': 'sonic_single_leaf_001', 'int_name': 'Ethernet7'}, }


def api_create_asn_pool():

    for i in asn_dic.keys():

        asn_name = asn_dic[i].get('asn_name')
        asn_start = asn_dic[i].get('asn_start')
        asn_stop = asn_dic[i].get('asn_stop')

        create_asn_pool(asn_name, asn_start, asn_stop)


def api_create_vni_pool():

    for i in vni_dic.keys():

        vni_name = vni_dic[i].get('vni_name')
        vni_start = vni_dic[i].get('vni_start')
        vni_stop = vni_dic[i].get('vni_stop')

        create_vni_pool(vni_name, vni_start, vni_stop)


def api_create_ip_pool():

    for i in ip_pool_dic.keys():

        ip_name = ip_pool_dic[i].get('ip_name')
        network = ip_pool_dic[i].get('network')

        create_ip_pool(ip_name, network)


def api_create_device_profiles():

    interface_map_list = create_device_profiles_dic()

    for i in interface_map_list.keys():

        device_profiles_name = interface_map_list[i].get('name')
        device_profiles_data = interface_map_list[i].get('data')

        create_device_profiles(device_profiles_name, device_profiles_data)


def api_create_logical_devices():

    logical_device_list = create_logical_devices_dic()

    for i in logical_device_list.keys():

        logical_name = logical_device_list[i].get('name')
        logical_data = logical_device_list[i].get('data')

        create_logical_device(logical_name,  logical_data)


def api_create_interface_map():

    interface_map_list = create_interface_map_dic()

    for i in interface_map_list.keys():

        interface_map_name = interface_map_list[i].get('name')
        interface_map_data = interface_map_list[i].get('data')

        create_interface_map(interface_map_name, interface_map_data)


def api_create_rack_type():

    rack_list = create_rack_type_dic()

    for i in rack_list.keys():

        rack_type_name = rack_list[i].get('name')
        rack_type_data = rack_list[i].get('data')

        create_rack_type(rack_type_name, rack_type_data)


def api_create_templates():

    template_list = create_templates_dic()

    for i in template_list.keys():

        template_name = template_list[i].get('name')
        template_data = template_list[i].get('data')

        create_template(template_name, template_data)


def api_create_blueprint():

    for i in blueprint_dic.keys():

        bl_name = blueprint_dic[i].get('bl_name')
        template_name = blueprint_dic[i].get('template_name')

        create_blueprint(bl_name, template_name)


def api_create_routing_zones(dic_data):

    dic_data = dic_data

    for i in dic_data.keys():

        bl_name = dic_data[i].get('bl_name')
        rz_name = dic_data[i].get('rz_name')
        vni_id = dic_data[i].get('vni_id')

        set_blueprint_sz(bl_name, rz_name, vni_id)


def api_set_svi_subnet_mlag(dic_data):

    dic_data = dic_data

    for i in dic_data.keys():

        bl_name = dic_data[i].get('bl_name')
        lb_ip = dic_data[i].get('lb_ip')

        set_blueprint_svi_subnet_mclag(bl_name, lb_ip)


def api_set_vtep_ip(dic_data):

    dic_data = dic_data

    for i in dic_data.keys():

        bl_name = dic_data[i].get('bl_name')
        lb_ip = dic_data[i].get('lb_ip')

        set_blueprint_vtep_ip(bl_name, lb_ip)


def api_set_rz_loopback(dic_data):

    dic_data = dic_data

    for i in dic_data.keys():

        bl_name = dic_data[i].get('bl_name')
        rz_name = dic_data[i].get('rz_name')
        lb_ip = dic_data[i].get('lb_ip')

        set_blueprint_sz_loopback(bl_name, rz_name, lb_ip)


def api_create_virtual_network(dic_data):

    dic_data = dic_data

    for i in dic_data.keys():

        bl_name = dic_data[i].get('bl_name')
        vn_name = dic_data[i].get('vn_name')
        rz_name = dic_data[i].get('rz_name')
        network = dic_data[i].get('network')
        gw = dic_data[i].get('gw')
        vlan_id = dic_data[i].get('vlan_id')
        vni_id = dic_data[i].get('vni_id')

        set_blueprint_vn(bl_name, vn_name, rz_name, network, gw, vlan_id, vni_id)


def api_create_vn_ct(dic_data):

    dic_data = dic_data

    for i in dic_data.keys():

        bl_name = dic_data[i].get('bl_name')
        policy_id = dic_data[i].get('policy_id')
        ct_name = dic_data[i].get('ct_name')
        vn_name = dic_data[i].get('vn_name')

        ct.set_virtual_network_ct(bl_name, policy_id, ct_name, vn_name)


def api_ct_int_assign(dic_data):

    dic_data = dic_data

    for i in dic_data.keys():

        bl_name = dic_data[i].get('bl_name')
        ct_name = dic_data[i].get('ct_name')
        leaf_name = dic_data[i].get('leaf_name')
        int_name = dic_data[i].get('int_name')

        ct.set_blueprint_server_link(bl_name, ct_name, leaf_name, int_name)


if __name__ == '__main__':

    print("################################################### Creating Common resources")


    # --------------------- Resources
    api_create_asn_pool()
    api_create_vni_pool()
    api_create_ip_pool()
    sleep(1)
    api_create_device_profiles()

    print("################################################### Onbox and Manage Devices")
    # --------------------- Onbox and Manage Devices
    sleep(2)
    create_onbox_device('192.168.122.215', '192.168.122.221')
    check_agent_state()
    manage_device_all()
    sleep(5)

    print("################################################### Design")
    # --------------------- Logical devices, interface map, rack type and templates
    api_create_logical_devices()
    sleep(1)
    api_create_interface_map()
    sleep(1)
    api_create_rack_type()
    sleep(1)
    api_create_templates()

    print("################################################### Create Blueprint")
    # --------------------- Blueprint
    api_create_blueprint()
    sleep(10)
    
    
    # --------------------- DC1 Blueprint
    print("################################################### Blueprint Configuration")
    
    # --------------------- Allocate IP pools to blueprint
    print("- Blueprint Resource")
    blueprint_resource_asn_spine("DC1", "DC1-ASN-POOL")
    sleep(1)
    blueprint_resource_asn_leaf("DC1", "DC1-ASN-POOL")
    sleep(1)
    blueprint_resource_loopback_spine("DC1", "DC1-SPINE-LOOPBACK")
    sleep(1)
    blueprint_resource_loopback_leaf("DC1", "DC1-LEAF-LOOPBACK")
    sleep(1)
    blueprint_resource_fabric_spine_leaf("DC1", "DC1-SPINE-LEAF")
    sleep(1)

    print("- Blueprint Device Profiles")
    # --------------------- assign device profiles to blueprint
    blueprint_device_profile_3_stage("DC1", "SONIC-10x10-Spine", "SONIC-12x10-Leaf", "SONIC-10x10-BorderLeaf")
    sleep(2)
    print("- Blueprint Physical Devices")
    # --------------------- assign physical device to blueprint
    send_physical_device_parameters_dc1("DC1")
    sleep(2)
    print("- Blueprint SVI Subnets MLAG")
    # --------------------- Configure SVI subnets ( necessary for mclag connectivity
    api_set_svi_subnet_mlag(dc1_svi_subnets_mlag_dic)

    print("- Blueprint Routing Zones")
    # --------------------- create routing zones
    api_create_routing_zones(dc1_routing_zones_dic)
    sleep(5)
    
    # --------------------- set routing zones loopback
    api_set_rz_loopback(dc1_routing_zones_loopback_dic)
    sleep(5)
    print("- Blueprint Virtual Networks")
    # --------------------- create virtual networks and set vtep IP
    api_create_virtual_network(dc1_virtual_network_dic)
    sleep(5)
    api_set_vtep_ip(dc1_vtep_ips_dic)
    print("- Blueprint Commit")
    # --------------------- commit basic configuration
    sleep(5)
    set_deploy_blueprint("DC1", "DC1 Basic Configuration")
    sleep(5)

    print("- Blueprint Connectivity Templates")
    # --------------------- create external router connectivity template, assign interface and allocate IP Pool
    ct.set_external_router_ct("DC1", "dc1-r1-ct-policy-id", "CT-DC1-R1", "10.1.1.1", 65002)
    sleep(5)
    
    # --------------------- Here is the first name after pod ie:sonic_border_leaf_001
    ct.set_blueprint_server_link("DC1", "CT-DC1-R1", "sonic_border_leaf_001", "Ethernet5")
    sleep(5)
    
    # --------------------- set generic IP for dc1-external-router
    blueprint_resource_generic_link_ip("DC1", "DC1-EXTERNAL-ROUTER")
    sleep(5)
    
    # --------------------- create virtual network - CT
    api_create_vn_ct(dc1_ct_virtual_network_dic)
    sleep(2)
    
    # --------------------- set interfaces 
    api_ct_int_assign(dc1_ct_int_assign_dic)
    
    sleep(5)
    print("- Blueprint Commit")
    # --------------------- commit configuration
    set_deploy_blueprint("DC1", "DC1 Connectivity Templates")
    sleep(5)


