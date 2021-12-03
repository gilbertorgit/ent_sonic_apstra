"""
---------------------------------
 Author: Gilberto Rampini
 Date: 12/2021
---------------------------------
"""
""" -------------- Logical Interface """


def create_logical_devices_dic():

    logical_data_dic = {'SONIC-10x10-BorderLeaf': {'name': 'SONIC-10x10-BorderLeaf',
                                                 'data': f'''{{
                        "create-mode?": true,
                        "display_name": "SONIC-10x10-BorderLeaf",
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
                                }},
                                "selected-port-count": 6
                            }}
                        ]
                        }}'''},

                        'SONIC-10x10-Spine': {'name': 'SONIC-10x10-Spine',
                                                 'data': f'''{{
                        "create-mode?": true,
                        "display_name": "SONIC-10x10-Spine",
                        "id": "SONIC-10x10-Spine",
                        "panels": [
                            {{
                                "panel_layout": {{
                                    "column_count": 10,
                                    "row_count": 1
                                }},
                                "port_groups": [
                                    {{
                                        "count": 8,
                                        "roles": [
                                            "superspine",
                                            "leaf"
                                        ],
                                        "speed": {{
                                            "unit": "G",
                                            "value": 10
                                        }}
                                    }},
                                    {{
                                        "count": 2,
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
                                }},
                                "selected-port-count": 2
                            }}
                        ]
                        }}'''},
                        'SONIC-12x10-Leaf': {'name': 'SONIC-12x10-Leaf',
                                                 'data': f'''{{
                        "create-mode?": true,
                        "display_name": "SONIC-12x10-Leaf",
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
                                }},
                                "selected-port-count": 2
                            }}
                        ]
                        }}'''},
                        }

    return logical_data_dic
