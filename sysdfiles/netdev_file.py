from .ini_file import IniFile


# =============================================================================
# NetDevFile
# Reference; https://manpages.debian.org/jessie/systemd/systemd.netdev.5.en.html
# =============================================================================
class NetDevFile(IniFile):

    def __init__(self, file_name=''):
        IniFile.__init__(self, file_name)

        # Match section
        self.add_properties('match',
                            [['host'],
                             ['virtualization'],
                             ['kernelcommandline'],
                             ['architecture']
                            ]
                           )
        # NetDev section
        self.add_properties('netdev',
                            [['name'],
                             ['kind'],
                             ['mtubytes'],
                             ['macaddress']
                            ]
                           )

        # VLAN section
        self.add_properties('vlan',
                            [['id']
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
                             ['maclearning']
                            ]
                           )

        # Tunnel section
        self.add_properties('vlan',
                            [['local'],
                             ['remote'],
                             ['tos'],
                             ['ttl'],
                             ['discoverpathmtu']
                            ]
                           )

        # Peer section
        self.add_properties('peer',
                            [['name'],
                             ['macaddress']
                            ]
                           )

        # Tun section
        self.add_properties('tun',
                            [['onequeue'],
                             ['multiqueue'],
                             ['packetinfo'],
                             ['user'],
                             ['group']
                            ]
                           )

        # Tap section
        self.add_properties('tap',
                            [['onequeue'],
                             ['multiqueue'],
                             ['packetinfo'],
                             ['user'],
                             ['group']
                            ]
                           )
