"""
---------------------------------
 Author: Gilberto Rampini
 Date: 12/2021
---------------------------------
"""
""" -------------- Interface Maps """


def create_interface_map_dic():

    interface_map_data_dic = {'SONIC-10x10-BorderLeaf': {'name': 'SONIC-10x10-BorderLeaf',
                                                       'data': f'''{{
                            "device_profile_id": "VS_SONIC_300_Generic",
                            "interfaces": [
                                {{
                                    "mapping": [
                                        1,
                                        1,
                                        1,
                                        1,
                                        1
                                    ],
                                    "name": "Ethernet1",
                                    "position": 1,
                                    "roles": [
                                        "spine"
                                    ],
                                    "setting": {{
                                        "param": "{{\\"interface\\": {{\\"index\\": \\"2\\", \\"lane_map\\": \\"50\\", \\"master\\": null, \\"brkout_mode\\": \\"\\", \\"speed\\": \\"10000\\", \\"port\\": \\"\\"}}}}"
                                    }},
                                    "speed": {{
                                        "unit": "G",
                                        "value": 10
                                    }},
                                    "state": "active"
                                }},
                                {{
                                    "mapping": [
                                        2,
                                        1,
                                        1,
                                        1,
                                        2
                                    ],
                                    "name": "Ethernet2",
                                    "position": 2,
                                    "roles": [
                                        "spine"
                                    ],
                                    "setting": {{
                                        "param": "{{\\"interface\\": {{\\"index\\": \\"3\\", \\"lane_map\\": \\"51\\", \\"master\\": null, \\"brkout_mode\\": \\"\\", \\"speed\\": \\"10000\\", \\"port\\": \\"\\"}}}}"
                                    }},
                                    "speed": {{
                                        "unit": "G",
                                        "value": 10
                                    }},
                                    "state": "active"
                                }},
                                {{
                                    "mapping": [
                                        3,
                                        1,
                                        1,
                                        1,
                                        3
                                    ],
                                    "name": "Ethernet3",
                                    "position": 3,
                                    "roles": [
                                        "spine"
                                    ],
                                    "setting": {{
                                        "param": "{{\\"interface\\": {{\\"index\\": \\"4\\", \\"lane_map\\": \\"52\\", \\"master\\": null, \\"brkout_mode\\": \\"\\", \\"speed\\": \\"10000\\", \\"port\\": \\"\\"}}}}"
                                    }},
                                    "speed": {{
                                        "unit": "G",
                                        "value": 10
                                    }},
                                    "state": "active"
                                }},
                                {{
                                    "mapping": [
                                        4,
                                        1,
                                        1,
                                        1,
                                        4
                                    ],
                                    "name": "Ethernet4",
                                    "position": 4,
                                    "roles": [
                                        "spine"
                                    ],
                                    "setting": {{
                                        "param": "{{\\"interface\\": {{\\"index\\": \\"5\\", \\"lane_map\\": \\"57\\", \\"master\\": null, \\"brkout_mode\\": \\"\\", \\"speed\\": \\"10000\\", \\"port\\": \\"\\"}}}}"
                                    }},
                                    "speed": {{
                                        "unit": "G",
                                        "value": 10
                                    }},
                                    "state": "active"
                                }},
                                {{
                                    "mapping": [
                                        5,
                                        1,
                                        1,
                                        1,
                                        5
                                    ],
                                    "name": "Ethernet5",
                                    "position": 5,
                                    "roles": [
                                        "generic"
                                    ],
                                    "setting": {{
                                        "param": "{{\\"interface\\": {{\\"index\\": \\"6\\", \\"lane_map\\": \\"58\\", \\"master\\": null, \\"brkout_mode\\": \\"\\", \\"speed\\": \\"10000\\", \\"port\\": \\"\\"}}}}"
                                    }},
                                    "speed": {{
                                        "unit": "G",
                                        "value": 10
                                    }},
                                    "state": "active"
                                }},
                                {{
                                    "mapping": [
                                        6,
                                        1,
                                        1,
                                        1,
                                        6
                                    ],
                                    "name": "Ethernet6",
                                    "position": 6,
                                    "roles": [
                                        "generic"
                                    ],
                                    "setting": {{
                                        "param": "{{\\"interface\\": {{\\"index\\": \\"7\\", \\"lane_map\\": \\"59\\", \\"master\\": null, \\"brkout_mode\\": \\"\\", \\"speed\\": \\"10000\\", \\"port\\": \\"\\"}}}}"
                                    }},
                                    "speed": {{
                                        "unit": "G",
                                        "value": 10
                                    }},
                                    "state": "active"
                                }},
                                {{
                                    "mapping": [
                                        7,
                                        1,
                                        1,
                                        1,
                                        7
                                    ],
                                    "name": "Ethernet7",
                                    "position": 7,
                                    "roles": [
                                        "generic"
                                    ],
                                    "setting": {{
                                        "param": "{{\\"interface\\": {{\\"index\\": \\"8\\", \\"lane_map\\": \\"60\\", \\"master\\": null, \\"brkout_mode\\": \\"\\", \\"speed\\": \\"10000\\", \\"port\\": \\"\\"}}}}"
                                    }},
                                    "speed": {{
                                        "unit": "G",
                                        "value": 10
                                    }},
                                    "state": "active"
                                }},
                                {{
                                    "mapping": [
                                        8,
                                        1,
                                        1,
                                        1,
                                        8
                                    ],
                                    "name": "Ethernet8",
                                    "position": 8,
                                    "roles": [
                                        "generic"
                                    ],
                                    "setting": {{
                                        "param": "{{\\"interface\\": {{\\"index\\": \\"9\\", \\"lane_map\\": \\"61\\", \\"master\\": null, \\"brkout_mode\\": \\"\\", \\"speed\\": \\"10000\\", \\"port\\": \\"\\"}}}}"
                                    }},
                                    "speed": {{
                                        "unit": "G",
                                        "value": 10
                                    }},
                                    "state": "active"
                                }},
                                {{
                                    "mapping": [
                                        9,
                                        1,
                                        1,
                                        1,
                                        9
                                    ],
                                    "name": "Ethernet9",
                                    "position": 9,
                                    "roles": [
                                        "generic"
                                    ],
                                    "setting": {{
                                        "param": "{{\\"interface\\": {{\\"index\\": \\"10\\", \\"lane_map\\": \\"62\\", \\"master\\": null, \\"brkout_mode\\": \\"\\", \\"speed\\": \\"10000\\", \\"port\\": \\"\\"}}}}"
                                    }},
                                    "speed": {{
                                        "unit": "G",
                                        "value": 10
                                    }},
                                    "state": "active"
                                }},
                                {{
                                    "mapping": [
                                        10,
                                        1,
                                        1,
                                        1,
                                        10
                                    ],
                                    "name": "Ethernet10",
                                    "position": 10,
                                    "roles": [
                                        "generic"
                                    ],
                                    "setting": {{
                                        "param": "{{\\"interface\\": {{\\"index\\": \\"11\\", \\"lane_map\\": \\"63\\", \\"master\\": null, \\"brkout_mode\\": \\"\\", \\"speed\\": \\"10000\\", \\"port\\": \\"\\"}}}}"
                                    }},
                                    "speed": {{
                                        "unit": "G",
                                        "value": 10
                                    }},
                                    "state": "active"
                                }},
                                {{
                                    "mapping": [
                                        11,
                                        1,
                                        1,
                                        null,
                                        null
                                    ],
                                    "name": "Ethernet11",
                                    "position": 11,
                                    "roles": [
                                        "unused"
                                    ],
                                    "setting": {{
                                        "param": "{{\\"interface\\": {{\\"index\\": \\"12\\", \\"lane_map\\": \\"64\\", \\"master\\": null, \\"brkout_mode\\": \\"\\", \\"speed\\": \\"10000\\", \\"port\\": \\"\\"}}}}"
                                    }},
                                    "speed": {{
                                        "unit": "G",
                                        "value": 10
                                    }},
                                    "state": "active"
                                }},
                                {{
                                    "mapping": [
                                        12,
                                        1,
                                        1,
                                        null,
                                        null
                                    ],
                                    "name": "Ethernet12",
                                    "position": 12,
                                    "roles": [
                                        "unused"
                                    ],
                                    "setting": {{
                                        "param": "{{\\"interface\\": {{\\"index\\": \\"13\\", \\"lane_map\\": \\"77\\", \\"master\\": null, \\"brkout_mode\\": \\"\\", \\"speed\\": \\"10000\\", \\"port\\": \\"\\"}}}}"
                                    }},
                                    "speed": {{
                                        "unit": "G",
                                        "value": 10
                                    }},
                                    "state": "active"
                                }},
                                {{
                                    "mapping": [
                                        13,
                                        1,
                                        1,
                                        null,
                                        null
                                    ],
                                    "name": "Ethernet13",
                                    "position": 13,
                                    "roles": [
                                        "unused"
                                    ],
                                    "setting": {{
                                        "param": "{{\\"interface\\": {{\\"index\\": \\"14\\", \\"lane_map\\": \\"78\\", \\"master\\": null, \\"brkout_mode\\": \\"\\", \\"speed\\": \\"10000\\", \\"port\\": \\"\\"}}}}"
                                    }},
                                    "speed": {{
                                        "unit": "G",
                                        "value": 10
                                    }},
                                    "state": "active"
                                }},
                                {{
                                    "mapping": [
                                        14,
                                        1,
                                        1,
                                        null,
                                        null
                                    ],
                                    "name": "Ethernet14",
                                    "position": 14,
                                    "roles": [
                                        "unused"
                                    ],
                                    "setting": {{
                                        "param": "{{\\"interface\\": {{\\"index\\": \\"15\\", \\"lane_map\\": \\"79\\", \\"master\\": null, \\"brkout_mode\\": \\"\\", \\"speed\\": \\"10000\\", \\"port\\": \\"\\"}}}}"
                                    }},
                                    "speed": {{
                                        "unit": "G",
                                        "value": 10
                                    }},
                                    "state": "active"
                                }}
                            ],
                            "label": "SONIC-10x10-BorderLeaf",
                            "id": "SONIC-10x10-BorderLeaf",
                            "logical_device_id": "SONIC-10x10-BorderLeaf"
                            }}'''},

                            'SONIC-12x10-Leaf': {'name': 'SONIC-12x10-Leaf',
                                                       'data': f'''{{
                            "device_profile_id": "VS_SONIC_300_Generic",
                            "interfaces": [
                                {{
                                    "mapping": [
                                        1,
                                        1,
                                        1,
                                        1,
                                        1
                                    ],
                                    "name": "Ethernet1",
                                    "position": 1,
                                    "roles": [
                                        "spine"
                                    ],
                                    "setting": {{
                                        "param": "{{\\"interface\\": {{\\"index\\": \\"2\\", \\"lane_map\\": \\"50\\", \\"master\\": null, \\"brkout_mode\\": \\"\\", \\"speed\\": \\"10000\\", \\"port\\": \\"\\"}}}}"
                                    }},
                                    "speed": {{
                                        "unit": "G",
                                        "value": 10
                                    }},
                                    "state": "active"
                                }},
                                {{
                                    "mapping": [
                                        2,
                                        1,
                                        1,
                                        1,
                                        2
                                    ],
                                    "name": "Ethernet2",
                                    "position": 2,
                                    "roles": [
                                        "spine"
                                    ],
                                    "setting": {{
                                        "param": "{{\\"interface\\": {{\\"index\\": \\"3\\", \\"lane_map\\": \\"51\\", \\"master\\": null, \\"brkout_mode\\": \\"\\", \\"speed\\": \\"10000\\", \\"port\\": \\"\\"}}}}"
                                    }},
                                    "speed": {{
                                        "unit": "G",
                                        "value": 10
                                    }},
                                    "state": "active"
                                }},
                                {{
                                    "mapping": [
                                        3,
                                        1,
                                        1,
                                        1,
                                        3
                                    ],
                                    "name": "Ethernet3",
                                    "position": 3,
                                    "roles": [
                                        "spine"
                                    ],
                                    "setting": {{
                                        "param": "{{\\"interface\\": {{\\"index\\": \\"4\\", \\"lane_map\\": \\"52\\", \\"master\\": null, \\"brkout_mode\\": \\"\\", \\"speed\\": \\"10000\\", \\"port\\": \\"\\"}}}}"
                                    }},
                                    "speed": {{
                                        "unit": "G",
                                        "value": 10
                                    }},
                                    "state": "active"
                                }},
                                {{
                                    "mapping": [
                                        4,
                                        1,
                                        1,
                                        1,
                                        4
                                    ],
                                    "name": "Ethernet4",
                                    "position": 4,
                                    "roles": [
                                        "spine"
                                    ],
                                    "setting": {{
                                        "param": "{{\\"interface\\": {{\\"index\\": \\"5\\", \\"lane_map\\": \\"57\\", \\"master\\": null, \\"brkout_mode\\": \\"\\", \\"speed\\": \\"10000\\", \\"port\\": \\"\\"}}}}"
                                    }},
                                    "speed": {{
                                        "unit": "G",
                                        "value": 10
                                    }},
                                    "state": "active"
                                }},
                                {{
                                    "mapping": [
                                        5,
                                        1,
                                        1,
                                        1,
                                        5
                                    ],
                                    "name": "Ethernet5",
                                    "position": 5,
                                    "roles": [
                                        "generic"
                                    ],
                                    "setting": {{
                                        "param": "{{\\"interface\\": {{\\"index\\": \\"6\\", \\"lane_map\\": \\"58\\", \\"master\\": null, \\"brkout_mode\\": \\"\\", \\"speed\\": \\"10000\\", \\"port\\": \\"\\"}}}}"
                                    }},
                                    "speed": {{
                                        "unit": "G",
                                        "value": 10
                                    }},
                                    "state": "active"
                                }},
                                {{
                                    "mapping": [
                                        6,
                                        1,
                                        1,
                                        1,
                                        6
                                    ],
                                    "name": "Ethernet6",
                                    "position": 6,
                                    "roles": [
                                        "generic"
                                    ],
                                    "setting": {{
                                        "param": "{{\\"interface\\": {{\\"index\\": \\"7\\", \\"lane_map\\": \\"59\\", \\"master\\": null, \\"brkout_mode\\": \\"\\", \\"speed\\": \\"10000\\", \\"port\\": \\"\\"}}}}"
                                    }},
                                    "speed": {{
                                        "unit": "G",
                                        "value": 10
                                    }},
                                    "state": "active"
                                }},
                                {{
                                    "mapping": [
                                        7,
                                        1,
                                        1,
                                        1,
                                        7
                                    ],
                                    "name": "Ethernet7",
                                    "position": 7,
                                    "roles": [
                                        "generic"
                                    ],
                                    "setting": {{
                                        "param": "{{\\"interface\\": {{\\"index\\": \\"8\\", \\"lane_map\\": \\"60\\", \\"master\\": null, \\"brkout_mode\\": \\"\\", \\"speed\\": \\"10000\\", \\"port\\": \\"\\"}}}}"
                                    }},
                                    "speed": {{
                                        "unit": "G",
                                        "value": 10
                                    }},
                                    "state": "active"
                                }},
                                {{
                                    "mapping": [
                                        8,
                                        1,
                                        1,
                                        1,
                                        8
                                    ],
                                    "name": "Ethernet8",
                                    "position": 8,
                                    "roles": [
                                        "generic"
                                    ],
                                    "setting": {{
                                        "param": "{{\\"interface\\": {{\\"index\\": \\"9\\", \\"lane_map\\": \\"61\\", \\"master\\": null, \\"brkout_mode\\": \\"\\", \\"speed\\": \\"10000\\", \\"port\\": \\"\\"}}}}"
                                    }},
                                    "speed": {{
                                        "unit": "G",
                                        "value": 10
                                    }},
                                    "state": "active"
                                }},
                                {{
                                    "mapping": [
                                        9,
                                        1,
                                        1,
                                        1,
                                        9
                                    ],
                                    "name": "Ethernet9",
                                    "position": 9,
                                    "roles": [
                                        "generic"
                                    ],
                                    "setting": {{
                                        "param": "{{\\"interface\\": {{\\"index\\": \\"10\\", \\"lane_map\\": \\"62\\", \\"master\\": null, \\"brkout_mode\\": \\"\\", \\"speed\\": \\"10000\\", \\"port\\": \\"\\"}}}}"
                                    }},
                                    "speed": {{
                                        "unit": "G",
                                        "value": 10
                                    }},
                                    "state": "active"
                                }},
                                {{
                                    "mapping": [
                                        10,
                                        1,
                                        1,
                                        1,
                                        10
                                    ],
                                    "name": "Ethernet10",
                                    "position": 10,
                                    "roles": [
                                        "generic"
                                    ],
                                    "setting": {{
                                        "param": "{{\\"interface\\": {{\\"index\\": \\"11\\", \\"lane_map\\": \\"63\\", \\"master\\": null, \\"brkout_mode\\": \\"\\", \\"speed\\": \\"10000\\", \\"port\\": \\"\\"}}}}"
                                    }},
                                    "speed": {{
                                        "unit": "G",
                                        "value": 10
                                    }},
                                    "state": "active"
                                }},
                                {{
                                    "mapping": [
                                        11,
                                        1,
                                        1,
                                        1,
                                        11
                                    ],
                                    "name": "Ethernet11",
                                    "position": 11,
                                    "roles": [
                                        "peer"
                                    ],
                                    "setting": {{
                                        "param": "{{\\"interface\\": {{\\"index\\": \\"12\\", \\"lane_map\\": \\"64\\", \\"master\\": null, \\"brkout_mode\\": \\"\\", \\"speed\\": \\"10000\\", \\"port\\": \\"\\"}}}}"
                                    }},
                                    "speed": {{
                                        "unit": "G",
                                        "value": 10
                                    }},
                                    "state": "active"
                                }},
                                {{
                                    "mapping": [
                                        12,
                                        1,
                                        1,
                                        1,
                                        12
                                    ],
                                    "name": "Ethernet12",
                                    "position": 12,
                                    "roles": [
                                        "peer"
                                    ],
                                    "setting": {{
                                        "param": "{{\\"interface\\": {{\\"index\\": \\"13\\", \\"lane_map\\": \\"77\\", \\"master\\": null, \\"brkout_mode\\": \\"\\", \\"speed\\": \\"10000\\", \\"port\\": \\"\\"}}}}"
                                    }},
                                    "speed": {{
                                        "unit": "G",
                                        "value": 10
                                    }},
                                    "state": "active"
                                }},
                                {{
                                    "mapping": [
                                        13,
                                        1,
                                        1,
                                        null,
                                        null
                                    ],
                                    "name": "Ethernet13",
                                    "position": 13,
                                    "roles": [
                                        "unused"
                                    ],
                                    "setting": {{
                                        "param": "{{\\"interface\\": {{\\"index\\": \\"14\\", \\"lane_map\\": \\"78\\", \\"master\\": null, \\"brkout_mode\\": \\"\\", \\"speed\\": \\"10000\\", \\"port\\": \\"\\"}}}}"
                                    }},
                                    "speed": {{
                                        "unit": "G",
                                        "value": 10
                                    }},
                                    "state": "active"
                                }},
                                {{
                                    "mapping": [
                                        14,
                                        1,
                                        1,
                                        null,
                                        null
                                    ],
                                    "name": "Ethernet14",
                                    "position": 14,
                                    "roles": [
                                        "unused"
                                    ],
                                    "setting": {{
                                        "param": "{{\\"interface\\": {{\\"index\\": \\"15\\", \\"lane_map\\": \\"79\\", \\"master\\": null, \\"brkout_mode\\": \\"\\", \\"speed\\": \\"10000\\", \\"port\\": \\"\\"}}}}"
                                    }},
                                    "speed": {{
                                        "unit": "G",
                                        "value": 10
                                    }},
                                    "state": "active"
                                }}
                            ],
                            "label": "SONIC-12x10-Leaf",
                            "id": "SONIC-12x10-Leaf",
                            "logical_device_id": "SONIC-12x10-Leaf"
                             }}'''},



                            'SONIC-10x10-Spine': {'name': 'SONIC-10x10-Spine',
                                                            'data': f'''{{
                            "device_profile_id": "VS_SONIC_300_Generic",
                            "interfaces": [
                                {{
                                    "mapping": [
                                        1,
                                        1,
                                        1,
                                        1,
                                        1
                                    ],
                                    "name": "Ethernet1",
                                    "position": 1,
                                    "roles": [
                                        "superspine",
                                        "leaf"
                                    ],
                                    "setting": {{
                                        "param": "{{\\"interface\\": {{\\"index\\": \\"2\\", \\"lane_map\\": \\"50\\", \\"master\\": null, \\"brkout_mode\\": \\"\\", \\"speed\\": \\"10000\\", \\"port\\": \\"\\"}}}}"
                                    }},
                                    "speed": {{
                                        "unit": "G",
                                        "value": 10
                                    }},
                                    "state": "active"
                                }},
                                {{
                                    "mapping": [
                                        2,
                                        1,
                                        1,
                                        1,
                                        2
                                    ],
                                    "name": "Ethernet2",
                                    "position": 2,
                                    "roles": [
                                        "superspine",
                                        "leaf"
                                    ],
                                    "setting": {{
                                        "param": "{{\\"interface\\": {{\\"index\\": \\"3\\", \\"lane_map\\": \\"51\\", \\"master\\": null, \\"brkout_mode\\": \\"\\", \\"speed\\": \\"10000\\", \\"port\\": \\"\\"}}}}"
                                    }},
                                    "speed": {{
                                        "unit": "G",
                                        "value": 10
                                    }},
                                    "state": "active"
                                }},
                                {{
                                    "mapping": [
                                        3,
                                        1,
                                        1,
                                        1,
                                        3
                                    ],
                                    "name": "Ethernet3",
                                    "position": 3,
                                    "roles": [
                                        "superspine",
                                        "leaf"
                                    ],
                                    "setting": {{
                                        "param": "{{\\"interface\\": {{\\"index\\": \\"4\\", \\"lane_map\\": \\"52\\", \\"master\\": null, \\"brkout_mode\\": \\"\\", \\"speed\\": \\"10000\\", \\"port\\": \\"\\"}}}}"
                                    }},
                                    "speed": {{
                                        "unit": "G",
                                        "value": 10
                                    }},
                                    "state": "active"
                                }},
                                {{
                                    "mapping": [
                                        4,
                                        1,
                                        1,
                                        1,
                                        4
                                    ],
                                    "name": "Ethernet4",
                                    "position": 4,
                                    "roles": [
                                        "superspine",
                                        "leaf"
                                    ],
                                    "setting": {{
                                        "param": "{{\\"interface\\": {{\\"index\\": \\"5\\", \\"lane_map\\": \\"57\\", \\"master\\": null, \\"brkout_mode\\": \\"\\", \\"speed\\": \\"10000\\", \\"port\\": \\"\\"}}}}"
                                    }},
                                    "speed": {{
                                        "unit": "G",
                                        "value": 10
                                    }},
                                    "state": "active"
                                }},
                                {{
                                    "mapping": [
                                        5,
                                        1,
                                        1,
                                        1,
                                        5
                                    ],
                                    "name": "Ethernet5",
                                    "position": 5,
                                    "roles": [
                                        "superspine",
                                        "leaf"
                                    ],
                                    "setting": {{
                                        "param": "{{\\"interface\\": {{\\"index\\": \\"6\\", \\"lane_map\\": \\"58\\", \\"master\\": null, \\"brkout_mode\\": \\"\\", \\"speed\\": \\"10000\\", \\"port\\": \\"\\"}}}}"
                                    }},
                                    "speed": {{
                                        "unit": "G",
                                        "value": 10
                                    }},
                                    "state": "active"
                                }},
                                {{
                                    "mapping": [
                                        6,
                                        1,
                                        1,
                                        1,
                                        6
                                    ],
                                    "name": "Ethernet6",
                                    "position": 6,
                                    "roles": [
                                        "superspine",
                                        "leaf"
                                    ],
                                    "setting": {{
                                        "param": "{{\\"interface\\": {{\\"index\\": \\"7\\", \\"lane_map\\": \\"59\\", \\"master\\": null, \\"brkout_mode\\": \\"\\", \\"speed\\": \\"10000\\", \\"port\\": \\"\\"}}}}"
                                    }},
                                    "speed": {{
                                        "unit": "G",
                                        "value": 10
                                    }},
                                    "state": "active"
                                }},
                                {{
                                    "mapping": [
                                        7,
                                        1,
                                        1,
                                        1,
                                        7
                                    ],
                                    "name": "Ethernet7",
                                    "position": 7,
                                    "roles": [
                                        "superspine",
                                        "leaf"
                                    ],
                                    "setting": {{
                                        "param": "{{\\"interface\\": {{\\"index\\": \\"8\\", \\"lane_map\\": \\"60\\", \\"master\\": null, \\"brkout_mode\\": \\"\\", \\"speed\\": \\"10000\\", \\"port\\": \\"\\"}}}}"
                                    }},
                                    "speed": {{
                                        "unit": "G",
                                        "value": 10
                                    }},
                                    "state": "active"
                                }},
                                {{
                                    "mapping": [
                                        8,
                                        1,
                                        1,
                                        1,
                                        8
                                    ],
                                    "name": "Ethernet8",
                                    "position": 8,
                                    "roles": [
                                        "superspine",
                                        "leaf"
                                    ],
                                    "setting": {{
                                        "param": "{{\\"interface\\": {{\\"index\\": \\"9\\", \\"lane_map\\": \\"61\\", \\"master\\": null, \\"brkout_mode\\": \\"\\", \\"speed\\": \\"10000\\", \\"port\\": \\"\\"}}}}"
                                    }},
                                    "speed": {{
                                        "unit": "G",
                                        "value": 10
                                    }},
                                    "state": "active"
                                }},
                                {{
                                    "mapping": [
                                        9,
                                        1,
                                        1,
                                        1,
                                        9
                                    ],
                                    "name": "Ethernet9",
                                    "position": 9,
                                    "roles": [
                                        "generic"
                                    ],
                                    "setting": {{
                                        "param": "{{\\"interface\\": {{\\"index\\": \\"10\\", \\"lane_map\\": \\"62\\", \\"master\\": null, \\"brkout_mode\\": \\"\\", \\"speed\\": \\"10000\\", \\"port\\": \\"\\"}}}}"
                                    }},
                                    "speed": {{
                                        "unit": "G",
                                        "value": 10
                                    }},
                                    "state": "active"
                                }},
                                {{
                                    "mapping": [
                                        10,
                                        1,
                                        1,
                                        1,
                                        10
                                    ],
                                    "name": "Ethernet10",
                                    "position": 10,
                                    "roles": [
                                        "generic"
                                    ],
                                    "setting": {{
                                        "param": "{{\\"interface\\": {{\\"index\\": \\"11\\", \\"lane_map\\": \\"63\\", \\"master\\": null, \\"brkout_mode\\": \\"\\", \\"speed\\": \\"10000\\", \\"port\\": \\"\\"}}}}"
                                    }},
                                    "speed": {{
                                        "unit": "G",
                                        "value": 10
                                    }},
                                    "state": "active"
                                }},
                                {{
                                    "mapping": [
                                        11,
                                        1,
                                        1,
                                        null,
                                        null
                                    ],
                                    "name": "Ethernet11",
                                    "position": 11,
                                    "roles": [
                                        "unused"
                                    ],
                                    "setting": {{
                                        "param": "{{\\"interface\\": {{\\"index\\": \\"12\\", \\"lane_map\\": \\"64\\", \\"master\\": null, \\"brkout_mode\\": \\"\\", \\"speed\\": \\"10000\\", \\"port\\": \\"\\"}}}}"
                                    }},
                                    "speed": {{
                                        "unit": "G",
                                        "value": 10
                                    }},
                                    "state": "active"
                                }},
                                {{
                                    "mapping": [
                                        12,
                                        1,
                                        1,
                                        null,
                                        null
                                    ],
                                    "name": "Ethernet12",
                                    "position": 12,
                                    "roles": [
                                        "unused"
                                    ],
                                    "setting": {{
                                        "param": "{{\\"interface\\": {{\\"index\\": \\"13\\", \\"lane_map\\": \\"77\\", \\"master\\": null, \\"brkout_mode\\": \\"\\", \\"speed\\": \\"10000\\", \\"port\\": \\"\\"}}}}"
                                    }},
                                    "speed": {{
                                        "unit": "G",
                                        "value": 10
                                    }},
                                    "state": "active"
                                }},
                                {{
                                    "mapping": [
                                        13,
                                        1,
                                        1,
                                        null,
                                        null
                                    ],
                                    "name": "Ethernet13",
                                    "position": 13,
                                    "roles": [
                                        "unused"
                                    ],
                                    "setting": {{
                                        "param": "{{\\"interface\\": {{\\"index\\": \\"14\\", \\"lane_map\\": \\"78\\", \\"master\\": null, \\"brkout_mode\\": \\"\\", \\"speed\\": \\"10000\\", \\"port\\": \\"\\"}}}}"
                                    }},
                                    "speed": {{
                                        "unit": "G",
                                        "value": 10
                                    }},
                                    "state": "active"
                                }},
                                {{
                                    "mapping": [
                                        14,
                                        1,
                                        1,
                                        null,
                                        null
                                    ],
                                    "name": "Ethernet14",
                                    "position": 14,
                                    "roles": [
                                        "unused"
                                    ],
                                    "setting": {{
                                        "param": "{{\\"interface\\": {{\\"index\\": \\"15\\", \\"lane_map\\": \\"79\\", \\"master\\": null, \\"brkout_mode\\": \\"\\", \\"speed\\": \\"10000\\", \\"port\\": \\"\\"}}}}"
                                    }},
                                    "speed": {{
                                        "unit": "G",
                                        "value": 10
                                    }},
                                    "state": "active"
                                }}
                            ],
                            "label": "SONIC-10x10-Spine",
                            "id": "SONIC-10x10-Spine",
                            "logical_device_id": "SONIC-10x10-Spine"
                             }}'''},
                            }

    return interface_map_data_dic











