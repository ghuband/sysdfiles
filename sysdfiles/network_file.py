from .ini_file import IniFile


# =============================================================================
# NetworkFile
# =============================================================================
class NetworkFile(IniFile):

    def __init__(self, file_name=''):
        IniFile.__init__(self, file_name)
        self.add_properties('match',
                            [['architecture'],
                             ['driver', 'l'],
                             ['host'],
                             ['kernel_command_line'],
                             ['kernel_version'],
                             ['mac_address', 'l', ' ', 3],
                             ['name', 'l'],
                             ['path', 'l'],
                             ['type', 'l'],
                             ['virtualization']])
        self.add_properties('link',
                            [['all_multicast', 'b'],
                             ['arp', 'b'],
                             ['mac_address'],
                             ['mtu_bytes', 'nb'],
                             ['multicast', 'b'],
                             ['required_for_online', 'b'],
                             ['unmanaged', 'b']])
        self.add_properties('network',
                            [['active_slave', 'b'],
                             ['address', 'l', ' ', 1],
                             ['bind_carrier', 'l'],
                             ['bond'],
                             ['bridge'],
                             ['configure_without_carrier', 'b'],
                             ['description'],
                             ['dhcp'],
                             ['dhcp_server', 'b'],
                             ['dns', 'l', ' ', 1],
                             ['dns_over_tls'],
                             ['dnssec'],
                             ['dnssec_negative_trust_anchors', 'l'],
                             ['domains', 'l'],
                             ['emit_lldp'],
                             ['gateway', 'l', ' ', 1],
                             ['ip_forward'],
                             ['ip_masquerade', 'b'],
                             ['ipv4_ll_route', 'b'],
                             ['ipv4_proxy_arp', 'b'],
                             ['ipv6_accept_ra', 'b'],
                             ['ipv6_duplicate_address_detection'],
                             ['ipv6_hop_limit', 'i'],
                             ['ipv6_mtu_bytes', 'nb'],
                             ['ipv6_prefix_delegation'],
                             ['ipv6_privacy_extensions'],
                             ['ipv6_proxy_ndp', 'b'],
                             ['ipv6_proxy_ndp_address', 'l', ' ', 1],
                             ['ipv6_token'],
                             ['link_local_addressing'],
                             ['lldp'],
                             ['llmnr'],
                             ['mac_vlan', 'l', ' ', 1],
                             ['multicast_dns'],
                             ['ntp', 'l', ' ', 1],
                             ['primary_slave', 'b'],
                             ['tunnel', 'l', ' ', 1],
                             ['vlan', 'l', ' ', 1],
                             ['vrf'],
                             ['vxlan', 'l', ' ', 1]])
        self.add_properties('address',
                            [['auto_join', 'b'],
                             ['address', 'l', ' ', 1],
                             ['broadcast'],
                             ['duplicate_address_detection', 'b'],
                             ['home_address', 'b'],
                             ['label'],
                             ['manage_temporary_address', 'b'],
                             ['peer', 'l', ' ', 1],
                             ['preferred_lifetime'],
                             ['prefix_route', 'b'],
                             ['scope']])
        self.add_properties('ipv6_address_label',
                            [['label', 'i'],
                             ['prefix']])
        self.add_properties('routing_policy_rule',
                            [['firewall_mark', 'i'],
                             ['from'],
                             ['incoming_interface'],
                             ['outgoing_interface'],
                             ['priority', 'i'],
                             ['table', 'i'],
                             ['to'],
                             ['type_of_service', 'i']])
        self.add_properties('route',
                            [['destination'],
                             ['gateway', 'l', ' ', 1],
                             ['gateway_on_link', 'b'],
                             ['initial_advertised_receive_window', 'nb'],
                             ['initial_congestion_window', 'nb'],
                             ['ipv6_preference'],
                             ['metric', 'i'],
                             ['mtu_bytes', 'nb'],
                             ['preferred_source'],
                             ['protocol'],
                             ['quick_ack', 'b'],
                             ['scope'],
                             ['source'],
                             ['table', 'i'],
                             ['type']])
        self.add_properties('dhcp',
                            [['anonymize', 'b'],
                             ['client_identifier'],
                             ['critical_connection', 'b'],
                             ['duid_raw_data'],
                             ['duid_type'],
                             ['host_name'],
                             ['iad', 'i'],
                             ['listen_port', 'i'],
                             ['rapid_commit', 'b'],
                             ['request_broadcast', 'b'],
                             ['route_metric', 'i'],
                             ['route_table', 'i'],
                             ['send_host_name', 'b'],
                             ['use_dns', 'b'],
                             ['use_domains'],
                             ['use_host_name', 'b'],
                             ['use_mtu', 'b'],
                             ['use_ntp', 'b'],
                             ['use_routes', 'b'],
                             ['use_timezone', 'b'],
                             ['user_class', 'l'],
                             ['vendor_class_identifier']])
        self.add_properties('ipv6_accept_ra',
                            [['route_table', 'i'],
                             ['use_domains'],
                             ['use_dns', 'b']])
        self.add_properties('dhcp_server',
                            [['default_lease_time_sec', 'ns'],
                             ['dns', 'l'],
                             ['emit_dns', 'b'],
                             ['emit_ntp', 'b'],
                             ['emit_router', 'b'],
                             ['emit_time_zone', 'b'],
                             ['max_lease_time_sec', 'ns'],
                             ['ntp', 'l'],
                             ['pool_offset', 'i'],
                             ['pool_size', 'i'],
                             ['router', 'l'],
                             ['time_zone']])
        self.add_properties('ipv6_prefix_delegation',
                            [['emit_dns', 'b'],
                             ['emit_domains', 'b'],
                             ['dns', 'l'],
                             ['dns_lifetime_sec', 'ns'],
                             ['domains', 'l'],
                             ['managed', 'b'],
                             ['other_information', 'b'],
                             ['router_lifetime_sec', 'ns'],
                             ['router_preference']])
        self.add_properties('ipv6_prefix',
                            [['address_auto_configuration', 'b'],
                             ['on_link', 'b'],
                             ['preferred_lifetime_sec', 'ns'],
                             ['prefix'],
                             ['valid_lifetime_sec', 'ns']])
        self.add_properties('bridge',
                            [['allow_port_to_be_root', 'b'],
                             ['cost', 'i'],
                             ['fast_leave', 'b'],
                             ['hair_pin', 'b'],
                             ['priority', 'i'],
                             ['unicast_flood', 'b'],
                             ['use_bpdu', 'b']])
        self.add_properties('bridge_fdb',
                            [['mac_address'],
                             ['vlan_id']])
        self.add_properties('can',
                            [['bit_rate', 'bps'],
                             ['restart_sec', 'ns'],
                             ['sample_point']])
        self.add_properties('bridge_vlan',
                            [['egress_untagged'],
                             ['pv_id'],
                             ['vlan']])

    def create(self,
               name,
               dhcp="yes",
               address=None,
               gateway=None
              ):
        """Create a network file with most common options.

        :param string name: interface name, ie "eth0"
        :param string dhcp: DHCP setting
        :param string address: IP adddress to assign to the interface
        :param string gateway: the gateway IP address
        """

        self.add_section("Match")
        self.match_name = name
        self.add_section("Network")
        self.network_dhcp = dhcp
        if address:
            self.network_address = address
        if gateway:
            self.network_gateway = gateway
