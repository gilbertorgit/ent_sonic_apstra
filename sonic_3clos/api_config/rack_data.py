"""
---------------------------------
 Author: Gilberto Rampini
 Date: 12/2021
---------------------------------
"""
""" Rack Type Data """


def create_rack_type_dic():

    rack_type_dic = {'SONIC-BORDER-LEAF': {'name': 'SONIC-BORDER-LEAF',
                                          'data': f'''{{
                    "access_switches": [],
                    "description": "SONIC-BORDER-LEAF",
                    "display_name": "SONIC-BORDER-LEAF",
                    "fabric_connectivity_design": "l3clos",
                    "generic_systems": [
                        {{
                            "asn_domain": "disabled",
                            "count": 1,
                            "label": "external-router",
                            "links": [
                                {{
                                    "attachment_type": "singleAttached",
                                    "label": "external-router -link-1",
                                    "lag_mode": null,
                                    "leaf_peer": null,
                                    "link_per_switch_count": 1,
                                    "link_speed": {{
                                        "unit": "G",
                                        "value": 10
                                    }},
                                    "tags": [
                                        "borderleaf-external-link"
                                    ],
                                    "target_switch_label": "SONIC-BORDER-LEAF"
                                }}
                            ],
                            "logical_device": "AOS-1x10-1",
                            "loopback": "disabled",
                            "management_level": "unmanaged",
                            "port_channel_id_max": 0,
                            "port_channel_id_min": 0
                        }}
                    ],
                    "id": "SONIC-BORDER-LEAF",
                    "last_modified_at": null,
                    "leafs": [
                        {{
                            "label": "SONIC-BORDER-LEAF",
                            "leaf_leaf_l3_link_count": 0,
                            "leaf_leaf_l3_link_port_channel_id": 0,
                            "leaf_leaf_l3_link_speed": null,
                            "leaf_leaf_link_count": 0,
                            "leaf_leaf_link_port_channel_id": 0,
                            "leaf_leaf_link_speed": null,
                            "link_per_spine_count": 1,
                            "link_per_spine_speed": {{
                                "unit": "G",
                                "value": 10
                            }},
                            "logical_device": "SONIC-10x10-BorderLeaf",
                            "redundancy_protocol": null,
                            "tags": [
                                "borderleaf"
                            ]
                        }}
                    ],
                    "logical_devices": [
                        {{
                            "display_name": "SONIC-10x10-BorderLeaf",
                            "href": "#/design/logical-devices/SONIC-10x10-BorderLeaf",
                            "id": "SONIC-10x10-BorderLeaf",
                            "panels": [
                                {{
                                    "panel_layout": {{
                                        "column_count": 10,
                                        "row_count": 1
                                    }},
                                    "port_groups": [
                                        {{
                                            "count": 4,
                                            "roles": [
                                                "spine"
                                            ],
                                            "speed": {{
                                                "unit": "G",
                                                "value": 10
                                            }}
                                        }},
                                        {{
                                            "count": 6,
                                            "roles": [
                                                "generic"
                                            ],
                                            "speed": {{
                                                "unit": "G",
                                                "value": 10
                                            }}
                                        }}
                                    ],
                                    "port_indexing": {{
                                        "order": "T-B, L-R",
                                        "schema": "absolute",
                                        "start_index": 1
                                    }}
                                }}
                            ]
                        }},
                        {{
                            "display_name": "AOS-1x10-1",
                            "href": "#/design/logical-devices/AOS-1x10-1",
                            "id": "AOS-1x10-1",
                            "panels": [
                                {{
                                    "panel_layout": {{
                                        "column_count": 1,
                                        "row_count": 1
                                    }},
                                    "port_groups": [
                                        {{
                                            "count": 1,
                                            "roles": [
                                                "leaf",
                                                "access"
                                            ],
                                            "speed": {{
                                                "unit": "G",
                                                "value": 10
                                            }}
                                        }}
                                    ],
                                    "port_indexing": {{
                                        "order": "T-B, L-R",
                                        "schema": "absolute",
                                        "start_index": 1
                                    }}
                                }}
                            ]
                        }},
                        {{
                            "display_name": "SONIC-10x10-BorderLeaf",
                            "href": "#/design/logical-devices/SONIC-10x10-BorderLeaf",
                            "id": "SONIC-10x10-BorderLeaf",
                            "panels": [
                                {{
                                    "panel_layout": {{
                                        "column_count": 10,
                                        "row_count": 1
                                    }},
                                    "port_groups": [
                                        {{
                                            "count": 4,
                                            "roles": [
                                                "spine"
                                            ],
                                            "speed": {{
                                                "unit": "G",
                                                "value": 10
                                            }}
                                        }},
                                        {{
                                            "count": 6,
                                            "roles": [
                                                "generic"
                                            ],
                                            "speed": {{
                                                "unit": "G",
                                                "value": 10
                                            }}
                                        }}
                                    ],
                                    "port_indexing": {{
                                        "order": "T-B, L-R",
                                        "schema": "absolute",
                                        "start_index": 1
                                    }}
                                }}
                            ]
                        }},
                        {{
                            "display_name": "AOS-1x10-1",
                            "href": "#/design/logical-devices/AOS-1x10-1",
                            "id": "AOS-1x10-1",
                            "panels": [
                                {{
                                    "panel_layout": {{
                                        "column_count": 1,
                                        "row_count": 1
                                    }},
                                    "port_groups": [
                                        {{
                                            "count": 1,
                                            "roles": [
                                                "leaf",
                                                "access"
                                            ],
                                            "speed": {{
                                                "unit": "G",
                                                "value": 10
                                            }}
                                        }}
                                    ],
                                    "port_indexing": {{
                                        "order": "T-B, L-R",
                                        "schema": "absolute",
                                        "start_index": 1
                                    }}
                                }}
                            ]
                        }},
                        {{
                            "display_name": "SONIC-10x10-BorderLeaf",
                            "href": "#/design/logical-devices/SONIC-10x10-BorderLeaf",
                            "id": "SONIC-10x10-BorderLeaf",
                            "panels": [
                                {{
                                    "panel_layout": {{
                                        "column_count": 10,
                                        "row_count": 1
                                    }},
                                    "port_groups": [
                                        {{
                                            "count": 4,
                                            "roles": [
                                                "spine"
                                            ],
                                            "speed": {{
                                                "unit": "G",
                                                "value": 10
                                            }}
                                        }},
                                        {{
                                            "count": 6,
                                            "roles": [
                                                "generic"
                                            ],
                                            "speed": {{
                                                "unit": "G",
                                                "value": 10
                                            }}
                                        }}
                                    ],
                                    "port_indexing": {{
                                        "order": "T-B, L-R",
                                        "schema": "absolute",
                                        "start_index": 1
                                    }}
                                }}
                            ]
                        }},
                        {{
                            "display_name": "AOS-1x10-1",
                            "href": "#/design/logical-devices/AOS-1x10-1",
                            "id": "AOS-1x10-1",
                            "panels": [
                                {{
                                    "panel_layout": {{
                                        "column_count": 1,
                                        "row_count": 1
                                    }},
                                    "port_groups": [
                                        {{
                                            "count": 1,
                                            "roles": [
                                                "leaf",
                                                "access"
                                            ],
                                            "speed": {{
                                                "unit": "G",
                                                "value": 10
                                            }}
                                        }}
                                    ],
                                    "port_indexing": {{
                                        "order": "T-B, L-R",
                                        "schema": "absolute",
                                        "start_index": 1
                                    }}
                                }}
                            ]
                        }},
                        {{
                            "display_name": "SONIC-10x10-BorderLeaf",
                            "href": "#/design/logical-devices/SONIC-10x10-BorderLeaf",
                            "id": "SONIC-10x10-BorderLeaf",
                            "panels": [
                                {{
                                    "panel_layout": {{
                                        "column_count": 10,
                                        "row_count": 1
                                    }},
                                    "port_groups": [
                                        {{
                                            "count": 4,
                                            "roles": [
                                                "spine"
                                            ],
                                            "speed": {{
                                                "unit": "G",
                                                "value": 10
                                            }}
                                        }},
                                        {{
                                            "count": 6,
                                            "roles": [
                                                "generic"
                                            ],
                                            "speed": {{
                                                "unit": "G",
                                                "value": 10
                                            }}
                                        }}
                                    ],
                                    "port_indexing": {{
                                        "order": "T-B, L-R",
                                        "schema": "absolute",
                                        "start_index": 1
                                    }}
                                }}
                            ]
                        }},
                        {{
                            "display_name": "AOS-1x10-1",
                            "href": "#/design/logical-devices/AOS-1x10-1",
                            "id": "AOS-1x10-1",
                            "panels": [
                                {{
                                    "panel_layout": {{
                                        "column_count": 1,
                                        "row_count": 1
                                    }},
                                    "port_groups": [
                                        {{
                                            "count": 1,
                                            "roles": [
                                                "leaf",
                                                "access"
                                            ],
                                            "speed": {{
                                                "unit": "G",
                                                "value": 10
                                            }}
                                        }}
                                    ],
                                    "port_indexing": {{
                                        "order": "T-B, L-R",
                                        "schema": "absolute",
                                        "start_index": 1
                                    }}
                                }}
                            ]
                        }},
                        {{
                            "display_name": "SONIC-10x10-BorderLeaf",
                            "href": "#/design/logical-devices/SONIC-10x10-BorderLeaf",
                            "id": "SONIC-10x10-BorderLeaf",
                            "panels": [
                                {{
                                    "panel_layout": {{
                                        "column_count": 10,
                                        "row_count": 1
                                    }},
                                    "port_groups": [
                                        {{
                                            "count": 4,
                                            "roles": [
                                                "spine"
                                            ],
                                            "speed": {{
                                                "unit": "G",
                                                "value": 10
                                            }}
                                        }},
                                        {{
                                            "count": 6,
                                            "roles": [
                                                "generic"
                                            ],
                                            "speed": {{
                                                "unit": "G",
                                                "value": 10
                                            }}
                                        }}
                                    ],
                                    "port_indexing": {{
                                        "order": "T-B, L-R",
                                        "schema": "absolute",
                                        "start_index": 1
                                    }}
                                }}
                            ]
                        }},
                        {{
                            "display_name": "SONIC-10x10-BorderLeaf",
                            "href": "#/design/logical-devices/SONIC-10x10-BorderLeaf",
                            "id": "SONIC-10x10-BorderLeaf",
                            "panels": [
                                {{
                                    "panel_layout": {{
                                        "column_count": 10,
                                        "row_count": 1
                                    }},
                                    "port_groups": [
                                        {{
                                            "count": 4,
                                            "roles": [
                                                "spine"
                                            ],
                                            "speed": {{
                                                "unit": "G",
                                                "value": 10
                                            }}
                                        }},
                                        {{
                                            "count": 6,
                                            "roles": [
                                                "generic"
                                            ],
                                            "speed": {{
                                                "unit": "G",
                                                "value": 10
                                            }}
                                        }}
                                    ],
                                    "port_indexing": {{
                                        "order": "T-B, L-R",
                                        "schema": "absolute",
                                        "start_index": 1
                                    }}
                                }}
                            ]
                        }},
                        {{
                            "display_name": "SONIC-10x10-BorderLeaf",
                            "href": "#/design/logical-devices/SONIC-10x10-BorderLeaf",
                            "id": "SONIC-10x10-BorderLeaf",
                            "panels": [
                                {{
                                    "panel_layout": {{
                                        "column_count": 10,
                                        "row_count": 1
                                    }},
                                    "port_groups": [
                                        {{
                                            "count": 4,
                                            "roles": [
                                                "spine"
                                            ],
                                            "speed": {{
                                                "unit": "G",
                                                "value": 10
                                            }}
                                        }},
                                        {{
                                            "count": 6,
                                            "roles": [
                                                "generic"
                                            ],
                                            "speed": {{
                                                "unit": "G",
                                                "value": 10
                                            }}
                                        }}
                                    ],
                                    "port_indexing": {{
                                        "order": "T-B, L-R",
                                        "schema": "absolute",
                                        "start_index": 1
                                    }}
                                }}
                            ]
                        }},
                        {{
                            "display_name": "SONIC-10x10-BorderLeaf",
                            "href": "#/design/logical-devices/SONIC-10x10-BorderLeaf",
                            "id": "SONIC-10x10-BorderLeaf",
                            "panels": [
                                {{
                                    "panel_layout": {{
                                        "column_count": 10,
                                        "row_count": 1
                                    }},
                                    "port_groups": [
                                        {{
                                            "count": 4,
                                            "roles": [
                                                "spine"
                                            ],
                                            "speed": {{
                                                "unit": "G",
                                                "value": 10
                                            }}
                                        }},
                                        {{
                                            "count": 6,
                                            "roles": [
                                                "generic"
                                            ],
                                            "speed": {{
                                                "unit": "G",
                                                "value": 10
                                            }}
                                        }}
                                    ],
                                    "port_indexing": {{
                                        "order": "T-B, L-R",
                                        "schema": "absolute",
                                        "start_index": 1
                                    }}
                                }}
                            ]
                        }}
                    ],
                    "tags": []
                    }}'''},
                    'SONIC-SINGLE-LEAF': {'name': 'SONIC-SINGLE-LEAF',
                                          'data': f'''{{
                    "access_switches": [],
                    "description": "SONIC-SINGLE-LEAF",
                    "display_name": "SONIC-SINGLE-LEAF",
                    "fabric_connectivity_design": "l3clos",
                    "generic_systems": [
                        {{
                            "asn_domain": "disabled",
                            "count": 1,
                            "label": "Server1",
                            "links": [
                                {{
                                    "attachment_type": "singleAttached",
                                    "label": "server-1-link-1",
                                    "lag_mode": null,
                                    "leaf_peer": null,
                                    "link_per_switch_count": 1,
                                    "link_speed": {{
                                        "unit": "G",
                                        "value": 10
                                    }},
                                    "tags": [
                                        "single-leaf-server-link-1"
                                    ],
                                    "target_switch_label": "SONIC-SINGLE-LEAF"
                                }}
                            ],
                            "logical_device": "AOS-1x10-1",
                            "loopback": "disabled",
                            "management_level": "unmanaged",
                            "port_channel_id_max": 0,
                            "port_channel_id_min": 0
                        }},
                        {{
                            "asn_domain": "disabled",
                            "count": 1,
                            "label": "Server2",
                            "links": [
                                {{
                                    "attachment_type": "singleAttached",
                                    "label": "server-2-link-1",
                                    "lag_mode": null,
                                    "leaf_peer": null,
                                    "link_per_switch_count": 1,
                                    "link_speed": {{
                                        "unit": "G",
                                        "value": 10
                                    }},
                                    "tags": [
                                        "single-leaf-server-link-2"
                                    ],
                                    "target_switch_label": "SONIC-SINGLE-LEAF"
                                }}
                            ],
                            "logical_device": "AOS-1x10-1",
                            "loopback": "disabled",
                            "management_level": "unmanaged",
                            "port_channel_id_max": 0,
                            "port_channel_id_min": 0
                        }},
                        {{
                            "asn_domain": "disabled",
                            "count": 1,
                            "label": "Server3",
                            "links": [
                                {{
                                    "attachment_type": "singleAttached",
                                    "label": "server-3-link-1",
                                    "lag_mode": null,
                                    "leaf_peer": null,
                                    "link_per_switch_count": 1,
                                    "link_speed": {{
                                        "unit": "G",
                                        "value": 10
                                    }},
                                    "tags": [
                                        "single-leaf-server-link-3"
                                    ],
                                    "target_switch_label": "SONIC-SINGLE-LEAF"
                                }}
                            ],
                            "logical_device": "AOS-1x10-1",
                            "loopback": "disabled",
                            "management_level": "unmanaged",
                            "port_channel_id_max": 0,
                            "port_channel_id_min": 0
                        }}
                    ],
                    "id": "SONIC-SINGLE-LEAF",
                    "last_modified_at": null,
                    "leafs": [
                        {{
                            "label": "SONIC-SINGLE-LEAF",
                            "leaf_leaf_l3_link_count": 0,
                            "leaf_leaf_l3_link_port_channel_id": 0,
                            "leaf_leaf_l3_link_speed": null,
                            "leaf_leaf_link_count": 0,
                            "leaf_leaf_link_port_channel_id": 0,
                            "leaf_leaf_link_speed": null,
                            "link_per_spine_count": 1,
                            "link_per_spine_speed": {{
                                "unit": "G",
                                "value": 10
                            }},
                            "logical_device": "SONIC-12x10-Leaf",
                            "redundancy_protocol": null,
                            "tags": [
                                "single-leaf"
                            ]
                        }}
                    ],
                    "logical_devices": [
                        {{
                            "display_name": "SONIC-12x10-Leaf",
                            "href": "#/design/logical-devices/SONIC-12x10-Leaf",
                            "id": "SONIC-12x10-Leaf",
                            "panels": [
                                {{
                                    "panel_layout": {{
                                        "column_count": 12,
                                        "row_count": 1
                                    }},
                                    "port_groups": [
                                        {{
                                            "count": 4,
                                            "roles": [
                                                "spine"
                                            ],
                                            "speed": {{
                                                "unit": "G",
                                                "value": 10
                                            }}
                                        }},
                                        {{
                                            "count": 6,
                                            "roles": [
                                                "generic"
                                            ],
                                            "speed": {{
                                                "unit": "G",
                                                "value": 10
                                            }}
                                        }},
                                        {{
                                            "count": 2,
                                            "roles": [
                                                "peer"
                                            ],
                                            "speed": {{
                                                "unit": "G",
                                                "value": 10
                                            }}
                                        }}
                                    ],
                                    "port_indexing": {{
                                        "order": "T-B, L-R",
                                        "schema": "absolute",
                                        "start_index": 1
                                    }}
                                }}
                            ]
                        }},
                        {{
                            "display_name": "AOS-1x10-1",
                            "href": "#/design/logical-devices/AOS-1x10-1",
                            "id": "AOS-1x10-1",
                            "panels": [
                                {{
                                    "panel_layout": {{
                                        "column_count": 1,
                                        "row_count": 1
                                    }},
                                    "port_groups": [
                                        {{
                                            "count": 1,
                                            "roles": [
                                                "leaf",
                                                "access"
                                            ],
                                            "speed": {{
                                                "unit": "G",
                                                "value": 10
                                            }}
                                        }}
                                    ],
                                    "port_indexing": {{
                                        "order": "T-B, L-R",
                                        "schema": "absolute",
                                        "start_index": 1
                                    }}
                                }}
                            ]
                        }},
                        {{
                            "display_name": "SONIC-12x10-Leaf",
                            "href": "#/design/logical-devices/SONIC-12x10-Leaf",
                            "id": "SONIC-12x10-Leaf",
                            "panels": [
                                {{
                                    "panel_layout": {{
                                        "column_count": 12,
                                        "row_count": 1
                                    }},
                                    "port_groups": [
                                        {{
                                            "count": 4,
                                            "roles": [
                                                "spine"
                                            ],
                                            "speed": {{
                                                "unit": "G",
                                                "value": 10
                                            }}
                                        }},
                                        {{
                                            "count": 6,
                                            "roles": [
                                                "generic"
                                            ],
                                            "speed": {{
                                                "unit": "G",
                                                "value": 10
                                            }}
                                        }},
                                        {{
                                            "count": 2,
                                            "roles": [
                                                "peer"
                                            ],
                                            "speed": {{
                                                "unit": "G",
                                                "value": 10
                                            }}
                                        }}
                                    ],
                                    "port_indexing": {{
                                        "order": "T-B, L-R",
                                        "schema": "absolute",
                                        "start_index": 1
                                    }}
                                }}
                            ]
                        }},
                        {{
                            "display_name": "AOS-1x10-1",
                            "href": "#/design/logical-devices/AOS-1x10-1",
                            "id": "AOS-1x10-1",
                            "panels": [
                                {{
                                    "panel_layout": {{
                                        "column_count": 1,
                                        "row_count": 1
                                    }},
                                    "port_groups": [
                                        {{
                                            "count": 1,
                                            "roles": [
                                                "leaf",
                                                "access"
                                            ],
                                            "speed": {{
                                                "unit": "G",
                                                "value": 10
                                            }}
                                        }}
                                    ],
                                    "port_indexing": {{
                                        "order": "T-B, L-R",
                                        "schema": "absolute",
                                        "start_index": 1
                                    }}
                                }}
                            ]
                        }},
                        {{
                            "display_name": "SONIC-12x10-Leaf",
                            "href": "#/design/logical-devices/SONIC-12x10-Leaf",
                            "id": "SONIC-12x10-Leaf",
                            "panels": [
                                {{
                                    "panel_layout": {{
                                        "column_count": 12,
                                        "row_count": 1
                                    }},
                                    "port_groups": [
                                        {{
                                            "count": 4,
                                            "roles": [
                                                "spine"
                                            ],
                                            "speed": {{
                                                "unit": "G",
                                                "value": 10
                                            }}
                                        }},
                                        {{
                                            "count": 6,
                                            "roles": [
                                                "generic"
                                            ],
                                            "speed": {{
                                                "unit": "G",
                                                "value": 10
                                            }}
                                        }},
                                        {{
                                            "count": 2,
                                            "roles": [
                                                "peer"
                                            ],
                                            "speed": {{
                                                "unit": "G",
                                                "value": 10
                                            }}
                                        }}
                                    ],
                                    "port_indexing": {{
                                        "order": "T-B, L-R",
                                        "schema": "absolute",
                                        "start_index": 1
                                    }}
                                }}
                            ]
                        }},
                        {{
                            "display_name": "AOS-1x10-1",
                            "href": "#/design/logical-devices/AOS-1x10-1",
                            "id": "AOS-1x10-1",
                            "panels": [
                                {{
                                    "panel_layout": {{
                                        "column_count": 1,
                                        "row_count": 1
                                    }},
                                    "port_groups": [
                                        {{
                                            "count": 1,
                                            "roles": [
                                                "leaf",
                                                "access"
                                            ],
                                            "speed": {{
                                                "unit": "G",
                                                "value": 10
                                            }}
                                        }}
                                    ],
                                    "port_indexing": {{
                                        "order": "T-B, L-R",
                                        "schema": "absolute",
                                        "start_index": 1
                                    }}
                                }}
                            ]
                        }},
                        {{
                            "display_name": "SONIC-12x10-Leaf",
                            "href": "#/design/logical-devices/SONIC-12x10-Leaf",
                            "id": "SONIC-12x10-Leaf",
                            "panels": [
                                {{
                                    "panel_layout": {{
                                        "column_count": 12,
                                        "row_count": 1
                                    }},
                                    "port_groups": [
                                        {{
                                            "count": 4,
                                            "roles": [
                                                "spine"
                                            ],
                                            "speed": {{
                                                "unit": "G",
                                                "value": 10
                                            }}
                                        }},
                                        {{
                                            "count": 6,
                                            "roles": [
                                                "generic"
                                            ],
                                            "speed": {{
                                                "unit": "G",
                                                "value": 10
                                            }}
                                        }},
                                        {{
                                            "count": 2,
                                            "roles": [
                                                "peer"
                                            ],
                                            "speed": {{
                                                "unit": "G",
                                                "value": 10
                                            }}
                                        }}
                                    ],
                                    "port_indexing": {{
                                        "order": "T-B, L-R",
                                        "schema": "absolute",
                                        "start_index": 1
                                    }}
                                }}
                            ]
                        }},
                        {{
                            "display_name": "AOS-1x10-1",
                            "href": "#/design/logical-devices/AOS-1x10-1",
                            "id": "AOS-1x10-1",
                            "panels": [
                                {{
                                    "panel_layout": {{
                                        "column_count": 1,
                                        "row_count": 1
                                    }},
                                    "port_groups": [
                                        {{
                                            "count": 1,
                                            "roles": [
                                                "leaf",
                                                "access"
                                            ],
                                            "speed": {{
                                                "unit": "G",
                                                "value": 10
                                            }}
                                        }}
                                    ],
                                    "port_indexing": {{
                                        "order": "T-B, L-R",
                                        "schema": "absolute",
                                        "start_index": 1
                                    }}
                                }}
                            ]
                        }},
                        {{
                            "display_name": "SONIC-12x10-Leaf",
                            "href": "#/design/logical-devices/SONIC-12x10-Leaf",
                            "id": "SONIC-12x10-Leaf",
                            "panels": [
                                {{
                                    "panel_layout": {{
                                        "column_count": 12,
                                        "row_count": 1
                                    }},
                                    "port_groups": [
                                        {{
                                            "count": 4,
                                            "roles": [
                                                "spine"
                                            ],
                                            "speed": {{
                                                "unit": "G",
                                                "value": 10
                                            }}
                                        }},
                                        {{
                                            "count": 6,
                                            "roles": [
                                                "generic"
                                            ],
                                            "speed": {{
                                                "unit": "G",
                                                "value": 10
                                            }}
                                        }},
                                        {{
                                            "count": 2,
                                            "roles": [
                                                "peer"
                                            ],
                                            "speed": {{
                                                "unit": "G",
                                                "value": 10
                                            }}
                                        }}
                                    ],
                                    "port_indexing": {{
                                        "order": "T-B, L-R",
                                        "schema": "absolute",
                                        "start_index": 1
                                    }}
                                }}
                            ]
                        }},
                        {{
                            "display_name": "AOS-1x10-1",
                            "href": "#/design/logical-devices/AOS-1x10-1",
                            "id": "AOS-1x10-1",
                            "panels": [
                                {{
                                    "panel_layout": {{
                                        "column_count": 1,
                                        "row_count": 1
                                    }},
                                    "port_groups": [
                                        {{
                                            "count": 1,
                                            "roles": [
                                                "leaf",
                                                "access"
                                            ],
                                            "speed": {{
                                                "unit": "G",
                                                "value": 10
                                            }}
                                        }}
                                    ],
                                    "port_indexing": {{
                                        "order": "T-B, L-R",
                                        "schema": "absolute",
                                        "start_index": 1
                                    }}
                                }}
                            ]
                        }},
                        {{
                            "display_name": "SONIC-12x10-Leaf",
                            "href": "#/design/logical-devices/SONIC-12x10-Leaf",
                            "id": "SONIC-12x10-Leaf",
                            "panels": [
                                {{
                                    "panel_layout": {{
                                        "column_count": 12,
                                        "row_count": 1
                                    }},
                                    "port_groups": [
                                        {{
                                            "count": 4,
                                            "roles": [
                                                "spine"
                                            ],
                                            "speed": {{
                                                "unit": "G",
                                                "value": 10
                                            }}
                                        }},
                                        {{
                                            "count": 6,
                                            "roles": [
                                                "generic"
                                            ],
                                            "speed": {{
                                                "unit": "G",
                                                "value": 10
                                            }}
                                        }},
                                        {{
                                            "count": 2,
                                            "roles": [
                                                "peer"
                                            ],
                                            "speed": {{
                                                "unit": "G",
                                                "value": 10
                                            }}
                                        }}
                                    ],
                                    "port_indexing": {{
                                        "order": "T-B, L-R",
                                        "schema": "absolute",
                                        "start_index": 1
                                    }}
                                }}
                            ]
                        }},
                        {{
                            "display_name": "AOS-1x10-1",
                            "href": "#/design/logical-devices/AOS-1x10-1",
                            "id": "AOS-1x10-1",
                            "panels": [
                                {{
                                    "panel_layout": {{
                                        "column_count": 1,
                                        "row_count": 1
                                    }},
                                    "port_groups": [
                                        {{
                                            "count": 1,
                                            "roles": [
                                                "leaf",
                                                "access"
                                            ],
                                            "speed": {{
                                                "unit": "G",
                                                "value": 10
                                            }}
                                        }}
                                    ],
                                    "port_indexing": {{
                                        "order": "T-B, L-R",
                                        "schema": "absolute",
                                        "start_index": 1
                                    }}
                                }}
                            ]
                        }},
                        {{
                            "display_name": "SONIC-12x10-Leaf",
                            "href": "#/design/logical-devices/SONIC-12x10-Leaf",
                            "id": "SONIC-12x10-Leaf",
                            "panels": [
                                {{
                                    "panel_layout": {{
                                        "column_count": 12,
                                        "row_count": 1
                                    }},
                                    "port_groups": [
                                        {{
                                            "count": 4,
                                            "roles": [
                                                "spine"
                                            ],
                                            "speed": {{
                                                "unit": "G",
                                                "value": 10
                                            }}
                                        }},
                                        {{
                                            "count": 6,
                                            "roles": [
                                                "generic"
                                            ],
                                            "speed": {{
                                                "unit": "G",
                                                "value": 10
                                            }}
                                        }},
                                        {{
                                            "count": 2,
                                            "roles": [
                                                "peer"
                                            ],
                                            "speed": {{
                                                "unit": "G",
                                                "value": 10
                                            }}
                                        }}
                                    ],
                                    "port_indexing": {{
                                        "order": "T-B, L-R",
                                        "schema": "absolute",
                                        "start_index": 1
                                    }}
                                }}
                            ]
                        }},
                        {{
                            "display_name": "AOS-1x10-1",
                            "href": "#/design/logical-devices/AOS-1x10-1",
                            "id": "AOS-1x10-1",
                            "panels": [
                                {{
                                    "panel_layout": {{
                                        "column_count": 1,
                                        "row_count": 1
                                    }},
                                    "port_groups": [
                                        {{
                                            "count": 1,
                                            "roles": [
                                                "leaf",
                                                "access"
                                            ],
                                            "speed": {{
                                                "unit": "G",
                                                "value": 10
                                            }}
                                        }}
                                    ],
                                    "port_indexing": {{
                                        "order": "T-B, L-R",
                                        "schema": "absolute",
                                        "start_index": 1
                                    }}
                                }}
                            ]
                        }},
                        {{
                            "display_name": "SONIC-12x10-Leaf",
                            "href": "#/design/logical-devices/SONIC-12x10-Leaf",
                            "id": "SONIC-12x10-Leaf",
                            "panels": [
                                {{
                                    "panel_layout": {{
                                        "column_count": 12,
                                        "row_count": 1
                                    }},
                                    "port_groups": [
                                        {{
                                            "count": 4,
                                            "roles": [
                                                "spine"
                                            ],
                                            "speed": {{
                                                "unit": "G",
                                                "value": 10
                                            }}
                                        }},
                                        {{
                                            "count": 6,
                                            "roles": [
                                                "generic"
                                            ],
                                            "speed": {{
                                                "unit": "G",
                                                "value": 10
                                            }}
                                        }},
                                        {{
                                            "count": 2,
                                            "roles": [
                                                "peer"
                                            ],
                                            "speed": {{
                                                "unit": "G",
                                                "value": 10
                                            }}
                                        }}
                                    ],
                                    "port_indexing": {{
                                        "order": "T-B, L-R",
                                        "schema": "absolute",
                                        "start_index": 1
                                    }}
                                }}
                            ]
                        }},
                        {{
                            "display_name": "AOS-1x10-1",
                            "href": "#/design/logical-devices/AOS-1x10-1",
                            "id": "AOS-1x10-1",
                            "panels": [
                                {{
                                    "panel_layout": {{
                                        "column_count": 1,
                                        "row_count": 1
                                    }},
                                    "port_groups": [
                                        {{
                                            "count": 1,
                                            "roles": [
                                                "leaf",
                                                "access"
                                            ],
                                            "speed": {{
                                                "unit": "G",
                                                "value": 10
                                            }}
                                        }}
                                    ],
                                    "port_indexing": {{
                                        "order": "T-B, L-R",
                                        "schema": "absolute",
                                        "start_index": 1
                                    }}
                                }}
                            ]
                        }},
                        {{
                            "display_name": "SONIC-12x10-Leaf",
                            "href": "#/design/logical-devices/SONIC-12x10-Leaf",
                            "id": "SONIC-12x10-Leaf",
                            "panels": [
                                {{
                                    "panel_layout": {{
                                        "column_count": 12,
                                        "row_count": 1
                                    }},
                                    "port_groups": [
                                        {{
                                            "count": 4,
                                            "roles": [
                                                "spine"
                                            ],
                                            "speed": {{
                                                "unit": "G",
                                                "value": 10
                                            }}
                                        }},
                                        {{
                                            "count": 6,
                                            "roles": [
                                                "generic"
                                            ],
                                            "speed": {{
                                                "unit": "G",
                                                "value": 10
                                            }}
                                        }},
                                        {{
                                            "count": 2,
                                            "roles": [
                                                "peer"
                                            ],
                                            "speed": {{
                                                "unit": "G",
                                                "value": 10
                                            }}
                                        }}
                                    ],
                                    "port_indexing": {{
                                        "order": "T-B, L-R",
                                        "schema": "absolute",
                                        "start_index": 1
                                    }}
                                }}
                            ]
                        }},
                        {{
                            "display_name": "AOS-1x10-1",
                            "href": "#/design/logical-devices/AOS-1x10-1",
                            "id": "AOS-1x10-1",
                            "panels": [
                                {{
                                    "panel_layout": {{
                                        "column_count": 1,
                                        "row_count": 1
                                    }},
                                    "port_groups": [
                                        {{
                                            "count": 1,
                                            "roles": [
                                                "leaf",
                                                "access"
                                            ],
                                            "speed": {{
                                                "unit": "G",
                                                "value": 10
                                            }}
                                        }}
                                    ],
                                    "port_indexing": {{
                                        "order": "T-B, L-R",
                                        "schema": "absolute",
                                        "start_index": 1
                                    }}
                                }}
                            ]
                        }},
                        {{
                            "display_name": "SONIC-12x10-Leaf",
                            "href": "#/design/logical-devices/SONIC-12x10-Leaf",
                            "id": "SONIC-12x10-Leaf",
                            "panels": [
                                {{
                                    "panel_layout": {{
                                        "column_count": 12,
                                        "row_count": 1
                                    }},
                                    "port_groups": [
                                        {{
                                            "count": 4,
                                            "roles": [
                                                "spine"
                                            ],
                                            "speed": {{
                                                "unit": "G",
                                                "value": 10
                                            }}
                                        }},
                                        {{
                                            "count": 6,
                                            "roles": [
                                                "generic"
                                            ],
                                            "speed": {{
                                                "unit": "G",
                                                "value": 10
                                            }}
                                        }},
                                        {{
                                            "count": 2,
                                            "roles": [
                                                "peer"
                                            ],
                                            "speed": {{
                                                "unit": "G",
                                                "value": 10
                                            }}
                                        }}
                                    ],
                                    "port_indexing": {{
                                        "order": "T-B, L-R",
                                        "schema": "absolute",
                                        "start_index": 1
                                    }}
                                }}
                            ]
                        }},
                        {{
                            "display_name": "AOS-1x10-1",
                            "href": "#/design/logical-devices/AOS-1x10-1",
                            "id": "AOS-1x10-1",
                            "panels": [
                                {{
                                    "panel_layout": {{
                                        "column_count": 1,
                                        "row_count": 1
                                    }},
                                    "port_groups": [
                                        {{
                                            "count": 1,
                                            "roles": [
                                                "leaf",
                                                "access"
                                            ],
                                            "speed": {{
                                                "unit": "G",
                                                "value": 10
                                            }}
                                        }}
                                    ],
                                    "port_indexing": {{
                                        "order": "T-B, L-R",
                                        "schema": "absolute",
                                        "start_index": 1
                                    }}
                                }}
                            ]
                        }},
                        {{
                            "display_name": "SONIC-12x10-Leaf",
                            "href": "#/design/logical-devices/SONIC-12x10-Leaf",
                            "id": "SONIC-12x10-Leaf",
                            "panels": [
                                {{
                                    "panel_layout": {{
                                        "column_count": 12,
                                        "row_count": 1
                                    }},
                                    "port_groups": [
                                        {{
                                            "count": 4,
                                            "roles": [
                                                "spine"
                                            ],
                                            "speed": {{
                                                "unit": "G",
                                                "value": 10
                                            }}
                                        }},
                                        {{
                                            "count": 6,
                                            "roles": [
                                                "generic"
                                            ],
                                            "speed": {{
                                                "unit": "G",
                                                "value": 10
                                            }}
                                        }},
                                        {{
                                            "count": 2,
                                            "roles": [
                                                "peer"
                                            ],
                                            "speed": {{
                                                "unit": "G",
                                                "value": 10
                                            }}
                                        }}
                                    ],
                                    "port_indexing": {{
                                        "order": "T-B, L-R",
                                        "schema": "absolute",
                                        "start_index": 1
                                    }}
                                }}
                            ]
                        }},
                        {{
                            "display_name": "AOS-1x10-1",
                            "href": "#/design/logical-devices/AOS-1x10-1",
                            "id": "AOS-1x10-1",
                            "panels": [
                                {{
                                    "panel_layout": {{
                                        "column_count": 1,
                                        "row_count": 1
                                    }},
                                    "port_groups": [
                                        {{
                                            "count": 1,
                                            "roles": [
                                                "leaf",
                                                "access"
                                            ],
                                            "speed": {{
                                                "unit": "G",
                                                "value": 10
                                            }}
                                        }}
                                    ],
                                    "port_indexing": {{
                                        "order": "T-B, L-R",
                                        "schema": "absolute",
                                        "start_index": 1
                                    }}
                                }}
                            ]
                        }},
                        {{
                            "display_name": "SONIC-12x10-Leaf",
                            "href": "#/design/logical-devices/SONIC-12x10-Leaf",
                            "id": "SONIC-12x10-Leaf",
                            "panels": [
                                {{
                                    "panel_layout": {{
                                        "column_count": 12,
                                        "row_count": 1
                                    }},
                                    "port_groups": [
                                        {{
                                            "count": 4,
                                            "roles": [
                                                "spine"
                                            ],
                                            "speed": {{
                                                "unit": "G",
                                                "value": 10
                                            }}
                                        }},
                                        {{
                                            "count": 6,
                                            "roles": [
                                                "generic"
                                            ],
                                            "speed": {{
                                                "unit": "G",
                                                "value": 10
                                            }}
                                        }},
                                        {{
                                            "count": 2,
                                            "roles": [
                                                "peer"
                                            ],
                                            "speed": {{
                                                "unit": "G",
                                                "value": 10
                                            }}
                                        }}
                                    ],
                                    "port_indexing": {{
                                        "order": "T-B, L-R",
                                        "schema": "absolute",
                                        "start_index": 1
                                    }}
                                }}
                            ]
                        }},
                        {{
                            "display_name": "AOS-1x10-1",
                            "href": "#/design/logical-devices/AOS-1x10-1",
                            "id": "AOS-1x10-1",
                            "panels": [
                                {{
                                    "panel_layout": {{
                                        "column_count": 1,
                                        "row_count": 1
                                    }},
                                    "port_groups": [
                                        {{
                                            "count": 1,
                                            "roles": [
                                                "leaf",
                                                "access"
                                            ],
                                            "speed": {{
                                                "unit": "G",
                                                "value": 10
                                            }}
                                        }}
                                    ],
                                    "port_indexing": {{
                                        "order": "T-B, L-R",
                                        "schema": "absolute",
                                        "start_index": 1
                                    }}
                                }}
                            ]
                        }},
                        {{
                            "display_name": "SONIC-12x10-Leaf",
                            "href": "#/design/logical-devices/SONIC-12x10-Leaf",
                            "id": "SONIC-12x10-Leaf",
                            "panels": [
                                {{
                                    "panel_layout": {{
                                        "column_count": 12,
                                        "row_count": 1
                                    }},
                                    "port_groups": [
                                        {{
                                            "count": 4,
                                            "roles": [
                                                "spine"
                                            ],
                                            "speed": {{
                                                "unit": "G",
                                                "value": 10
                                            }}
                                        }},
                                        {{
                                            "count": 6,
                                            "roles": [
                                                "generic"
                                            ],
                                            "speed": {{
                                                "unit": "G",
                                                "value": 10
                                            }}
                                        }},
                                        {{
                                            "count": 2,
                                            "roles": [
                                                "peer"
                                            ],
                                            "speed": {{
                                                "unit": "G",
                                                "value": 10
                                            }}
                                        }}
                                    ],
                                    "port_indexing": {{
                                        "order": "T-B, L-R",
                                        "schema": "absolute",
                                        "start_index": 1
                                    }}
                                }}
                            ]
                        }},
                        {{
                            "display_name": "AOS-1x10-1",
                            "href": "#/design/logical-devices/AOS-1x10-1",
                            "id": "AOS-1x10-1",
                            "panels": [
                                {{
                                    "panel_layout": {{
                                        "column_count": 1,
                                        "row_count": 1
                                    }},
                                    "port_groups": [
                                        {{
                                            "count": 1,
                                            "roles": [
                                                "leaf",
                                                "access"
                                            ],
                                            "speed": {{
                                                "unit": "G",
                                                "value": 10
                                            }}
                                        }}
                                    ],
                                    "port_indexing": {{
                                        "order": "T-B, L-R",
                                        "schema": "absolute",
                                        "start_index": 1
                                    }}
                                }}
                            ]
                        }},
                        {{
                            "display_name": "SONIC-12x10-Leaf",
                            "href": "#/design/logical-devices/SONIC-12x10-Leaf",
                            "id": "SONIC-12x10-Leaf",
                            "panels": [
                                {{
                                    "panel_layout": {{
                                        "column_count": 12,
                                        "row_count": 1
                                    }},
                                    "port_groups": [
                                        {{
                                            "count": 4,
                                            "roles": [
                                                "spine"
                                            ],
                                            "speed": {{
                                                "unit": "G",
                                                "value": 10
                                            }}
                                        }},
                                        {{
                                            "count": 6,
                                            "roles": [
                                                "generic"
                                            ],
                                            "speed": {{
                                                "unit": "G",
                                                "value": 10
                                            }}
                                        }},
                                        {{
                                            "count": 2,
                                            "roles": [
                                                "peer"
                                            ],
                                            "speed": {{
                                                "unit": "G",
                                                "value": 10
                                            }}
                                        }}
                                    ],
                                    "port_indexing": {{
                                        "order": "T-B, L-R",
                                        "schema": "absolute",
                                        "start_index": 1
                                    }}
                                }}
                            ]
                        }},
                        {{
                            "display_name": "AOS-1x10-1",
                            "href": "#/design/logical-devices/AOS-1x10-1",
                            "id": "AOS-1x10-1",
                            "panels": [
                                {{
                                    "panel_layout": {{
                                        "column_count": 1,
                                        "row_count": 1
                                    }},
                                    "port_groups": [
                                        {{
                                            "count": 1,
                                            "roles": [
                                                "leaf",
                                                "access"
                                            ],
                                            "speed": {{
                                                "unit": "G",
                                                "value": 10
                                            }}
                                        }}
                                    ],
                                    "port_indexing": {{
                                        "order": "T-B, L-R",
                                        "schema": "absolute",
                                        "start_index": 1
                                    }}
                                }}
                            ]
                        }},
                        {{
                            "display_name": "SONIC-12x10-Leaf",
                            "href": "#/design/logical-devices/SONIC-12x10-Leaf",
                            "id": "SONIC-12x10-Leaf",
                            "panels": [
                                {{
                                    "panel_layout": {{
                                        "column_count": 12,
                                        "row_count": 1
                                    }},
                                    "port_groups": [
                                        {{
                                            "count": 4,
                                            "roles": [
                                                "spine"
                                            ],
                                            "speed": {{
                                                "unit": "G",
                                                "value": 10
                                            }}
                                        }},
                                        {{
                                            "count": 6,
                                            "roles": [
                                                "generic"
                                            ],
                                            "speed": {{
                                                "unit": "G",
                                                "value": 10
                                            }}
                                        }},
                                        {{
                                            "count": 2,
                                            "roles": [
                                                "peer"
                                            ],
                                            "speed": {{
                                                "unit": "G",
                                                "value": 10
                                            }}
                                        }}
                                    ],
                                    "port_indexing": {{
                                        "order": "T-B, L-R",
                                        "schema": "absolute",
                                        "start_index": 1
                                    }}
                                }}
                            ]
                        }},
                        {{
                            "display_name": "AOS-1x10-1",
                            "href": "#/design/logical-devices/AOS-1x10-1",
                            "id": "AOS-1x10-1",
                            "panels": [
                                {{
                                    "panel_layout": {{
                                        "column_count": 1,
                                        "row_count": 1
                                    }},
                                    "port_groups": [
                                        {{
                                            "count": 1,
                                            "roles": [
                                                "leaf",
                                                "access"
                                            ],
                                            "speed": {{
                                                "unit": "G",
                                                "value": 10
                                            }}
                                        }}
                                    ],
                                    "port_indexing": {{
                                        "order": "T-B, L-R",
                                        "schema": "absolute",
                                        "start_index": 1
                                    }}
                                }}
                            ]
                        }},
                        {{
                            "display_name": "SONIC-12x10-Leaf",
                            "href": "#/design/logical-devices/SONIC-12x10-Leaf",
                            "id": "SONIC-12x10-Leaf",
                            "panels": [
                                {{
                                    "panel_layout": {{
                                        "column_count": 12,
                                        "row_count": 1
                                    }},
                                    "port_groups": [
                                        {{
                                            "count": 4,
                                            "roles": [
                                                "spine"
                                            ],
                                            "speed": {{
                                                "unit": "G",
                                                "value": 10
                                            }}
                                        }},
                                        {{
                                            "count": 6,
                                            "roles": [
                                                "generic"
                                            ],
                                            "speed": {{
                                                "unit": "G",
                                                "value": 10
                                            }}
                                        }},
                                        {{
                                            "count": 2,
                                            "roles": [
                                                "peer"
                                            ],
                                            "speed": {{
                                                "unit": "G",
                                                "value": 10
                                            }}
                                        }}
                                    ],
                                    "port_indexing": {{
                                        "order": "T-B, L-R",
                                        "schema": "absolute",
                                        "start_index": 1
                                    }}
                                }}
                            ]
                        }},
                        {{
                            "display_name": "AOS-1x10-1",
                            "href": "#/design/logical-devices/AOS-1x10-1",
                            "id": "AOS-1x10-1",
                            "panels": [
                                {{
                                    "panel_layout": {{
                                        "column_count": 1,
                                        "row_count": 1
                                    }},
                                    "port_groups": [
                                        {{
                                            "count": 1,
                                            "roles": [
                                                "leaf",
                                                "access"
                                            ],
                                            "speed": {{
                                                "unit": "G",
                                                "value": 10
                                            }}
                                        }}
                                    ],
                                    "port_indexing": {{
                                        "order": "T-B, L-R",
                                        "schema": "absolute",
                                        "start_index": 1
                                    }}
                                }}
                            ]
                        }},
                        {{
                            "display_name": "SONIC-12x10-Leaf",
                            "href": "#/design/logical-devices/SONIC-12x10-Leaf",
                            "id": "SONIC-12x10-Leaf",
                            "panels": [
                                {{
                                    "panel_layout": {{
                                        "column_count": 12,
                                        "row_count": 1
                                    }},
                                    "port_groups": [
                                        {{
                                            "count": 4,
                                            "roles": [
                                                "spine"
                                            ],
                                            "speed": {{
                                                "unit": "G",
                                                "value": 10
                                            }}
                                        }},
                                        {{
                                            "count": 6,
                                            "roles": [
                                                "generic"
                                            ],
                                            "speed": {{
                                                "unit": "G",
                                                "value": 10
                                            }}
                                        }},
                                        {{
                                            "count": 2,
                                            "roles": [
                                                "peer"
                                            ],
                                            "speed": {{
                                                "unit": "G",
                                                "value": 10
                                            }}
                                        }}
                                    ],
                                    "port_indexing": {{
                                        "order": "T-B, L-R",
                                        "schema": "absolute",
                                        "start_index": 1
                                    }}
                                }}
                            ]
                        }},
                        {{
                            "display_name": "SONIC-12x10-Leaf",
                            "href": "#/design/logical-devices/SONIC-12x10-Leaf",
                            "id": "SONIC-12x10-Leaf",
                            "panels": [
                                {{
                                    "panel_layout": {{
                                        "column_count": 12,
                                        "row_count": 1
                                    }},
                                    "port_groups": [
                                        {{
                                            "count": 4,
                                            "roles": [
                                                "spine"
                                            ],
                                            "speed": {{
                                                "unit": "G",
                                                "value": 10
                                            }}
                                        }},
                                        {{
                                            "count": 6,
                                            "roles": [
                                                "generic"
                                            ],
                                            "speed": {{
                                                "unit": "G",
                                                "value": 10
                                            }}
                                        }},
                                        {{
                                            "count": 2,
                                            "roles": [
                                                "peer"
                                            ],
                                            "speed": {{
                                                "unit": "G",
                                                "value": 10
                                            }}
                                        }}
                                    ],
                                    "port_indexing": {{
                                        "order": "T-B, L-R",
                                        "schema": "absolute",
                                        "start_index": 1
                                    }}
                                }}
                            ]
                        }},
                        {{
                            "display_name": "SONIC-12x10-Leaf",
                            "href": "#/design/logical-devices/SONIC-12x10-Leaf",
                            "id": "SONIC-12x10-Leaf",
                            "panels": [
                                {{
                                    "panel_layout": {{
                                        "column_count": 12,
                                        "row_count": 1
                                    }},
                                    "port_groups": [
                                        {{
                                            "count": 4,
                                            "roles": [
                                                "spine"
                                            ],
                                            "speed": {{
                                                "unit": "G",
                                                "value": 10
                                            }}
                                        }},
                                        {{
                                            "count": 6,
                                            "roles": [
                                                "generic"
                                            ],
                                            "speed": {{
                                                "unit": "G",
                                                "value": 10
                                            }}
                                        }},
                                        {{
                                            "count": 2,
                                            "roles": [
                                                "peer"
                                            ],
                                            "speed": {{
                                                "unit": "G",
                                                "value": 10
                                            }}
                                        }}
                                    ],
                                    "port_indexing": {{
                                        "order": "T-B, L-R",
                                        "schema": "absolute",
                                        "start_index": 1
                                    }}
                                }}
                            ]
                        }},
                        {{
                            "display_name": "SONIC-12x10-Leaf",
                            "href": "#/design/logical-devices/SONIC-12x10-Leaf",
                            "id": "SONIC-12x10-Leaf",
                            "panels": [
                                {{
                                    "panel_layout": {{
                                        "column_count": 12,
                                        "row_count": 1
                                    }},
                                    "port_groups": [
                                        {{
                                            "count": 4,
                                            "roles": [
                                                "spine"
                                            ],
                                            "speed": {{
                                                "unit": "G",
                                                "value": 10
                                            }}
                                        }},
                                        {{
                                            "count": 6,
                                            "roles": [
                                                "generic"
                                            ],
                                            "speed": {{
                                                "unit": "G",
                                                "value": 10
                                            }}
                                        }},
                                        {{
                                            "count": 2,
                                            "roles": [
                                                "peer"
                                            ],
                                            "speed": {{
                                                "unit": "G",
                                                "value": 10
                                            }}
                                        }}
                                    ],
                                    "port_indexing": {{
                                        "order": "T-B, L-R",
                                        "schema": "absolute",
                                        "start_index": 1
                                    }}
                                }}
                            ]
                        }}
                    ],
                    "tags": []
                    }}'''},
                    'SONIC-MCLAG-LEAF': {'name': 'SONIC-MCLAG-LEAF',
                                          'data': f'''{{
                    "access_switches": [],
                    "description": "SONIC-MCLAG-LEAF",
                    "display_name": "SONIC-MCLAG-LEAF",
                    "fabric_connectivity_design": "l3clos",
                    "generic_systems": [
                        {{
                            "asn_domain": "disabled",
                            "count": 1,
                            "label": "Server1",
                            "links": [
                                {{
                                    "attachment_type": "dualAttached",
                                    "label": "server-1-dual-link",
                                    "lag_mode": "lacp_active",
                                    "link_per_switch_count": 1,
                                    "link_speed": {{
                                        "unit": "G",
                                        "value": 10
                                    }},
                                    "tags": [
                                        "esi-leaf-lacp-server-link-1"
                                    ],
                                    "target_switch_label": "SONIC-MCLAG-LEAF"
                                }}
                            ],
                            "logical_device": "AOS-2x10-1",
                            "loopback": "disabled",
                            "management_level": "unmanaged",
                            "port_channel_id_max": 0,
                            "port_channel_id_min": 0
                        }},
                        {{
                            "asn_domain": "disabled",
                            "count": 1,
                            "label": "Server2",
                            "links": [
                                {{
                                    "attachment_type": "singleAttached",
                                    "label": "server-2-link-1",
                                    "lag_mode": null,
                                    "leaf_peer": "second",
                                    "link_per_switch_count": 1,
                                    "link_speed": {{
                                        "unit": "G",
                                        "value": 10
                                    }},
                                    "tags": [
                                        "esi-leaf-server-link-2"
                                    ],
                                    "target_switch_label": "SONIC-MCLAG-LEAF"
                                }}
                            ],
                            "logical_device": "AOS-1x10-1",
                            "loopback": "disabled",
                            "management_level": "unmanaged",
                            "port_channel_id_max": 0,
                            "port_channel_id_min": 0
                        }}
                    ],
                    "id": "SONIC-MCLAG-LEAF",
                    "last_modified_at": null,
                    "leafs": [
                        {{
                            "label": "SONIC-MCLAG-LEAF",
                            "leaf_leaf_l3_link_count": 0,
                            "leaf_leaf_l3_link_port_channel_id": 0,
                            "leaf_leaf_l3_link_speed": {{
                                "unit": "G",
                                "value": 10
                            }},
                            "leaf_leaf_link_count": 1,
                            "leaf_leaf_link_port_channel_id": 0,
                            "leaf_leaf_link_speed": {{
                                "unit": "G",
                                "value": 10
                            }},
                            "link_per_spine_count": 1,
                            "link_per_spine_speed": {{
                                "unit": "G",
                                "value": 10
                            }},
                            "logical_device": "SONIC-12x10-Leaf",
                            "mlag_vlan_id": 2999,
                            "redundancy_protocol": "mlag",
                            "tags": [
                                "mclag-leaf"
                            ]
                        }}
                    ],
                    "logical_devices": [
                        {{
                            "display_name": "AOS-2x10-1",
                            "href": "#/design/logical-devices/AOS-2x10-1",
                            "id": "AOS-2x10-1",
                            "panels": [
                                {{
                                    "panel_layout": {{
                                        "column_count": 2,
                                        "row_count": 1
                                    }},
                                    "port_groups": [
                                        {{
                                            "count": 2,
                                            "roles": [
                                                "leaf",
                                                "access"
                                            ],
                                            "speed": {{
                                                "unit": "G",
                                                "value": 10
                                            }}
                                        }}
                                    ],
                                    "port_indexing": {{
                                        "order": "T-B, L-R",
                                        "schema": "absolute",
                                        "start_index": 1
                                    }}
                                }}
                            ]
                        }},
                        {{
                            "display_name": "SONIC-12x10-Leaf",
                            "href": "#/design/logical-devices/SONIC-12x10-Leaf",
                            "id": "SONIC-12x10-Leaf",
                            "panels": [
                                {{
                                    "panel_layout": {{
                                        "column_count": 12,
                                        "row_count": 1
                                    }},
                                    "port_groups": [
                                        {{
                                            "count": 4,
                                            "roles": [
                                                "spine"
                                            ],
                                            "speed": {{
                                                "unit": "G",
                                                "value": 10
                                            }}
                                        }},
                                        {{
                                            "count": 6,
                                            "roles": [
                                                "generic"
                                            ],
                                            "speed": {{
                                                "unit": "G",
                                                "value": 10
                                            }}
                                        }},
                                        {{
                                            "count": 2,
                                            "roles": [
                                                "peer"
                                            ],
                                            "speed": {{
                                                "unit": "G",
                                                "value": 10
                                            }}
                                        }}
                                    ],
                                    "port_indexing": {{
                                        "order": "T-B, L-R",
                                        "schema": "absolute",
                                        "start_index": 1
                                    }}
                                }}
                            ]
                        }},
                        {{
                            "display_name": "AOS-1x10-1",
                            "href": "#/design/logical-devices/AOS-1x10-1",
                            "id": "AOS-1x10-1",
                            "panels": [
                                {{
                                    "panel_layout": {{
                                        "column_count": 1,
                                        "row_count": 1
                                    }},
                                    "port_groups": [
                                        {{
                                            "count": 1,
                                            "roles": [
                                                "leaf",
                                                "access"
                                            ],
                                            "speed": {{
                                                "unit": "G",
                                                "value": 10
                                            }}
                                        }}
                                    ],
                                    "port_indexing": {{
                                        "order": "T-B, L-R",
                                        "schema": "absolute",
                                        "start_index": 1
                                    }}
                                }}
                            ]
                        }},
                        {{
                            "display_name": "AOS-2x10-1",
                            "href": "#/design/logical-devices/AOS-2x10-1",
                            "id": "AOS-2x10-1",
                            "panels": [
                                {{
                                    "panel_layout": {{
                                        "column_count": 2,
                                        "row_count": 1
                                    }},
                                    "port_groups": [
                                        {{
                                            "count": 2,
                                            "roles": [
                                                "leaf",
                                                "access"
                                            ],
                                            "speed": {{
                                                "unit": "G",
                                                "value": 10
                                            }}
                                        }}
                                    ],
                                    "port_indexing": {{
                                        "order": "T-B, L-R",
                                        "schema": "absolute",
                                        "start_index": 1
                                    }}
                                }}
                            ]
                        }},
                        {{
                            "display_name": "SONIC-12x10-Leaf",
                            "href": "#/design/logical-devices/SONIC-12x10-Leaf",
                            "id": "SONIC-12x10-Leaf",
                            "panels": [
                                {{
                                    "panel_layout": {{
                                        "column_count": 12,
                                        "row_count": 1
                                    }},
                                    "port_groups": [
                                        {{
                                            "count": 4,
                                            "roles": [
                                                "spine"
                                            ],
                                            "speed": {{
                                                "unit": "G",
                                                "value": 10
                                            }}
                                        }},
                                        {{
                                            "count": 6,
                                            "roles": [
                                                "generic"
                                            ],
                                            "speed": {{
                                                "unit": "G",
                                                "value": 10
                                            }}
                                        }},
                                        {{
                                            "count": 2,
                                            "roles": [
                                                "peer"
                                            ],
                                            "speed": {{
                                                "unit": "G",
                                                "value": 10
                                            }}
                                        }}
                                    ],
                                    "port_indexing": {{
                                        "order": "T-B, L-R",
                                        "schema": "absolute",
                                        "start_index": 1
                                    }}
                                }}
                            ]
                        }},
                        {{
                            "display_name": "AOS-1x10-1",
                            "href": "#/design/logical-devices/AOS-1x10-1",
                            "id": "AOS-1x10-1",
                            "panels": [
                                {{
                                    "panel_layout": {{
                                        "column_count": 1,
                                        "row_count": 1
                                    }},
                                    "port_groups": [
                                        {{
                                            "count": 1,
                                            "roles": [
                                                "leaf",
                                                "access"
                                            ],
                                            "speed": {{
                                                "unit": "G",
                                                "value": 10
                                            }}
                                        }}
                                    ],
                                    "port_indexing": {{
                                        "order": "T-B, L-R",
                                        "schema": "absolute",
                                        "start_index": 1
                                    }}
                                }}
                            ]
                        }},
                        {{
                            "display_name": "AOS-2x10-1",
                            "href": "#/design/logical-devices/AOS-2x10-1",
                            "id": "AOS-2x10-1",
                            "panels": [
                                {{
                                    "panel_layout": {{
                                        "column_count": 2,
                                        "row_count": 1
                                    }},
                                    "port_groups": [
                                        {{
                                            "count": 2,
                                            "roles": [
                                                "leaf",
                                                "access"
                                            ],
                                            "speed": {{
                                                "unit": "G",
                                                "value": 10
                                            }}
                                        }}
                                    ],
                                    "port_indexing": {{
                                        "order": "T-B, L-R",
                                        "schema": "absolute",
                                        "start_index": 1
                                    }}
                                }}
                            ]
                        }},
                        {{
                            "display_name": "SONIC-12x10-Leaf",
                            "href": "#/design/logical-devices/SONIC-12x10-Leaf",
                            "id": "SONIC-12x10-Leaf",
                            "panels": [
                                {{
                                    "panel_layout": {{
                                        "column_count": 12,
                                        "row_count": 1
                                    }},
                                    "port_groups": [
                                        {{
                                            "count": 4,
                                            "roles": [
                                                "spine"
                                            ],
                                            "speed": {{
                                                "unit": "G",
                                                "value": 10
                                            }}
                                        }},
                                        {{
                                            "count": 6,
                                            "roles": [
                                                "generic"
                                            ],
                                            "speed": {{
                                                "unit": "G",
                                                "value": 10
                                            }}
                                        }},
                                        {{
                                            "count": 2,
                                            "roles": [
                                                "peer"
                                            ],
                                            "speed": {{
                                                "unit": "G",
                                                "value": 10
                                            }}
                                        }}
                                    ],
                                    "port_indexing": {{
                                        "order": "T-B, L-R",
                                        "schema": "absolute",
                                        "start_index": 1
                                    }}
                                }}
                            ]
                        }},
                        {{
                            "display_name": "AOS-1x10-1",
                            "href": "#/design/logical-devices/AOS-1x10-1",
                            "id": "AOS-1x10-1",
                            "panels": [
                                {{
                                    "panel_layout": {{
                                        "column_count": 1,
                                        "row_count": 1
                                    }},
                                    "port_groups": [
                                        {{
                                            "count": 1,
                                            "roles": [
                                                "leaf",
                                                "access"
                                            ],
                                            "speed": {{
                                                "unit": "G",
                                                "value": 10
                                            }}
                                        }}
                                    ],
                                    "port_indexing": {{
                                        "order": "T-B, L-R",
                                        "schema": "absolute",
                                        "start_index": 1
                                    }}
                                }}
                            ]
                        }},
                        {{
                            "display_name": "AOS-2x10-1",
                            "href": "#/design/logical-devices/AOS-2x10-1",
                            "id": "AOS-2x10-1",
                            "panels": [
                                {{
                                    "panel_layout": {{
                                        "column_count": 2,
                                        "row_count": 1
                                    }},
                                    "port_groups": [
                                        {{
                                            "count": 2,
                                            "roles": [
                                                "leaf",
                                                "access"
                                            ],
                                            "speed": {{
                                                "unit": "G",
                                                "value": 10
                                            }}
                                        }}
                                    ],
                                    "port_indexing": {{
                                        "order": "T-B, L-R",
                                        "schema": "absolute",
                                        "start_index": 1
                                    }}
                                }}
                            ]
                        }},
                        {{
                            "display_name": "SONIC-12x10-Leaf",
                            "href": "#/design/logical-devices/SONIC-12x10-Leaf",
                            "id": "SONIC-12x10-Leaf",
                            "panels": [
                                {{
                                    "panel_layout": {{
                                        "column_count": 12,
                                        "row_count": 1
                                    }},
                                    "port_groups": [
                                        {{
                                            "count": 4,
                                            "roles": [
                                                "spine"
                                            ],
                                            "speed": {{
                                                "unit": "G",
                                                "value": 10
                                            }}
                                        }},
                                        {{
                                            "count": 6,
                                            "roles": [
                                                "generic"
                                            ],
                                            "speed": {{
                                                "unit": "G",
                                                "value": 10
                                            }}
                                        }},
                                        {{
                                            "count": 2,
                                            "roles": [
                                                "peer"
                                            ],
                                            "speed": {{
                                                "unit": "G",
                                                "value": 10
                                            }}
                                        }}
                                    ],
                                    "port_indexing": {{
                                        "order": "T-B, L-R",
                                        "schema": "absolute",
                                        "start_index": 1
                                    }}
                                }}
                            ]
                        }},
                        {{
                            "display_name": "AOS-1x10-1",
                            "href": "#/design/logical-devices/AOS-1x10-1",
                            "id": "AOS-1x10-1",
                            "panels": [
                                {{
                                    "panel_layout": {{
                                        "column_count": 1,
                                        "row_count": 1
                                    }},
                                    "port_groups": [
                                        {{
                                            "count": 1,
                                            "roles": [
                                                "leaf",
                                                "access"
                                            ],
                                            "speed": {{
                                                "unit": "G",
                                                "value": 10
                                            }}
                                        }}
                                    ],
                                    "port_indexing": {{
                                        "order": "T-B, L-R",
                                        "schema": "absolute",
                                        "start_index": 1
                                    }}
                                }}
                            ]
                        }},
                        {{
                            "display_name": "AOS-2x10-1",
                            "href": "#/design/logical-devices/AOS-2x10-1",
                            "id": "AOS-2x10-1",
                            "panels": [
                                {{
                                    "panel_layout": {{
                                        "column_count": 2,
                                        "row_count": 1
                                    }},
                                    "port_groups": [
                                        {{
                                            "count": 2,
                                            "roles": [
                                                "leaf",
                                                "access"
                                            ],
                                            "speed": {{
                                                "unit": "G",
                                                "value": 10
                                            }}
                                        }}
                                    ],
                                    "port_indexing": {{
                                        "order": "T-B, L-R",
                                        "schema": "absolute",
                                        "start_index": 1
                                    }}
                                }}
                            ]
                        }},
                        {{
                            "display_name": "SONIC-12x10-Leaf",
                            "href": "#/design/logical-devices/SONIC-12x10-Leaf",
                            "id": "SONIC-12x10-Leaf",
                            "panels": [
                                {{
                                    "panel_layout": {{
                                        "column_count": 12,
                                        "row_count": 1
                                    }},
                                    "port_groups": [
                                        {{
                                            "count": 4,
                                            "roles": [
                                                "spine"
                                            ],
                                            "speed": {{
                                                "unit": "G",
                                                "value": 10
                                            }}
                                        }},
                                        {{
                                            "count": 6,
                                            "roles": [
                                                "generic"
                                            ],
                                            "speed": {{
                                                "unit": "G",
                                                "value": 10
                                            }}
                                        }},
                                        {{
                                            "count": 2,
                                            "roles": [
                                                "peer"
                                            ],
                                            "speed": {{
                                                "unit": "G",
                                                "value": 10
                                            }}
                                        }}
                                    ],
                                    "port_indexing": {{
                                        "order": "T-B, L-R",
                                        "schema": "absolute",
                                        "start_index": 1
                                    }}
                                }}
                            ]
                        }},
                        {{
                            "display_name": "AOS-1x10-1",
                            "href": "#/design/logical-devices/AOS-1x10-1",
                            "id": "AOS-1x10-1",
                            "panels": [
                                {{
                                    "panel_layout": {{
                                        "column_count": 1,
                                        "row_count": 1
                                    }},
                                    "port_groups": [
                                        {{
                                            "count": 1,
                                            "roles": [
                                                "leaf",
                                                "access"
                                            ],
                                            "speed": {{
                                                "unit": "G",
                                                "value": 10
                                            }}
                                        }}
                                    ],
                                    "port_indexing": {{
                                        "order": "T-B, L-R",
                                        "schema": "absolute",
                                        "start_index": 1
                                    }}
                                }}
                            ]
                        }},
                        {{
                            "display_name": "AOS-2x10-1",
                            "href": "#/design/logical-devices/AOS-2x10-1",
                            "id": "AOS-2x10-1",
                            "panels": [
                                {{
                                    "panel_layout": {{
                                        "column_count": 2,
                                        "row_count": 1
                                    }},
                                    "port_groups": [
                                        {{
                                            "count": 2,
                                            "roles": [
                                                "leaf",
                                                "access"
                                            ],
                                            "speed": {{
                                                "unit": "G",
                                                "value": 10
                                            }}
                                        }}
                                    ],
                                    "port_indexing": {{
                                        "order": "T-B, L-R",
                                        "schema": "absolute",
                                        "start_index": 1
                                    }}
                                }}
                            ]
                        }},
                        {{
                            "display_name": "SONIC-12x10-Leaf",
                            "href": "#/design/logical-devices/SONIC-12x10-Leaf",
                            "id": "SONIC-12x10-Leaf",
                            "panels": [
                                {{
                                    "panel_layout": {{
                                        "column_count": 12,
                                        "row_count": 1
                                    }},
                                    "port_groups": [
                                        {{
                                            "count": 4,
                                            "roles": [
                                                "spine"
                                            ],
                                            "speed": {{
                                                "unit": "G",
                                                "value": 10
                                            }}
                                        }},
                                        {{
                                            "count": 6,
                                            "roles": [
                                                "generic"
                                            ],
                                            "speed": {{
                                                "unit": "G",
                                                "value": 10
                                            }}
                                        }},
                                        {{
                                            "count": 2,
                                            "roles": [
                                                "peer"
                                            ],
                                            "speed": {{
                                                "unit": "G",
                                                "value": 10
                                            }}
                                        }}
                                    ],
                                    "port_indexing": {{
                                        "order": "T-B, L-R",
                                        "schema": "absolute",
                                        "start_index": 1
                                    }}
                                }}
                            ]
                        }},
                        {{
                            "display_name": "AOS-2x10-1",
                            "href": "#/design/logical-devices/AOS-2x10-1",
                            "id": "AOS-2x10-1",
                            "panels": [
                                {{
                                    "panel_layout": {{
                                        "column_count": 2,
                                        "row_count": 1
                                    }},
                                    "port_groups": [
                                        {{
                                            "count": 2,
                                            "roles": [
                                                "leaf",
                                                "access"
                                            ],
                                            "speed": {{
                                                "unit": "G",
                                                "value": 10
                                            }}
                                        }}
                                    ],
                                    "port_indexing": {{
                                        "order": "T-B, L-R",
                                        "schema": "absolute",
                                        "start_index": 1
                                    }}
                                }}
                            ]
                        }},
                        {{
                            "display_name": "SONIC-12x10-Leaf",
                            "href": "#/design/logical-devices/SONIC-12x10-Leaf",
                            "id": "SONIC-12x10-Leaf",
                            "panels": [
                                {{
                                    "panel_layout": {{
                                        "column_count": 12,
                                        "row_count": 1
                                    }},
                                    "port_groups": [
                                        {{
                                            "count": 4,
                                            "roles": [
                                                "spine"
                                            ],
                                            "speed": {{
                                                "unit": "G",
                                                "value": 10
                                            }}
                                        }},
                                        {{
                                            "count": 6,
                                            "roles": [
                                                "generic"
                                            ],
                                            "speed": {{
                                                "unit": "G",
                                                "value": 10
                                            }}
                                        }},
                                        {{
                                            "count": 2,
                                            "roles": [
                                                "peer"
                                            ],
                                            "speed": {{
                                                "unit": "G",
                                                "value": 10
                                            }}
                                        }}
                                    ],
                                    "port_indexing": {{
                                        "order": "T-B, L-R",
                                        "schema": "absolute",
                                        "start_index": 1
                                    }}
                                }}
                            ]
                        }},
                        {{
                            "display_name": "AOS-2x10-1",
                            "href": "#/design/logical-devices/AOS-2x10-1",
                            "id": "AOS-2x10-1",
                            "panels": [
                                {{
                                    "panel_layout": {{
                                        "column_count": 2,
                                        "row_count": 1
                                    }},
                                    "port_groups": [
                                        {{
                                            "count": 2,
                                            "roles": [
                                                "leaf",
                                                "access"
                                            ],
                                            "speed": {{
                                                "unit": "G",
                                                "value": 10
                                            }}
                                        }}
                                    ],
                                    "port_indexing": {{
                                        "order": "T-B, L-R",
                                        "schema": "absolute",
                                        "start_index": 1
                                    }}
                                }}
                            ]
                        }},
                        {{
                            "display_name": "SONIC-12x10-Leaf",
                            "href": "#/design/logical-devices/SONIC-12x10-Leaf",
                            "id": "SONIC-12x10-Leaf",
                            "panels": [
                                {{
                                    "panel_layout": {{
                                        "column_count": 12,
                                        "row_count": 1
                                    }},
                                    "port_groups": [
                                        {{
                                            "count": 4,
                                            "roles": [
                                                "spine"
                                            ],
                                            "speed": {{
                                                "unit": "G",
                                                "value": 10
                                            }}
                                        }},
                                        {{
                                            "count": 6,
                                            "roles": [
                                                "generic"
                                            ],
                                            "speed": {{
                                                "unit": "G",
                                                "value": 10
                                            }}
                                        }},
                                        {{
                                            "count": 2,
                                            "roles": [
                                                "peer"
                                            ],
                                            "speed": {{
                                                "unit": "G",
                                                "value": 10
                                            }}
                                        }}
                                    ],
                                    "port_indexing": {{
                                        "order": "T-B, L-R",
                                        "schema": "absolute",
                                        "start_index": 1
                                    }}
                                }}
                            ]
                        }},
                        {{
                            "display_name": "AOS-2x10-1",
                            "href": "#/design/logical-devices/AOS-2x10-1",
                            "id": "AOS-2x10-1",
                            "panels": [
                                {{
                                    "panel_layout": {{
                                        "column_count": 2,
                                        "row_count": 1
                                    }},
                                    "port_groups": [
                                        {{
                                            "count": 2,
                                            "roles": [
                                                "leaf",
                                                "access"
                                            ],
                                            "speed": {{
                                                "unit": "G",
                                                "value": 10
                                            }}
                                        }}
                                    ],
                                    "port_indexing": {{
                                        "order": "T-B, L-R",
                                        "schema": "absolute",
                                        "start_index": 1
                                    }}
                                }}
                            ]
                        }},
                        {{
                            "display_name": "SONIC-12x10-Leaf",
                            "href": "#/design/logical-devices/SONIC-12x10-Leaf",
                            "id": "SONIC-12x10-Leaf",
                            "panels": [
                                {{
                                    "panel_layout": {{
                                        "column_count": 12,
                                        "row_count": 1
                                    }},
                                    "port_groups": [
                                        {{
                                            "count": 4,
                                            "roles": [
                                                "spine"
                                            ],
                                            "speed": {{
                                                "unit": "G",
                                                "value": 10
                                            }}
                                        }},
                                        {{
                                            "count": 6,
                                            "roles": [
                                                "generic"
                                            ],
                                            "speed": {{
                                                "unit": "G",
                                                "value": 10
                                            }}
                                        }},
                                        {{
                                            "count": 2,
                                            "roles": [
                                                "peer"
                                            ],
                                            "speed": {{
                                                "unit": "G",
                                                "value": 10
                                            }}
                                        }}
                                    ],
                                    "port_indexing": {{
                                        "order": "T-B, L-R",
                                        "schema": "absolute",
                                        "start_index": 1
                                    }}
                                }}
                            ]
                        }},
                        {{
                            "display_name": "AOS-2x10-1",
                            "href": "#/design/logical-devices/AOS-2x10-1",
                            "id": "AOS-2x10-1",
                            "panels": [
                                {{
                                    "panel_layout": {{
                                        "column_count": 2,
                                        "row_count": 1
                                    }},
                                    "port_groups": [
                                        {{
                                            "count": 2,
                                            "roles": [
                                                "leaf",
                                                "access"
                                            ],
                                            "speed": {{
                                                "unit": "G",
                                                "value": 10
                                            }}
                                        }}
                                    ],
                                    "port_indexing": {{
                                        "order": "T-B, L-R",
                                        "schema": "absolute",
                                        "start_index": 1
                                    }}
                                }}
                            ]
                        }},
                        {{
                            "display_name": "SONIC-12x10-Leaf",
                            "href": "#/design/logical-devices/SONIC-12x10-Leaf",
                            "id": "SONIC-12x10-Leaf",
                            "panels": [
                                {{
                                    "panel_layout": {{
                                        "column_count": 12,
                                        "row_count": 1
                                    }},
                                    "port_groups": [
                                        {{
                                            "count": 4,
                                            "roles": [
                                                "spine"
                                            ],
                                            "speed": {{
                                                "unit": "G",
                                                "value": 10
                                            }}
                                        }},
                                        {{
                                            "count": 6,
                                            "roles": [
                                                "generic"
                                            ],
                                            "speed": {{
                                                "unit": "G",
                                                "value": 10
                                            }}
                                        }},
                                        {{
                                            "count": 2,
                                            "roles": [
                                                "peer"
                                            ],
                                            "speed": {{
                                                "unit": "G",
                                                "value": 10
                                            }}
                                        }}
                                    ],
                                    "port_indexing": {{
                                        "order": "T-B, L-R",
                                        "schema": "absolute",
                                        "start_index": 1
                                    }}
                                }}
                            ]
                        }},
                        {{
                            "display_name": "AOS-2x10-1",
                            "href": "#/design/logical-devices/AOS-2x10-1",
                            "id": "AOS-2x10-1",
                            "panels": [
                                {{
                                    "panel_layout": {{
                                        "column_count": 2,
                                        "row_count": 1
                                    }},
                                    "port_groups": [
                                        {{
                                            "count": 2,
                                            "roles": [
                                                "leaf",
                                                "access"
                                            ],
                                            "speed": {{
                                                "unit": "G",
                                                "value": 10
                                            }}
                                        }}
                                    ],
                                    "port_indexing": {{
                                        "order": "T-B, L-R",
                                        "schema": "absolute",
                                        "start_index": 1
                                    }}
                                }}
                            ]
                        }},
                        {{
                            "display_name": "SONIC-12x10-Leaf",
                            "href": "#/design/logical-devices/SONIC-12x10-Leaf",
                            "id": "SONIC-12x10-Leaf",
                            "panels": [
                                {{
                                    "panel_layout": {{
                                        "column_count": 12,
                                        "row_count": 1
                                    }},
                                    "port_groups": [
                                        {{
                                            "count": 4,
                                            "roles": [
                                                "spine"
                                            ],
                                            "speed": {{
                                                "unit": "G",
                                                "value": 10
                                            }}
                                        }},
                                        {{
                                            "count": 6,
                                            "roles": [
                                                "generic"
                                            ],
                                            "speed": {{
                                                "unit": "G",
                                                "value": 10
                                            }}
                                        }},
                                        {{
                                            "count": 2,
                                            "roles": [
                                                "peer"
                                            ],
                                            "speed": {{
                                                "unit": "G",
                                                "value": 10
                                            }}
                                        }}
                                    ],
                                    "port_indexing": {{
                                        "order": "T-B, L-R",
                                        "schema": "absolute",
                                        "start_index": 1
                                    }}
                                }}
                            ]
                        }},
                        {{
                            "display_name": "AOS-2x10-1",
                            "href": "#/design/logical-devices/AOS-2x10-1",
                            "id": "AOS-2x10-1",
                            "panels": [
                                {{
                                    "panel_layout": {{
                                        "column_count": 2,
                                        "row_count": 1
                                    }},
                                    "port_groups": [
                                        {{
                                            "count": 2,
                                            "roles": [
                                                "leaf",
                                                "access"
                                            ],
                                            "speed": {{
                                                "unit": "G",
                                                "value": 10
                                            }}
                                        }}
                                    ],
                                    "port_indexing": {{
                                        "order": "T-B, L-R",
                                        "schema": "absolute",
                                        "start_index": 1
                                    }}
                                }}
                            ]
                        }},
                        {{
                            "display_name": "SONIC-12x10-Leaf",
                            "href": "#/design/logical-devices/SONIC-12x10-Leaf",
                            "id": "SONIC-12x10-Leaf",
                            "panels": [
                                {{
                                    "panel_layout": {{
                                        "column_count": 12,
                                        "row_count": 1
                                    }},
                                    "port_groups": [
                                        {{
                                            "count": 4,
                                            "roles": [
                                                "spine"
                                            ],
                                            "speed": {{
                                                "unit": "G",
                                                "value": 10
                                            }}
                                        }},
                                        {{
                                            "count": 6,
                                            "roles": [
                                                "generic"
                                            ],
                                            "speed": {{
                                                "unit": "G",
                                                "value": 10
                                            }}
                                        }},
                                        {{
                                            "count": 2,
                                            "roles": [
                                                "peer"
                                            ],
                                            "speed": {{
                                                "unit": "G",
                                                "value": 10
                                            }}
                                        }}
                                    ],
                                    "port_indexing": {{
                                        "order": "T-B, L-R",
                                        "schema": "absolute",
                                        "start_index": 1
                                    }}
                                }}
                            ]
                        }},
                        {{
                            "display_name": "SONIC-12x10-Leaf",
                            "href": "#/design/logical-devices/SONIC-12x10-Leaf",
                            "id": "SONIC-12x10-Leaf",
                            "panels": [
                                {{
                                    "panel_layout": {{
                                        "column_count": 12,
                                        "row_count": 1
                                    }},
                                    "port_groups": [
                                        {{
                                            "count": 4,
                                            "roles": [
                                                "spine"
                                            ],
                                            "speed": {{
                                                "unit": "G",
                                                "value": 10
                                            }}
                                        }},
                                        {{
                                            "count": 6,
                                            "roles": [
                                                "generic"
                                            ],
                                            "speed": {{
                                                "unit": "G",
                                                "value": 10
                                            }}
                                        }},
                                        {{
                                            "count": 2,
                                            "roles": [
                                                "peer"
                                            ],
                                            "speed": {{
                                                "unit": "G",
                                                "value": 10
                                            }}
                                        }}
                                    ],
                                    "port_indexing": {{
                                        "order": "T-B, L-R",
                                        "schema": "absolute",
                                        "start_index": 1
                                    }}
                                }}
                            ]
                        }},
                        {{
                            "display_name": "SONIC-12x10-Leaf",
                            "href": "#/design/logical-devices/SONIC-12x10-Leaf",
                            "id": "SONIC-12x10-Leaf",
                            "panels": [
                                {{
                                    "panel_layout": {{
                                        "column_count": 12,
                                        "row_count": 1
                                    }},
                                    "port_groups": [
                                        {{
                                            "count": 4,
                                            "roles": [
                                                "spine"
                                            ],
                                            "speed": {{
                                                "unit": "G",
                                                "value": 10
                                            }}
                                        }},
                                        {{
                                            "count": 6,
                                            "roles": [
                                                "generic"
                                            ],
                                            "speed": {{
                                                "unit": "G",
                                                "value": 10
                                            }}
                                        }},
                                        {{
                                            "count": 2,
                                            "roles": [
                                                "peer"
                                            ],
                                            "speed": {{
                                                "unit": "G",
                                                "value": 10
                                            }}
                                        }}
                                    ],
                                    "port_indexing": {{
                                        "order": "T-B, L-R",
                                        "schema": "absolute",
                                        "start_index": 1
                                    }}
                                }}
                            ]
                        }},
                        {{
                            "display_name": "SONIC-12x10-Leaf",
                            "href": "#/design/logical-devices/SONIC-12x10-Leaf",
                            "id": "SONIC-12x10-Leaf",
                            "panels": [
                                {{
                                    "panel_layout": {{
                                        "column_count": 12,
                                        "row_count": 1
                                    }},
                                    "port_groups": [
                                        {{
                                            "count": 4,
                                            "roles": [
                                                "spine"
                                            ],
                                            "speed": {{
                                                "unit": "G",
                                                "value": 10
                                            }}
                                        }},
                                        {{
                                            "count": 6,
                                            "roles": [
                                                "generic"
                                            ],
                                            "speed": {{
                                                "unit": "G",
                                                "value": 10
                                            }}
                                        }},
                                        {{
                                            "count": 2,
                                            "roles": [
                                                "peer"
                                            ],
                                            "speed": {{
                                                "unit": "G",
                                                "value": 10
                                            }}
                                        }}
                                    ],
                                    "port_indexing": {{
                                        "order": "T-B, L-R",
                                        "schema": "absolute",
                                        "start_index": 1
                                    }}
                                }}
                            ]
                        }},
                        {{
                            "display_name": "SONIC-12x10-Leaf",
                            "href": "#/design/logical-devices/SONIC-12x10-Leaf",
                            "id": "SONIC-12x10-Leaf",
                            "panels": [
                                {{
                                    "panel_layout": {{
                                        "column_count": 12,
                                        "row_count": 1
                                    }},
                                    "port_groups": [
                                        {{
                                            "count": 4,
                                            "roles": [
                                                "spine"
                                            ],
                                            "speed": {{
                                                "unit": "G",
                                                "value": 10
                                            }}
                                        }},
                                        {{
                                            "count": 6,
                                            "roles": [
                                                "generic"
                                            ],
                                            "speed": {{
                                                "unit": "G",
                                                "value": 10
                                            }}
                                        }},
                                        {{
                                            "count": 2,
                                            "roles": [
                                                "peer"
                                            ],
                                            "speed": {{
                                                "unit": "G",
                                                "value": 10
                                            }}
                                        }}
                                    ],
                                    "port_indexing": {{
                                        "order": "T-B, L-R",
                                        "schema": "absolute",
                                        "start_index": 1
                                    }}
                                }}
                            ]
                        }},
                        {{
                            "display_name": "SONIC-12x10-Leaf",
                            "href": "#/design/logical-devices/SONIC-12x10-Leaf",
                            "id": "SONIC-12x10-Leaf",
                            "panels": [
                                {{
                                    "panel_layout": {{
                                        "column_count": 12,
                                        "row_count": 1
                                    }},
                                    "port_groups": [
                                        {{
                                            "count": 4,
                                            "roles": [
                                                "spine"
                                            ],
                                            "speed": {{
                                                "unit": "G",
                                                "value": 10
                                            }}
                                        }},
                                        {{
                                            "count": 6,
                                            "roles": [
                                                "generic"
                                            ],
                                            "speed": {{
                                                "unit": "G",
                                                "value": 10
                                            }}
                                        }},
                                        {{
                                            "count": 2,
                                            "roles": [
                                                "peer"
                                            ],
                                            "speed": {{
                                                "unit": "G",
                                                "value": 10
                                            }}
                                        }}
                                    ],
                                    "port_indexing": {{
                                        "order": "T-B, L-R",
                                        "schema": "absolute",
                                        "start_index": 1
                                    }}
                                }}
                            ]
                        }}
                    ],
                    "tags": []
                    }}'''},
                    }

    return rack_type_dic
