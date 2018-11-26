import os
from sysdfiles import HostsFile
from tests import TestInfo, compare_files, check_names


class TestHosts:
    def __init__(self):
        self.is_setup = False

    def setUp(self):
        assert not self.is_setup
        self.is_setup = True
        self.test_info = TestInfo()
        self.file_name1 = os.path.join(os.path.dirname(__file__), 'hosts1')
        self.file_name2 = os.path.join(os.path.dirname(__file__), 'hosts2')
        self.hosts = HostsFile(self.file_name1)
        self.saved_host_name = self.hosts.host_name
        self.saved_domain_name = self.hosts.domain_name
        print(self.saved_host_name + '   ' + self.saved_domain_name)

    def tearDown(self):
        assert self.is_setup

        if self.test_info.num_errors == 1:
            print('1 error')
        else:
            print('{0:d} errors'.format(self.test_info.num_errors))
        self.is_setup = False

    def test_hosts(self):
        assert self.is_setup

        self.test_info.test_number += 1
        i, line = self.hosts.get_line('127.0.0.1')
        print('{0:d} - {1:d} {2!r}'.format(self.test_info.test_number, i, line))
        if line is None:
            self.test_info.num_errors += 1
            print("ERROR: couldn't find 127.0.0.1")

        self.test_info.test_number += 1
        i, line = self.hosts.get_line('127.0.1.1')
        print('{0:d} - {1:d} {2!r}'.format(self.test_info.test_number, i, line))
        if line is None:
            self.test_info.num_errors += 1
            print("ERROR: couldn't find 127.0.1.1")

        self.hosts.host_name = 'server1.home.net'
        assert 0 == check_names(self.test_info, self.hosts, line, 'server1', 'home.net')

        self.hosts.host_name = 'server2'
        assert 0 == check_names(self.test_info, self.hosts, line, 'server2', 'home.net')

        self.hosts.domain_name = 'home.org'
        assert 0 == check_names(self.test_info, self.hosts, line, 'server2', 'home.org')

        self.hosts.domain_name = 'server2.home.net'
        assert 0 == check_names(self.test_info, self.hosts, line, 'server2', 'home.net')

        self.hosts.host_name = self.saved_host_name
        self.hosts.domain_name = self.saved_domain_name
        self.hosts.save(file_name=self.file_name2)
        assert 0 == compare_files(self.test_info, self.file_name1, self.file_name2)
