from .ini_file import IniFile


# =============================================================================
# NetDevFile
# Virtual Network Device Configuration
# https://www.freedesktop.org/software/systemd/man/systemd.netdev.html
# NOT ALL SECTIONS ARE INCLUDED
# NOT ALL OPTIONS IN THE SECTIONS ARE INCLUDED
# =============================================================================
class NetDevFile(IniFile):

    def __init__(self, file_name=''):
        IniFile.__init__(self, file_name)

        # Match section
        self.add_properties('match',
                            [['host'],
                             ['virtualization'],
                             ['kernel_command_line'],
                             ['architecture']
                            ]
                           )
        # NetDev section
        self.add_properties('net_dev',
                            [['description'],
                             ['name'],
                             ['kind'],
                             ['mtu_bytes'],
                             ['mac_address']
                            ]
                           )

        # Bridge section
        self.add_properties('bridge',
                            [['hello_time_sec'],
                             ['max_age_sec'],
                             ['forward_delay_sec'],
                             ['ageing_time_sec'],
                             ['priority'],
                             ['group_forward_mask'],
                             ['default_pvid'],
                             ['multicast_querier', 'b'],
                             ['multicast_snooping', 'b'],
                             ['vlan_filtering', 'b'],
                             ['stp', 'b'],
                             ['multicast_igmp_version']
                            ]
                           )

        # VLAN section
        self.add_properties('vlan',
                            [['id'],
                             ['gvrp', 'b'],
                             ['mvrp', 'b'],
                             ['loose_binding', 'b'],
                             ['reorder_header', 'b']
                            ]
                           )

        # MACVLAN section
        self.add_properties('macvlan',
                            [['mode']
                            ]
                           )

        # VXVLAN section
        self.add_properties('vxvlan',
                            [['id'],
                             ['group'],
                             ['tos'],
                             ['ttl'],
                             ['mac_learning', 'b']
                            ]
                           )

        # Tunnel section
        self.add_properties('vlan',
                            [['local'],
                             ['remote'],
                             ['tos'],
                             ['ttl'],
                             ['discover_path_mtu', 'b']
                            ]
                           )

        # Peer section
        self.add_properties('peer',
                            [['name'],
                             ['mac_address']
                            ]
                           )

        # Tun section
        self.add_properties('tun',
                            [['multi_queue', 'b'],
                             ['packet_info', 'b'],
                             ['v_net_header', 'b'],
                             ['user'],
                             ['group']
                            ]
                           )

        # Tap section
        self.add_properties('tap',
                            [['multi_queue', 'b'],
                             ['packet_info', 'b'],
                             ['v_net_header', 'b'],
                             ['user'],
                             ['group']
                            ]
                           )

    def create(self,
               name=None,
               kind=None
              ):
        """Create a netdev file with minimal options.

        :param string name: interface name
        :param string kind: virtual interface kind (vlan, bridge, etc.)
        """

        self.add_section("NetDev")
        if name:
            self.net_dev_name = name
        if kind:
            self.net_dev_kind = kind
        self.save()
