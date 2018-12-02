from sysdfiles import IniFile, NetworkFile, ServiceFile
from tests import *


class TestIniFile:
    def __init__(self):
        self.is_setup = False

    # =========================================================================
    # setUp
    # =========================================================================
    def setUp(self):
        assert not self.is_setup
        print('')

        self.test_info = TestInfo()
        self.ini_file_name1 = os.path.join(os.path.dirname(__file__), 'lan1.network')
        self.ini_file_name2 = os.path.join(os.path.dirname(__file__), 'lan2.network')
        self.ini = IniFile(self.ini_file_name1)
        self.is_setup = True

    # =========================================================================
    # tearDown
    # =========================================================================
    def tearDown(self):
        assert self.is_setup
        print('')

        if self.test_info.num_errors == 1:
            print('1 error')
        else:
            print('{0:d} errors'.format(self.test_info.num_errors))
        self.is_setup = False

    # =========================================================================
    # test_00_files
    # =========================================================================
    def test_00_files(self):
        assert self.is_setup
        print('')

        self.ini.save(self.ini_file_name2)
        assert 0 == compare_files(self.test_info, self.ini_file_name1, self.ini_file_name2)

    # =========================================================================
    # test_05_formatted_data
    # =========================================================================
    def test_05_formatted_data(self):
        assert self.is_setup
        print('')

        assert 0 == check_str_to_sec(self.test_info, '1years', IniFile.SECONDS_PER_YEAR, '1y')
        assert 0 == check_str_to_sec(self.test_info, '1year', IniFile.SECONDS_PER_YEAR, '1y')
        assert 0 == check_str_to_sec(self.test_info, '1y', IniFile.SECONDS_PER_YEAR)
        assert 0 == check_str_to_sec(self.test_info, '1months', IniFile.SECONDS_PER_MONTH, '1M')
        assert 0 == check_str_to_sec(self.test_info, '1month', IniFile.SECONDS_PER_MONTH, '1M')
        assert 0 == check_str_to_sec(self.test_info, '1M', IniFile.SECONDS_PER_MONTH)
        assert 0 == check_str_to_sec(self.test_info, '1weeks', IniFile.SECONDS_PER_WEEK, '1w')
        assert 0 == check_str_to_sec(self.test_info, '1week', IniFile.SECONDS_PER_WEEK, '1w')
        assert 0 == check_str_to_sec(self.test_info, '1w', IniFile.SECONDS_PER_WEEK)
        assert 0 == check_str_to_sec(self.test_info, '1days', IniFile.SECONDS_PER_DAY, '1d')
        assert 0 == check_str_to_sec(self.test_info, '1day', IniFile.SECONDS_PER_DAY, '1d')
        assert 0 == check_str_to_sec(self.test_info, '1d', IniFile.SECONDS_PER_DAY)
        assert 0 == check_str_to_sec(self.test_info, '1hours', IniFile.SECONDS_PER_HOUR, '1h')
        assert 0 == check_str_to_sec(self.test_info, '1hour', IniFile.SECONDS_PER_HOUR, '1h')
        assert 0 == check_str_to_sec(self.test_info, '1hr', IniFile.SECONDS_PER_HOUR, '1h')
        assert 0 == check_str_to_sec(self.test_info, '1h', IniFile.SECONDS_PER_HOUR)
        assert 0 == check_str_to_sec(self.test_info, '1minutes', 60, '1m')
        assert 0 == check_str_to_sec(self.test_info, '1minute', 60, '1m')
        assert 0 == check_str_to_sec(self.test_info, '1min', 60, '1m')
        assert 0 == check_str_to_sec(self.test_info, '1m', 60)
        assert 0 == check_str_to_sec(self.test_info, '1seconds', 1, '1s')
        assert 0 == check_str_to_sec(self.test_info, '1second', 1, '1s')
        assert 0 == check_str_to_sec(self.test_info, '1sec', 1, '1s')
        assert 0 == check_str_to_sec(self.test_info, '1s', 1)
        assert 0 == check_str_to_sec(self.test_info, '1', 1, '1s')
        assert 0 == check_str_to_sec(self.test_info, '0s', 0)
        assert 0 == check_str_to_sec(self.test_info, '0', 0, '0s')
        assert 0 == check_str_to_sec(self.test_info, 'infinity', IniFile.SECONDS_INFINITY)
        assert 0 == check_str_to_sec(self.test_info, '1msec', IniFile.SECONDS_PER_MS, '1ms')
        assert 0 == check_str_to_sec(self.test_info, '1ms', IniFile.SECONDS_PER_MS)
        assert 0 == check_str_to_sec(self.test_info, '1usec', IniFile.SECONDS_PER_US, '1us')
        assert 0 == check_str_to_sec(self.test_info, '1us', IniFile.SECONDS_PER_US)
        assert 0 == check_str_to_sec(self.test_info, '1nsec', IniFile.SECONDS_PER_NS, '1ns')
        assert 0 == check_str_to_sec(self.test_info, '1ns', IniFile.SECONDS_PER_NS)
        assert 0 == check_str_to_sec(self.test_info, '1', IniFile.SECONDS_PER_NS, '1ns', IniFile.SECONDS_PER_NS)
        assert 0 == check_str_to_sec(self.test_info, '1d24h1440m86401s', IniFile.SECONDS_PER_DAY * 4 + 1, '4d 1s')
        sec = IniFile.SECONDS_PER_WEEK + IniFile.SECONDS_PER_DAY + IniFile.SECONDS_PER_HOUR +\
              IniFile.SECONDS_PER_MINUTE + 1
        assert 0 == check_str_to_sec(self.test_info, '1w 1d 1h 1m 1s', sec)
        assert 0 == check_str_to_sec(self.test_info, ' 1 d  1w 1   s  1 m  1h', sec, '1w 1d 1h 1m 1s')

        assert 0 == check_sec_to_str(self.test_info, IniFile.SECONDS_INFINITY, 'infinity')
        assert 0 == check_sec_to_str(self.test_info, 1, '1s')
        assert 0 == check_sec_to_str(self.test_info, IniFile.SECONDS_PER_YEAR, '1y')
        assert 0 == check_sec_to_str(self.test_info, IniFile.SECONDS_PER_MONTH, '1M')
        assert 0 == check_sec_to_str(self.test_info, IniFile.SECONDS_PER_WEEK, '1w')
        assert 0 == check_sec_to_str(self.test_info, IniFile.SECONDS_PER_DAY, '1d')
        assert 0 == check_sec_to_str(self.test_info, IniFile.SECONDS_PER_HOUR, '1h')
        assert 0 == check_sec_to_str(self.test_info, IniFile.SECONDS_PER_MS, '1ms')
        assert 0 == check_sec_to_str(self.test_info, IniFile.SECONDS_PER_US, '1us')
        assert 0 == check_sec_to_str(self.test_info, IniFile.SECONDS_PER_NS, '1ns')
        assert 0 == check_sec_to_str(self.test_info, IniFile.SECONDS_PER_WEEK +
                                     IniFile.SECONDS_PER_DAY + IniFile.SECONDS_PER_HOUR +
                                     IniFile.SECONDS_PER_MINUTE + 1, '1w 1d 1h 1m 1s')

        assert 0 == check_str_to_nb(self.test_info, '1', 1)
        assert 0 == check_str_to_nb(self.test_info, '1K', IniFile.KILOBYTE)
        assert 0 == check_str_to_nb(self.test_info, str(IniFile.KILOBYTE), IniFile.KILOBYTE, '1K')
        assert 0 == check_str_to_nb(self.test_info, '1M', IniFile.MEGABYTE)
        assert 0 == check_str_to_nb(self.test_info, str(IniFile.MEGABYTE), IniFile.MEGABYTE, '1M')
        assert 0 == check_str_to_nb(self.test_info, '1G', IniFile.GIGABYTE)
        assert 0 == check_str_to_nb(self.test_info, str(IniFile.GIGABYTE), IniFile.GIGABYTE, '1G')
        assert 0 == check_str_to_nb(self.test_info, '1T', IniFile.TERABYTE)
        assert 0 == check_str_to_nb(self.test_info, str(IniFile.TERABYTE), IniFile.TERABYTE, '1T')
        assert 0 == check_str_to_nb(self.test_info, '1P', IniFile.PETABYTE)
        assert 0 == check_str_to_nb(self.test_info, str(IniFile.PETABYTE), IniFile.PETABYTE, '1P')

        assert 0 == check_nb_to_str(self.test_info, 1, '1')
        assert 0 == check_nb_to_str(self.test_info, IniFile.KILOBYTE + 1, str(IniFile.KILOBYTE + 1))
        assert 0 == check_nb_to_str(self.test_info, IniFile.KILOBYTE, '1K')
        assert 0 == check_nb_to_str(self.test_info, IniFile.MEGABYTE, '1M')
        assert 0 == check_nb_to_str(self.test_info, IniFile.GIGABYTE, '1G')
        assert 0 == check_nb_to_str(self.test_info, IniFile.TERABYTE, '1T')
        assert 0 == check_nb_to_str(self.test_info, IniFile.PETABYTE, '1P')

        assert 0 == check_str_to_bps(self.test_info, '1', 1)
        assert 0 == check_str_to_bps(self.test_info, '1K', IniFile.THOUSAND)
        assert 0 == check_str_to_bps(self.test_info, str(IniFile.THOUSAND), IniFile.THOUSAND, '1K')
        assert 0 == check_str_to_bps(self.test_info, '1M', IniFile.MILLION)
        assert 0 == check_str_to_bps(self.test_info, str(IniFile.MILLION), IniFile.MILLION, '1M')
        assert 0 == check_str_to_bps(self.test_info, '1G', IniFile.BILLION)
        assert 0 == check_str_to_bps(self.test_info, str(IniFile.BILLION), IniFile.BILLION, '1G')

        assert 0 == check_bps_to_str(self.test_info, 1, '1')
        assert 0 == check_bps_to_str(self.test_info, IniFile.THOUSAND + 1, str(IniFile.THOUSAND + 1))
        assert 0 == check_bps_to_str(self.test_info, IniFile.THOUSAND, '1K')
        assert 0 == check_bps_to_str(self.test_info, IniFile.MILLION, '1M')
        assert 0 == check_bps_to_str(self.test_info, IniFile.BILLION, '1G')

        assert 0 == check_str_to_fm(self.test_info, '0755', 0o755)
        assert 0 == check_fm_to_str(self.test_info, 0o755, '0755')

    # =========================================================================
    # test_10_section
    # =========================================================================
    def test_10_section(self):
        assert self.is_setup
        print('')

        section, options = self.ini.get_section('Match')
        assert 0 == check_section(self.test_info, section, options, 'Match')

        section, options = self.ini.get_section('match')
        assert 0 == check_section(self.test_info, section, options, 'Match')

        section, options = self.ini.get_section('[Match]')
        assert 0 == check_section(self.test_info, section, options, 'Match')

        section, options = self.ini.get_section('Section')
        assert 0 == check_section(self.test_info, section, options, None)

        section, options = self.ini.add_section('Section')
        assert 0 == check_section(self.test_info, section, options, 'Section')

        section, options = self.ini.add_section('Section')
        assert 0 == check_section(self.test_info, section, options, 'Section')

        self.ini.remove_section('Section')
        section, options = self.ini.get_section('Section')
        assert 0 == check_section(self.test_info, section, options, None)

    # =========================================================================
    # test_15_option
    # =========================================================================
    def test_15_option(self):
        assert self.is_setup
        print('')

        section, options = self.ini.get_option('Network', 'Address')
        assert 0 == check_option(self.test_info, section, options, 'Network', 'Address', '192.168.0.1/24')

        section, options = self.ini.get_option('Network', 'address')
        assert 0 == check_option(self.test_info, section, options, 'Network', 'Address', '192.168.0.1/24')

        section, options = self.ini.get_option('Network', 'aDdReSs')
        assert 0 == check_option(self.test_info, section, options, 'Network', 'Address', '192.168.0.1/24')

        section, options = self.ini.get_option('Network', 'DNS')
        assert 0 == check_option(self.test_info, section, options, 'Network', 'DNS', ['8.8.8.8', '8.8.4.4'])

        section, options = self.ini.get_option('Network', 'Test')
        assert 0 == check_option(self.test_info, section, options, 'Network', 'Test', None)

        section, options = self.ini.get_option('Section', 'Test')
        assert 0 == check_option(self.test_info, section, options, None, None, None)

        self.ini.set_option('Section', 'Test', 'value')
        section, options = self.ini.get_option('Section', 'Test')
        assert 0 == check_option(self.test_info, section, options, 'Section', 'Test', 'value')

        self.ini.set_option('Section', 'Test', 'different')
        section, options = self.ini.get_option('Section', 'Test')
        assert 0 == check_option(self.test_info, section, options, 'Section', 'Test', 'different')

        self.ini.set_option('Section', 'Test', 1234)
        section, options = self.ini.get_option('Section', 'Test')
        assert 0 == check_option(self.test_info, section, options, 'Section', 'Test', '1234')

        self.ini.remove_option('Section', 'Test')
        section, option = self.ini.get_option('Section', 'Test')
        assert 0 == check_option(self.test_info, section, option, 'Section', 'Test', None)

        value = ['one', 'two', 'three']
        self.ini.set_option('Section', 'Test', value)
        section, options = self.ini.get_option('Section', 'Test')
        assert 0 == check_option(self.test_info, section, options, 'Section', 'Test', value)

        value = ['four', 'five']
        self.ini.set_option('Section', 'Test', value)
        section, options = self.ini.get_option('Section', 'Test')
        assert 0 == check_option(self.test_info, section, options, 'Section', 'Test', value)

        self.ini.set_option('Section', 'Test', 'value')
        section, options = self.ini.get_option('Section', 'Test')
        assert 0 == check_option(self.test_info, section, options, 'Section', 'Test', 'value')

        value = ['one', 'two', 'three']
        self.ini.set_option('Section', 'Test', value)
        section, options = self.ini.get_option('Section', 'Test')
        assert 0 == check_option(self.test_info, section, options, 'Section', 'Test', value)

    # =========================================================================
    # test_20_str
    # =========================================================================
    def test_20_str(self):
        assert self.is_setup
        print('')

        value = self.ini.get_str('Section', 'TestStr')
        assert 0 == check_str(self.test_info, value, 'Section', 'TestStr', None)

        self.ini.set_str('Section', 'TestStr', 'value')
        value = self.ini.get_str('Section', 'TestStr')
        assert 0 == check_str(self.test_info, value, 'Section', 'TestStr', 'value')

        self.ini.set_str('Section', 'TestStr', 'junk')
        value = self.ini.get_str('Section', 'TestStr')
        assert 0 == check_str(self.test_info, value, 'Section', 'TestStr', 'junk')

        self.ini.set_str('Section', 'TestStr', '')
        value = self.ini.get_str('Section', 'TestStr')
        assert 0 == check_str(self.test_info, value, 'Section', 'TestStr', '')

        self.ini.set_str('Section', 'TestStr', None)
        value = self.ini.get_str('Section', 'TestStr')
        assert 0 == check_str(self.test_info, value, 'Section', 'TestStr', None)

    # =========================================================================
    # test_25_bool
    # =========================================================================
    def test_25_bool(self):
        assert self.is_setup
        print('')

        value = self.ini.get_bool('Section', 'TestBool')
        assert 0 == check_str(self.test_info, value, 'Section', 'TestBool', None)

        self.ini.set_bool('Section', 'TestBool', True)
        value = self.ini.get_str('Section', 'TestBool')
        assert 0 == check_str(self.test_info, value, 'Section', 'TestBool', 'yes')

        self.ini.set_bool('Section', 'TestBool', False)
        value = self.ini.get_str('Section', 'TestBool')
        assert 0 == check_str(self.test_info, value, 'Section', 'TestBool', 'no')

        self.ini.set_str('Section', 'TestBool', 'True')
        value = self.ini.get_bool('Section', 'TestBool')
        assert 0 == check_str(self.test_info, str(value), 'Section', 'TestBool', 'True')

        self.ini.set_str('Section', 'TestBool', 'Yes')
        value = self.ini.get_bool('Section', 'TestBool')
        assert 0 == check_str(self.test_info, str(value), 'Section', 'TestBool', 'True')

        self.ini.set_str('Section', 'TestBool', 'YES')
        value = self.ini.get_bool('Section', 'TestBool')
        assert 0 == check_str(self.test_info, str(value), 'Section', 'TestBool', 'True')

        self.ini.set_str('Section', 'TestBool', 'On')
        value = self.ini.get_bool('Section', 'TestBool')
        assert 0 == check_str(self.test_info, str(value), 'Section', 'TestBool', 'True')

        self.ini.set_str('Section', 'TestBool', '1')
        value = self.ini.get_bool('Section', 'TestBool')
        assert 0 == check_str(self.test_info, str(value), 'Section', 'TestBool', 'True')

        self.ini.set_str('Section', 'TestBool', 'junk')
        value = self.ini.get_bool('Section', 'TestBool')
        assert 0 == check_str(self.test_info, str(value), 'Section', 'TestBool', 'False')

        self.ini.set_bool('Section', 'TestBool', None)
        value = self.ini.get_str('Section', 'TestBool')
        assert 0 == check_str(self.test_info, value, 'Section', 'TestBool', None)

    # =========================================================================
    # test_30_int
    # =========================================================================
    def test_30_int(self):
        assert self.is_setup
        print('')

        value = self.ini.get_int('Section', 'TestInt')
        assert 0 == check_str(self.test_info, value, 'Section', 'TestInt', None)

        self.ini.set_int('Section', 'TestInt', 0)
        value = self.ini.get_str('Section', 'TestInt')
        assert 0 == check_str(self.test_info, value, 'Section', 'TestInt', '0')
        value = self.ini.get_int('Section', 'TestInt')
        assert 0 == check_str(self.test_info, str(value), 'Section', 'TestInt', '0')
        value += 1
        self.ini.set_int('Section', 'TestInt', value)
        assert 0 == check_str(self.test_info, str(value), 'Section', 'TestInt', '1')

        self.ini.set_int('Section', 'TestInt', 1234)
        value = self.ini.get_str('Section', 'TestInt')
        assert 0 == check_str(self.test_info, value, 'Section', 'TestInt', '1234')
        value = self.ini.get_int('Section', 'TestInt')
        assert 0 == check_str(self.test_info, str(value), 'Section', 'TestInt', '1234')

        self.ini.set_int('Section', 'TestInt', -5678)
        value = self.ini.get_str('Section', 'TestInt')
        assert 0 == check_str(self.test_info, value, 'Section', 'TestInt', '-5678')
        value = self.ini.get_int('Section', 'TestInt')
        assert 0 == check_str(self.test_info, str(value), 'Section', 'TestInt', '-5678')

        self.ini.set_str('Section', 'TestInt', '9753')
        value = self.ini.get_int('Section', 'TestInt')
        assert 0 == check_str(self.test_info, str(value), 'Section', 'TestInt', '9753')

        self.ini.set_str('Section', 'TestInt', '-8642')
        value = self.ini.get_int('Section', 'TestInt')
        assert 0 == check_str(self.test_info, str(value), 'Section', 'TestInt', '-8642')

        try:
            self.test_info.test_number += 1
            print('{0:d} - get_int on non int'.format(self.test_info.test_number))
            self.ini.set_str('Section', 'TestInt', 'value')
            self.ini.get_int('Section', 'TestInt')
            self.test_info.num_errors += 1
            print("ERROR: shouldn't be able to get an integer")
        except ValueError:
            pass

        self.ini.set_int('Section', 'TestInt', None)
        value = self.ini.get_str('Section', 'TestInt')
        assert 0 == check_str(self.test_info, value, 'Section', 'TestInt', None)

    # =========================================================================
    # test_35_list
    # =========================================================================
    def test_35_list(self):
        assert self.is_setup
        print('')

        value = self.ini.get_list('Section', 'TestList')
        assert 0 == check_list(self.test_info, value, 'Section', 'TestList', None)

        value = ['one', 'two', 'three', 'four', 'five', 'six', 'seven']
        self.ini.set_list('Section', 'TestList', value, ' ', 0)
        section, options = self.ini.get_option('Section', 'TestList')
        assert 0 == check_option(self.test_info, section, options, 'Section', 'TestList',
                                 ['one two three four five six seven'])
        new_value = self.ini.get_list('Section', 'TestList')
        assert 0 == check_list(self.test_info, new_value, 'Section', 'TestList', value)

        self.ini.set_list('Section', 'TestList', value, ' ', 1)
        section, options = self.ini.get_option('Section', 'TestList')
        assert 0 == check_option(self.test_info, section, options, 'Section', 'TestList',
                                 ['one', 'two', 'three', 'four', 'five', 'six', 'seven'])
        new_value = self.ini.get_list('Section', 'TestList')
        assert 0 == check_list(self.test_info, new_value, 'Section', 'TestList', value)

        self.ini.set_list('Section', 'TestList', value, ' ', 3)
        section, options = self.ini.get_option('Section', 'TestList')
        assert 0 == check_option(self.test_info, section, options, 'Section', 'TestList',
                                 ['one two three', 'four five six', 'seven'])
        new_value = self.ini.get_list('Section', 'TestList')
        assert 0 == check_list(self.test_info, new_value, 'Section', 'TestList', value)

        options[0].value = 'one two'
        section, options = self.ini.get_option('Section', 'TestList')
        assert 0 == check_option(self.test_info, section, options, 'Section', 'TestList',
                                 ['one two', 'four five six', 'seven'])
        new_value = self.ini.get_list('Section', 'TestList')
        assert 0 == check_list(self.test_info, new_value, 'Section', 'TestList',
                               ['one', 'two', 'four', 'five', 'six', 'seven'])

        value = ['all', 'good', 'children', 'get', 'candy']
        self.ini.set_list('Section', 'TestList', value, ' ', 3)
        section, options = self.ini.get_option('Section', 'TestList')
        assert 0 == check_option(self.test_info, section, options, 'Section', 'TestList',
                                 ['all good children', 'get candy'])
        new_value = self.ini.get_list('Section', 'TestList')
        assert 0 == check_list(self.test_info, new_value, 'Section', 'TestList', value)

        self.ini.set_list('Section', 'TestList', 'value', ' ', 3)
        section, options = self.ini.get_option('Section', 'TestList')
        assert 0 == check_option(self.test_info, section, options, 'Section', 'TestList', ['value'])
        new_value = self.ini.get_list('Section', 'TestList')
        assert 0 == check_list(self.test_info, new_value, 'Section', 'TestList', ['value'])

        self.ini.set_list('Section', 'TestList', None, ' ', 3)
        value = self.ini.get_list('Section', 'TestList')
        assert 0 == check_list(self.test_info, value, 'Section', 'TestList', None)

    # =========================================================================
    # test_40_sec
    # =========================================================================
    def test_40_sec(self):
        assert self.is_setup
        print('')

        value = self.ini.get_sec('Section', 'TestSec')
        assert 0 == check_str(self.test_info, value, 'Section', 'TestSec', None)

        self.ini.set_sec('Section', 'TestSec', 1)
        value = self.ini.get_str('Section', 'TestSec')
        assert 0 == check_str(self.test_info, value, 'Section', 'TestSec', '1s')

        self.ini.set_sec('Section', 'TestSec', IniFile.SECONDS_PER_DAY)
        value = self.ini.get_str('Section', 'TestSec')
        assert 0 == check_str(self.test_info, value, 'Section', 'TestSec', '1d')
        value = self.ini.get_sec('Section', 'TestSec')
        assert 0 == check_str(self.test_info, str(value), 'Section', 'TestSec', str(IniFile.SECONDS_PER_DAY))

        self.ini.set_str('Section', 'TestSec', '1w')
        value = self.ini.get_sec('Section', 'TestSec')
        assert 0 == check_str(self.test_info, str(value), 'Section', 'TestSec', str(IniFile.SECONDS_PER_WEEK))

        self.ini.set_sec('Section', 'TestSec', None)
        value = self.ini.get_str('Section', 'TestSec')
        assert 0 == check_str(self.test_info, value, 'Section', 'TestSec', None)

    # =========================================================================
    # test_45_nb
    # =========================================================================
    def test_45_nb(self):
        assert self.is_setup
        print('')

        value = self.ini.get_nb('Section', 'TestNumBytes')
        assert 0 == check_str(self.test_info, value, 'Section', 'TestNumBytes', None)

        self.ini.set_nb('Section', 'TestNumBytes', 1)
        value = self.ini.get_str('Section', 'TestNumBytes')
        assert 0 == check_str(self.test_info, value, 'Section', 'TestNumBytes', '1')

        self.ini.set_nb('Section', 'TestNumBytes', IniFile.KILOBYTE)
        value = self.ini.get_str('Section', 'TestNumBytes')
        assert 0 == check_str(self.test_info, value, 'Section', 'TestNumBytes', '1K')
        value = self.ini.get_nb('Section', 'TestNumBytes')
        assert 0 == check_str(self.test_info, str(value), 'Section', 'TestNumBytes', str(IniFile.KILOBYTE))

        self.ini.set_str('Section', 'TestNumBytes', '1M')
        value = self.ini.get_nb('Section', 'TestNumBytes')
        assert 0 == check_str(self.test_info, str(value), 'Section', 'TestNumBytes', str(IniFile.MEGABYTE))

        self.ini.set_nb('Section', 'TestNumBytes', None)
        value = self.ini.get_str('Section', 'TestNumBytes')
        assert 0 == check_str(self.test_info, value, 'Section', 'TestNumBytes', None)

    # =========================================================================
    # test_50_bps
    # =========================================================================
    def test_50_bps(self):
        assert self.is_setup
        print('')

        value = self.ini.get_bps('Section', 'TestBytesPerSecond')
        assert 0 == check_str(self.test_info, value, 'Section', 'TestBytesPerSecond', None)

        self.ini.set_bps('Section', 'TestBytesPerSecond', 1)
        value = self.ini.get_str('Section', 'TestBytesPerSecond')
        assert 0 == check_str(self.test_info, value, 'Section', 'TestBytesPerSecond', '1')

        self.ini.set_bps('Section', 'TestBytesPerSecond', IniFile.THOUSAND)
        value = self.ini.get_str('Section', 'TestBytesPerSecond')
        assert 0 == check_str(self.test_info, value, 'Section', 'TestBytesPerSecond', '1K')
        value = self.ini.get_bps('Section', 'TestBytesPerSecond')
        assert 0 == check_str(self.test_info, str(value), 'Section', 'TestBytesPerSecond', str(IniFile.THOUSAND))

        self.ini.set_str('Section', 'TestBytesPerSecond', '1M')
        value = self.ini.get_bps('Section', 'TestBytesPerSecond')
        assert 0 == check_str(self.test_info, str(value), 'Section', 'TestBytesPerSecond', str(IniFile.MILLION))

        self.ini.set_bps('Section', 'TestBytesPerSecond', None)
        value = self.ini.get_str('Section', 'TestBytesPerSecond')
        assert 0 == check_str(self.test_info, value, 'Section', 'TestBytesPerSecond', None)

    # =============================================================================
    # test_55_property
    # =============================================================================
    def test_55_property(self):
        assert self.is_setup
        print('')

        network = NetworkFile(self.ini_file_name1)
        assert 0 == check_str(self.test_info, network.match_mac_address[0], 'Match', 'MACAddress', '11:22:33:44:55:66')
        assert 0 == check_str(self.test_info, network.match_name, 'Match', 'Name', None)
        assert 0 == check_str(self.test_info, network.network_dhcp, 'Network', 'DHCP', 'no')
        assert 0 == check_str(self.test_info, str(network.network_dhcp_server), 'Network', 'DHCPServer', 'True')
        assert 0 == check_str(self.test_info, network.network_address[0], 'Network', 'DHCPServer', '192.168.0.1/24')
        assert 0 == check_str(self.test_info, network.network_dns[0], 'Network', 'DNS', '8.8.8.8')
        assert 0 == check_str(self.test_info, network.network_dns[1], 'Network', 'DNS', '8.8.4.4')
        assert 0 == check_str(self.test_info, network.network_domains[0], 'Network', 'Domains', 'home.net')

        service_file_name = os.path.join(os.path.dirname(__file__), 'test1.service')
        service = ServiceFile(service_file_name)
        assert 0 == check_str(self.test_info, service.unit_after[0], 'Unit', 'After', 'network.target')
        assert 0 == check_str(self.test_info, service.install_wanted_by[0], 'Install', 'WantedBy', 'multi-user.target')
        assert 0 == check_str(self.test_info, service.service_kill_mode, 'Service', 'KillMode', 'process')

    # =============================================================================
    # test_99_last
    # =============================================================================
    def test_99_last(self):
        assert self.is_setup
        print('')

        self.ini.remove_section('Section')
        section, options = self.ini.get_section('Section')
        assert 0 == check_section(self.test_info, section, options, None)

        self.ini.save(self.ini_file_name2)
        assert 0 == compare_files(self.test_info, self.ini_file_name1, self.ini_file_name2)

        service_file_name1 = os.path.join(os.path.dirname(__file__), 'test1.service')
        service_file_name2 = os.path.join(os.path.dirname(__file__), 'test2.service')
        service1 = ServiceFile(service_file_name1)
        service2 = ServiceFile()
        service2.unit_after = service1.unit_after
        service2.service_after = service1.service_after
        service2.service_working_directory = service1.service_working_directory
        service2.service_type = service1.service_type
        service2.service_exec_start = service1.service_exec_start
        service2.service_kill_mode = service1.service_kill_mode
        service2.install_wanted_by = service1.install_wanted_by
        service2.save(service_file_name2)
        assert 0 == compare_files(self.test_info, service_file_name1, service_file_name2)

        file_name1 = os.path.join(os.path.dirname(__file__), 'test1.ini')
        ini2 = IniFile(file_name1)
        value = ini2.get_str('Section', 'Option1')
        assert 0 == check_str(self.test_info, value, 'Section', 'Option1', 'onetwothree')
        value = ini2.get_str('Section', 'Option2')
        assert 0 == check_str(self.test_info, value, 'Section', 'Option2', 'one two three')
        value = ini2.get_str('Section', 'Option3')
        assert 0 == check_str(self.test_info, value, 'Section', 'Option3', 'onetwothree')
