"""
---------------------------------
 Author: Gilberto Rampini
 Date: 12/2021
---------------------------------
"""
""" -------------- Device Profiles """


def create_device_profiles_dic():

    device_profiles_data_dic = {'JNPR_vQFX-7x10-Spine': {'name': 'VS_SONIC_300_Generic',
                                                       'data': f'''{{
                                "hardware_capabilities": {{
                                    "asic": "vs",
                                    "cpu": "x86",
                                    "ecmp_limit": 64,
                                    "form_factor": "1RU",
                                    "ram": 16,
                                    "userland": 64
                                }},
                                "id": "VS_SONIC_300_Generic",
                                "label": "VS_SONIC_300_Generic",
                                "ports": [
                                    {{
                                        "column_id": 1,
                                        "connector_type": "sfp28",
                                        "failure_domain_id": 1,
                                        "panel_id": 1,
                                        "port_id": 1,
                                        "row_id": 1,
                                        "slot_id": 0,
                                        "transformations": [
                                            {{
                                                "interfaces": [
                                                    {{
                                                        "interface_id": 1,
                                                        "name": "Ethernet1",
                                                        "setting": "{{\\"interface\\": {{\\"index\\": \\"2\\", \\"lane_map\\": \\"50\\", \\"master\\": null, \\"brkout_mode\\": \\"\\", \\"speed\\": \\"10000\\", \\"port\\": \\"\\"}}}}",
                                                        "speed": {{
                                                            "color": "blue",
                                                            "label": "10 Gbps",
                                                            "unit": "G",
                                                            "value": 10
                                                        }},
                                                        "state": "active"
                                                    }}
                                                ],
                                                "is_default": true,
                                                "transformation_id": 1
                                            }},
                                            {{
                                                "interfaces": [
                                                    {{
                                                        "interface_id": 1,
                                                        "name": "Ethernet1",
                                                        "setting": "{{\\"interface\\": {{\\"index\\": \\"2\\", \\"lane_map\\": \\"50\\", \\"master\\": null, \\"brkout_mode\\": \\"\\", \\"speed\\": \\"25000\\", \\"port\\": \\"\\"}}}}",
                                                        "speed": {{
                                                            "color": "yellow",
                                                            "label": "25 Gbps",
                                                            "unit": "G",
                                                            "value": 25
                                                        }},
                                                        "state": "active"
                                                    }}
                                                ],
                                                "is_default": false,
                                                "transformation_id": 2
                                            }}
                                        ]
                                    }},
                                    {{
                                        "column_id": 2,
                                        "connector_type": "sfp28",
                                        "failure_domain_id": 1,
                                        "panel_id": 1,
                                        "port_id": 2,
                                        "row_id": 1,
                                        "slot_id": 0,
                                        "transformations": [
                                            {{
                                                "interfaces": [
                                                    {{
                                                        "interface_id": 1,
                                                        "name": "Ethernet2",
                                                        "setting": "{{\\"interface\\": {{\\"index\\": \\"3\\", \\"lane_map\\": \\"51\\", \\"master\\": null, \\"brkout_mode\\": \\"\\", \\"speed\\": \\"10000\\", \\"port\\": \\"\\"}}}}",
                                                        "speed": {{
                                                            "color": "blue",
                                                            "label": "10 Gbps",
                                                            "unit": "G",
                                                            "value": 10
                                                        }},
                                                        "state": "active"
                                                    }}
                                                ],
                                                "is_default": true,
                                                "transformation_id": 1
                                            }},
                                            {{
                                                "interfaces": [
                                                    {{
                                                        "interface_id": 1,
                                                        "name": "Ethernet2",
                                                        "setting": "{{\\"interface\\": {{\\"index\\": \\"3\\", \\"lane_map\\": \\"51\\", \\"master\\": null, \\"brkout_mode\\": \\"\\", \\"speed\\": \\"25000\\", \\"port\\": \\"\\"}}}}",
                                                        "speed": {{
                                                            "color": "yellow",
                                                            "label": "25 Gbps",
                                                            "unit": "G",
                                                            "value": 25
                                                        }},
                                                        "state": "active"
                                                    }}
                                                ],
                                                "is_default": false,
                                                "transformation_id": 2
                                            }}
                                        ]
                                    }},
                                    {{
                                        "column_id": 3,
                                        "connector_type": "sfp28",
                                        "failure_domain_id": 1,
                                        "panel_id": 1,
                                        "port_id": 3,
                                        "row_id": 1,
                                        "slot_id": 0,
                                        "transformations": [
                                            {{
                                                "interfaces": [
                                                    {{
                                                        "interface_id": 1,
                                                        "name": "Ethernet3",
                                                        "setting": "{{\\"interface\\": {{\\"index\\": \\"4\\", \\"lane_map\\": \\"52\\", \\"master\\": null, \\"brkout_mode\\": \\"\\", \\"speed\\": \\"10000\\", \\"port\\": \\"\\"}}}}",
                                                        "speed": {{
                                                            "color": "blue",
                                                            "label": "10 Gbps",
                                                            "unit": "G",
                                                            "value": 10
                                                        }},
                                                        "state": "active"
                                                    }}
                                                ],
                                                "is_default": true,
                                                "transformation_id": 1
                                            }},
                                            {{
                                                "interfaces": [
                                                    {{
                                                        "interface_id": 1,
                                                        "name": "Ethernet3",
                                                        "setting": "{{\\"interface\\": {{\\"index\\": \\"4\\", \\"lane_map\\": \\"52\\", \\"master\\": null, \\"brkout_mode\\": \\"\\", \\"speed\\": \\"25000\\", \\"port\\": \\"\\"}}}}",
                                                        "speed": {{
                                                            "color": "yellow",
                                                            "label": "25 Gbps",
                                                            "unit": "G",
                                                            "value": 25
                                                        }},
                                                        "state": "active"
                                                    }}
                                                ],
                                                "is_default": false,
                                                "transformation_id": 2
                                            }}
                                        ]
                                    }},
                                    {{
                                        "column_id": 4,
                                        "connector_type": "sfp28",
                                        "failure_domain_id": 1,
                                        "panel_id": 1,
                                        "port_id": 4,
                                        "row_id": 1,
                                        "slot_id": 0,
                                        "transformations": [
                                            {{
                                                "interfaces": [
                                                    {{
                                                        "interface_id": 1,
                                                        "name": "Ethernet4",
                                                        "setting": "{{\\"interface\\": {{\\"index\\": \\"5\\", \\"lane_map\\": \\"57\\", \\"master\\": null, \\"brkout_mode\\": \\"\\", \\"speed\\": \\"10000\\", \\"port\\": \\"\\"}}}}",
                                                        "speed": {{
                                                            "color": "blue",
                                                            "label": "10 Gbps",
                                                            "unit": "G",
                                                            "value": 10
                                                        }},
                                                        "state": "active"
                                                    }}
                                                ],
                                                "is_default": true,
                                                "transformation_id": 1
                                            }},
                                            {{
                                                "interfaces": [
                                                    {{
                                                        "interface_id": 1,
                                                        "name": "Ethernet4",
                                                        "setting": "{{\\"interface\\": {{\\"index\\": \\"5\\", \\"lane_map\\": \\"57\\", \\"master\\": null, \\"brkout_mode\\": \\"\\", \\"speed\\": \\"25000\\", \\"port\\": \\"\\"}}}}",
                                                        "speed": {{
                                                            "color": "yellow",
                                                            "label": "25 Gbps",
                                                            "unit": "G",
                                                            "value": 25
                                                        }},
                                                        "state": "active"
                                                    }}
                                                ],
                                                "is_default": false,
                                                "transformation_id": 2
                                            }}
                                        ]
                                    }},
                                    {{
                                        "column_id": 5,
                                        "connector_type": "sfp28",
                                        "failure_domain_id": 1,
                                        "panel_id": 1,
                                        "port_id": 5,
                                        "row_id": 1,
                                        "slot_id": 0,
                                        "transformations": [
                                            {{
                                                "interfaces": [
                                                    {{
                                                        "interface_id": 1,
                                                        "name": "Ethernet5",
                                                        "setting": "{{\\"interface\\": {{\\"index\\": \\"6\\", \\"lane_map\\": \\"58\\", \\"master\\": null, \\"brkout_mode\\": \\"\\", \\"speed\\": \\"10000\\", \\"port\\": \\"\\"}}}}",
                                                        "speed": {{
                                                            "color": "blue",
                                                            "label": "10 Gbps",
                                                            "unit": "G",
                                                            "value": 10
                                                        }},
                                                        "state": "active"
                                                    }}
                                                ],
                                                "is_default": true,
                                                "transformation_id": 1
                                            }},
                                            {{
                                                "interfaces": [
                                                    {{
                                                        "interface_id": 1,
                                                        "name": "Ethernet5",
                                                        "setting": "{{\\"interface\\": {{\\"index\\": \\"6\\", \\"lane_map\\": \\"58\\", \\"master\\": null, \\"brkout_mode\\": \\"\\", \\"speed\\": \\"25000\\", \\"port\\": \\"\\"}}}}",
                                                        "speed": {{
                                                            "color": "yellow",
                                                            "label": "25 Gbps",
                                                            "unit": "G",
                                                            "value": 25
                                                        }},
                                                        "state": "active"
                                                    }}
                                                ],
                                                "is_default": false,
                                                "transformation_id": 2
                                            }}
                                        ]
                                    }},
                                    {{
                                        "column_id": 6,
                                        "connector_type": "sfp28",
                                        "failure_domain_id": 1,
                                        "panel_id": 1,
                                        "port_id": 6,
                                        "row_id": 1,
                                        "slot_id": 0,
                                        "transformations": [
                                            {{
                                                "interfaces": [
                                                    {{
                                                        "interface_id": 1,
                                                        "name": "Ethernet6",
                                                        "setting": "{{\\"interface\\": {{\\"index\\": \\"7\\", \\"lane_map\\": \\"59\\", \\"master\\": null, \\"brkout_mode\\": \\"\\", \\"speed\\": \\"10000\\", \\"port\\": \\"\\"}}}}",
                                                        "speed": {{
                                                            "color": "blue",
                                                            "label": "10 Gbps",
                                                            "unit": "G",
                                                            "value": 10
                                                        }},
                                                        "state": "active"
                                                    }}
                                                ],
                                                "is_default": true,
                                                "transformation_id": 1
                                            }},
                                            {{
                                                "interfaces": [
                                                    {{
                                                        "interface_id": 1,
                                                        "name": "Ethernet6",
                                                        "setting": "{{\\"interface\\": {{\\"index\\": \\"7\\", \\"lane_map\\": \\"59\\", \\"master\\": null, \\"brkout_mode\\": \\"\\", \\"speed\\": \\"25000\\", \\"port\\": \\"\\"}}}}",
                                                        "speed": {{
                                                            "color": "yellow",
                                                            "label": "25 Gbps",
                                                            "unit": "G",
                                                            "value": 25
                                                        }},
                                                        "state": "active"
                                                    }}
                                                ],
                                                "is_default": false,
                                                "transformation_id": 2
                                            }}
                                        ]
                                    }},
                                    {{
                                        "column_id": 7,
                                        "connector_type": "sfp28",
                                        "failure_domain_id": 1,
                                        "panel_id": 1,
                                        "port_id": 7,
                                        "row_id": 1,
                                        "slot_id": 0,
                                        "transformations": [
                                            {{
                                                "interfaces": [
                                                    {{
                                                        "interface_id": 1,
                                                        "name": "Ethernet7",
                                                        "setting": "{{\\"interface\\": {{\\"index\\": \\"8\\", \\"lane_map\\": \\"60\\", \\"master\\": null, \\"brkout_mode\\": \\"\\", \\"speed\\": \\"10000\\", \\"port\\": \\"\\"}}}}",
                                                        "speed": {{
                                                            "color": "blue",
                                                            "label": "10 Gbps",
                                                            "unit": "G",
                                                            "value": 10
                                                        }},
                                                        "state": "active"
                                                    }}
                                                ],
                                                "is_default": true,
                                                "transformation_id": 1
                                            }},
                                            {{
                                                "interfaces": [
                                                    {{
                                                        "interface_id": 1,
                                                        "name": "Ethernet7",
                                                        "setting": "{{\\"interface\\": {{\\"index\\": \\"8\\", \\"lane_map\\": \\"60\\", \\"master\\": null, \\"brkout_mode\\": \\"\\", \\"speed\\": \\"25000\\", \\"port\\": \\"\\"}}}}",
                                                        "speed": {{
                                                            "color": "yellow",
                                                            "label": "25 Gbps",
                                                            "unit": "G",
                                                            "value": 25
                                                        }},
                                                        "state": "active"
                                                    }}
                                                ],
                                                "is_default": false,
                                                "transformation_id": 2
                                            }}
                                        ]
                                    }},
                                    {{
                                        "column_id": 8,
                                        "connector_type": "sfp28",
                                        "failure_domain_id": 1,
                                        "panel_id": 1,
                                        "port_id": 8,
                                        "row_id": 1,
                                        "slot_id": 0,
                                        "transformations": [
                                            {{
                                                "interfaces": [
                                                    {{
                                                        "interface_id": 1,
                                                        "name": "Ethernet8",
                                                        "setting": "{{\\"interface\\": {{\\"index\\": \\"9\\", \\"lane_map\\": \\"61\\", \\"master\\": null, \\"brkout_mode\\": \\"\\", \\"speed\\": \\"10000\\", \\"port\\": \\"\\"}}}}",
                                                        "speed": {{
                                                            "color": "blue",
                                                            "label": "10 Gbps",
                                                            "unit": "G",
                                                            "value": 10
                                                        }},
                                                        "state": "active"
                                                    }}
                                                ],
                                                "is_default": true,
                                                "transformation_id": 1
                                            }},
                                            {{
                                                "interfaces": [
                                                    {{
                                                        "interface_id": 1,
                                                        "name": "Ethernet8",
                                                        "setting": "{{\\"interface\\": {{\\"index\\": \\"9\\", \\"lane_map\\": \\"61\\", \\"master\\": null, \\"brkout_mode\\": \\"\\", \\"speed\\": \\"25000\\", \\"port\\": \\"\\"}}}}",
                                                        "speed": {{
                                                            "color": "yellow",
                                                            "label": "25 Gbps",
                                                            "unit": "G",
                                                            "value": 25
                                                        }},
                                                        "state": "active"
                                                    }}
                                                ],
                                                "is_default": false,
                                                "transformation_id": 2
                                            }}
                                        ]
                                    }},
                                    {{
                                        "column_id": 9,
                                        "connector_type": "sfp28",
                                        "failure_domain_id": 1,
                                        "panel_id": 1,
                                        "port_id": 9,
                                        "row_id": 1,
                                        "slot_id": 0,
                                        "transformations": [
                                            {{
                                                "interfaces": [
                                                    {{
                                                        "interface_id": 1,
                                                        "name": "Ethernet9",
                                                        "setting": "{{\\"interface\\": {{\\"index\\": \\"10\\", \\"lane_map\\": \\"62\\", \\"master\\": null, \\"brkout_mode\\": \\"\\", \\"speed\\": \\"10000\\", \\"port\\": \\"\\"}}}}",
                                                        "speed": {{
                                                            "color": "blue",
                                                            "label": "10 Gbps",
                                                            "unit": "G",
                                                            "value": 10
                                                        }},
                                                        "state": "active"
                                                    }}
                                                ],
                                                "is_default": true,
                                                "transformation_id": 1
                                            }},
                                            {{
                                                "interfaces": [
                                                    {{
                                                        "interface_id": 1,
                                                        "name": "Ethernet9",
                                                        "setting": "{{\\"interface\\": {{\\"index\\": \\"10\\", \\"lane_map\\": \\"62\\", \\"master\\": null, \\"brkout_mode\\": \\"\\", \\"speed\\": \\"25000\\", \\"port\\": \\"\\"}}}}",
                                                        "speed": {{
                                                            "color": "yellow",
                                                            "label": "25 Gbps",
                                                            "unit": "G",
                                                            "value": 25
                                                        }},
                                                        "state": "active"
                                                    }}
                                                ],
                                                "is_default": false,
                                                "transformation_id": 2
                                            }}
                                        ]
                                    }},
                                    {{
                                        "column_id": 10,
                                        "connector_type": "sfp28",
                                        "failure_domain_id": 1,
                                        "panel_id": 1,
                                        "port_id": 10,
                                        "row_id": 1,
                                        "slot_id": 0,
                                        "transformations": [
                                            {{
                                                "interfaces": [
                                                    {{
                                                        "interface_id": 1,
                                                        "name": "Ethernet10",
                                                        "setting": "{{\\"interface\\": {{\\"index\\": \\"11\\", \\"lane_map\\": \\"63\\", \\"master\\": null, \\"brkout_mode\\": \\"\\", \\"speed\\": \\"10000\\", \\"port\\": \\"\\"}}}}",
                                                        "speed": {{
                                                            "color": "blue",
                                                            "label": "10 Gbps",
                                                            "unit": "G",
                                                            "value": 10
                                                        }},
                                                        "state": "active"
                                                    }}
                                                ],
                                                "is_default": true,
                                                "transformation_id": 1
                                            }},
                                            {{
                                                "interfaces": [
                                                    {{
                                                        "interface_id": 1,
                                                        "name": "Ethernet10",
                                                        "setting": "{{\\"interface\\": {{\\"index\\": \\"11\\", \\"lane_map\\": \\"63\\", \\"master\\": null, \\"brkout_mode\\": \\"\\", \\"speed\\": \\"25000\\", \\"port\\": \\"\\"}}}}",
                                                        "speed": {{
                                                            "color": "yellow",
                                                            "label": "25 Gbps",
                                                            "unit": "G",
                                                            "value": 25
                                                        }},
                                                        "state": "active"
                                                    }}
                                                ],
                                                "is_default": false,
                                                "transformation_id": 2
                                            }}
                                        ]
                                    }},
                                    {{
                                        "column_id": 11,
                                        "connector_type": "sfp28",
                                        "failure_domain_id": 1,
                                        "panel_id": 1,
                                        "port_id": 11,
                                        "row_id": 1,
                                        "slot_id": 0,
                                        "transformations": [
                                            {{
                                                "interfaces": [
                                                    {{
                                                        "interface_id": 1,
                                                        "name": "Ethernet11",
                                                        "setting": "{{\\"interface\\": {{\\"index\\": \\"12\\", \\"lane_map\\": \\"64\\", \\"master\\": null, \\"brkout_mode\\": \\"\\", \\"speed\\": \\"10000\\", \\"port\\": \\"\\"}}}}",
                                                        "speed": {{
                                                            "color": "blue",
                                                            "label": "10 Gbps",
                                                            "unit": "G",
                                                            "value": 10
                                                        }},
                                                        "state": "active"
                                                    }}
                                                ],
                                                "is_default": true,
                                                "transformation_id": 1
                                            }},
                                            {{
                                                "interfaces": [
                                                    {{
                                                        "interface_id": 1,
                                                        "name": "Ethernet11",
                                                        "setting": "{{\\"interface\\": {{\\"index\\": \\"12\\", \\"lane_map\\": \\"64\\", \\"master\\": null, \\"brkout_mode\\": \\"\\", \\"speed\\": \\"25000\\", \\"port\\": \\"\\"}}}}",
                                                        "speed": {{
                                                            "color": "yellow",
                                                            "label": "25 Gbps",
                                                            "unit": "G",
                                                            "value": 25
                                                        }},
                                                        "state": "active"
                                                    }}
                                                ],
                                                "is_default": false,
                                                "transformation_id": 2
                                            }}
                                        ]
                                    }},
                                    {{
                                        "column_id": 12,
                                        "connector_type": "sfp28",
                                        "failure_domain_id": 1,
                                        "panel_id": 1,
                                        "port_id": 12,
                                        "row_id": 1,
                                        "slot_id": 0,
                                        "transformations": [
                                            {{
                                                "interfaces": [
                                                    {{
                                                        "interface_id": 1,
                                                        "name": "Ethernet12",
                                                        "setting": "{{\\"interface\\": {{\\"index\\": \\"13\\", \\"lane_map\\": \\"77\\", \\"master\\": null, \\"brkout_mode\\": \\"\\", \\"speed\\": \\"10000\\", \\"port\\": \\"\\"}}}}",
                                                        "speed": {{
                                                            "color": "blue",
                                                            "label": "10 Gbps",
                                                            "unit": "G",
                                                            "value": 10
                                                        }},
                                                        "state": "active"
                                                    }}
                                                ],
                                                "is_default": true,
                                                "transformation_id": 1
                                            }},
                                            {{
                                                "interfaces": [
                                                    {{
                                                        "interface_id": 1,
                                                        "name": "Ethernet12",
                                                        "setting": "{{\\"interface\\": {{\\"index\\": \\"13\\", \\"lane_map\\": \\"77\\", \\"master\\": null, \\"brkout_mode\\": \\"\\", \\"speed\\": \\"25000\\", \\"port\\": \\"\\"}}}}",
                                                        "speed": {{
                                                            "color": "yellow",
                                                            "label": "25 Gbps",
                                                            "unit": "G",
                                                            "value": 25
                                                        }},
                                                        "state": "active"
                                                    }}
                                                ],
                                                "is_default": false,
                                                "transformation_id": 2
                                            }}
                                        ]
                                    }},
                                    {{
                                        "column_id": 13,
                                        "connector_type": "sfp28",
                                        "failure_domain_id": 1,
                                        "panel_id": 1,
                                        "port_id": 13,
                                        "row_id": 1,
                                        "slot_id": 0,
                                        "transformations": [
                                            {{
                                                "interfaces": [
                                                    {{
                                                        "interface_id": 1,
                                                        "name": "Ethernet13",
                                                        "setting": "{{\\"interface\\": {{\\"index\\": \\"14\\", \\"lane_map\\": \\"78\\", \\"master\\": null, \\"brkout_mode\\": \\"\\", \\"speed\\": \\"10000\\", \\"port\\": \\"\\"}}}}",
                                                        "speed": {{
                                                            "color": "blue",
                                                            "label": "10 Gbps",
                                                            "unit": "G",
                                                            "value": 10
                                                        }},
                                                        "state": "active"
                                                    }}
                                                ],
                                                "is_default": true,
                                                "transformation_id": 1
                                            }},
                                            {{
                                                "interfaces": [
                                                    {{
                                                        "interface_id": 1,
                                                        "name": "Ethernet13",
                                                        "setting": "{{\\"interface\\": {{\\"index\\": \\"14\\", \\"lane_map\\": \\"78\\", \\"master\\": null, \\"brkout_mode\\": \\"\\", \\"speed\\": \\"25000\\", \\"port\\": \\"\\"}}}}",
                                                        "speed": {{
                                                            "color": "yellow",
                                                            "label": "25 Gbps",
                                                            "unit": "G",
                                                            "value": 25
                                                        }},
                                                        "state": "active"
                                                    }}
                                                ],
                                                "is_default": false,
                                                "transformation_id": 2
                                            }}
                                        ]
                                    }},
                                    {{
                                        "column_id": 14,
                                        "connector_type": "sfp28",
                                        "failure_domain_id": 1,
                                        "panel_id": 1,
                                        "port_id": 14,
                                        "row_id": 1,
                                        "slot_id": 0,
                                        "transformations": [
                                            {{
                                                "interfaces": [
                                                    {{
                                                        "interface_id": 1,
                                                        "name": "Ethernet14",
                                                        "setting": "{{\\"interface\\": {{\\"index\\": \\"15\\", \\"lane_map\\": \\"79\\", \\"master\\": null, \\"brkout_mode\\": \\"\\", \\"speed\\": \\"10000\\", \\"port\\": \\"\\"}}}}",
                                                        "speed": {{
                                                            "color": "blue",
                                                            "label": "10 Gbps",
                                                            "unit": "G",
                                                            "value": 10
                                                        }},
                                                        "state": "active"
                                                    }}
                                                ],
                                                "is_default": true,
                                                "transformation_id": 1
                                            }},
                                            {{
                                                "interfaces": [
                                                    {{
                                                        "interface_id": 1,
                                                        "name": "Ethernet14",
                                                        "setting": "{{\\"interface\\": {{\\"index\\": \\"15\\", \\"lane_map\\": \\"79\\", \\"master\\": null, \\"brkout_mode\\": \\"\\", \\"speed\\": \\"25000\\", \\"port\\": \\"\\"}}}}",
                                                        "speed": {{
                                                            "color": "yellow",
                                                            "label": "25 Gbps",
                                                            "unit": "G",
                                                            "value": 25
                                                        }},
                                                        "state": "active"
                                                    }}
                                                ],
                                                "is_default": false,
                                                "transformation_id": 2
                                            }}
                                        ]
                                    }}
                                ],
                                "selector": {{
                                    "manufacturer": "Virtual_Machine",
                                    "model": "vs-sonic-vm",
                                    "os": "SONiC",
                                    "os_version": ".*3.3.0-Generic"
                                }},
                                "slot_count": 0,
                                "software_capabilities": {{
                                    "config_apply_support": "incremental",
                                    "lxc_support": false,
                                    "onie": true
                                }}
                            }}'''}, }

    return device_profiles_data_dic











