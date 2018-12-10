import os
import uuid
from sysdfiles import HostsFile, HostnameFile, MachineIdFile, MachineInfoFile, OSReleaseFile
from tests import TestInfo, compare_files, check_hosts, check_string


class TestOtherFiles:
    def __init__(self):
        self.is_setup = False

    def setUp(self):
        assert not self.is_setup
        print('')

        self.is_setup = True
        self.test_info = TestInfo()

    def tearDown(self):
        assert self.is_setup
        print('')

        if self.test_info.num_errors == 1:
            print('1 error')
        else:
            print('{0:d} errors'.format(self.test_info.num_errors))
        self.is_setup = False

    def test_10_hosts(self):
        assert self.is_setup
        print('')

        file_name1 = os.path.join(os.path.dirname(__file__), 'hosts1')
        file_name2 = os.path.join(os.path.dirname(__file__), 'hosts2')
        hosts = HostsFile(file_name1)
        saved_host_name = hosts.host_name
        saved_domain_name = hosts.domain_name
        print(saved_host_name + '   ' + saved_domain_name)

        self.test_info.test_number += 1
        i, line = hosts.get_line('127.0.0.1')
        print('{0:d} - {1:d} {2!r}'.format(self.test_info.test_number, i, line))
        if line is None:
            self.test_info.num_errors += 1
            print("ERROR: couldn't find 127.0.0.1")

        self.test_info.test_number += 1
        i, line = hosts.get_line('127.0.1.1')
        print('{0:d} - {1:d} {2!r}'.format(self.test_info.test_number, i, line))
        if line is None:
            self.test_info.num_errors += 1
            print("ERROR: couldn't find 127.0.1.1")

        hosts.host_name = 'server1.home.net'
        assert 0 == check_hosts(self.test_info, hosts, line, 'server1', 'home.net')

        hosts.host_name = 'server2'
        assert 0 == check_hosts(self.test_info, hosts, line, 'server2', 'home.net')

        hosts.domain_name = 'home.org'
        assert 0 == check_hosts(self.test_info, hosts, line, 'server2', 'home.org')

        hosts.domain_name = 'server2.home.net'
        assert 0 == check_hosts(self.test_info, hosts, line, 'server2', 'home.net')

        hosts.host_name = saved_host_name
        hosts.domain_name = saved_domain_name
        hosts.save(file_name2)
        assert 0 == compare_files(self.test_info, file_name1, file_name2)

    def test_20_hostname(self):
        assert self.is_setup
        print('')

        file_name1 = os.path.join(os.path.dirname(__file__), 'hostname1')
        file_name2 = os.path.join(os.path.dirname(__file__), 'hostname2')
        hostname = HostnameFile(file_name1)
        saved_name = hostname.value

        assert 0 == check_string(self.test_info, 'hostname', hostname.value, 'iceberg')

        hostname.value = 'fred'
        assert 0 == check_string(self.test_info, 'hostname', hostname.value, 'fred')

        hostname.save(file_name2)
        hostname = HostnameFile(file_name2)
        assert 0 == check_string(self.test_info, 'hostname', hostname.value, 'fred')

        hostname.value = saved_name
        hostname.save(file_name2)
        assert 0 == compare_files(self.test_info, file_name1, file_name2)

    def test_30_machine_id(self):
        assert self.is_setup
        print('')

        file_name1 = os.path.join(os.path.dirname(__file__), 'machine-id1')
        file_name2 = os.path.join(os.path.dirname(__file__), 'machine-id2')
        mid = MachineIdFile(file_name1)
        saved_id = mid.value

        assert 0 == check_string(self.test_info, 'machine-id', mid.value, '8a0162f4bd434e3eb5bea4d77d36ed3a')

        new_id = uuid.uuid4().hex
        mid.value = new_id
        assert 0 == check_string(self.test_info, 'machine-id', mid.value, new_id)

        mid.save(file_name2)
        mid = MachineIdFile(file_name2)
        assert 0 == check_string(self.test_info, 'machine-id', mid.value, new_id)

        mid.value = saved_id
        mid.save(file_name2)
        assert 0 == compare_files(self.test_info, file_name1, file_name2)

    def test_40_machine_info(self):
        assert self.is_setup
        print('')

        file_name1 = os.path.join(os.path.dirname(__file__), 'machine-info1')
        file_name2 = os.path.join(os.path.dirname(__file__), 'machine-info2')
        info = MachineInfoFile(file_name1)

        assert 0 == check_string(self.test_info, 'pretty_host_name', info.pretty_host_name, 'Main Server (iceberg)')
        assert 0 == check_string(self.test_info, 'icon_name', info.icon_name, 'computer')
        assert 0 == check_string(self.test_info, 'chassis', info.chassis, 'server')
        assert 0 == check_string(self.test_info, 'deployment', info.deployment, 'development')
        assert 0 == check_string(self.test_info, 'location', info.location, 'Utility Room')

        saved_location = info.location
        info.location = None
        assert 0 == check_string(self.test_info, 'location', info.location, None)
        assert 0 == check_string(self.test_info, 'location', info.location, '')
        info.location = saved_location
        assert 0 == check_string(self.test_info, 'location', info.location, saved_location)

        saved_deployment = info.deployment
        new_deployment = 'production'
        info.deployment = new_deployment
        assert 0 == check_string(self.test_info, 'deployment', info.deployment, new_deployment)

        info.save(file_name2)
        info = MachineInfoFile(file_name2)
        assert 0 == check_string(self.test_info, 'deployment', info.deployment, new_deployment)

        info.deployment = saved_deployment
        info.save(file_name2)
        assert 0 == compare_files(self.test_info, file_name1, file_name2)

    def test_50_os_release(self):
        assert self.is_setup
        print('')

        file_name1 = os.path.join(os.path.dirname(__file__), 'os-release1')
        file_name2 = os.path.join(os.path.dirname(__file__), 'os-release2')
        osr = OSReleaseFile(file_name1)

        assert 0 == check_string(self.test_info, 'pretty_name', osr.pretty_name, 'Debian GNU/Linux buster/sid')
        assert 0 == check_string(self.test_info, 'name', osr.name, 'Debian GNU/Linux')
        assert 0 == check_string(self.test_info, 'id', osr.id, 'debian')
        assert 0 == check_string(self.test_info, 'home_url', osr.home_url, 'https://www.debian.org/')
        assert 0 == check_string(self.test_info, 'support_url', osr.support_url, 'https://www.debian.org/support')
        assert 0 == check_string(self.test_info, 'bug_report_url', osr.bug_report_url, 'https://bugs.debian.org/')

        assert 0 == check_string(self.test_info, 'version', osr.version, None)
        assert 0 == check_string(self.test_info, 'name', osr.build_id, '')

        saved_bug_report_url = osr.bug_report_url
        osr.bug_report_url = None
        assert 0 == check_string(self.test_info, 'bug_report_url', osr.bug_report_url, None)
        assert 0 == check_string(self.test_info, 'bug_report_url', osr.bug_report_url, '')
        osr.bug_report_url = saved_bug_report_url
        assert 0 == check_string(self.test_info, 'bug_report_url', osr.bug_report_url, saved_bug_report_url)

        saved_id = osr.id
        new_id = 'debbie'
        osr.id = new_id
        assert 0 == check_string(self.test_info, 'id', osr.id, new_id)

        osr.save(file_name2)
        osr = OSReleaseFile(file_name2)
        assert 0 == check_string(self.test_info, 'id', osr.id, new_id)

        osr.id = saved_id
        osr.save(file_name2)
        assert 0 == compare_files(self.test_info, file_name1, file_name2)
