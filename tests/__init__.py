import os
from sysdfiles import IniFile


# =============================================================================
# TestInfo
# =============================================================================
class TestInfo:
    test_number = 0
    num_errors = 0


# =============================================================================
# compare_files
# =============================================================================
def compare_files(test_info, file_name1, file_name2):
    start_num_errors = test_info.num_errors
    test_info.test_number += 1
    lines1 = open(file_name1, 'r').read().splitlines()
    lines2 = open(file_name2, 'r').read().splitlines()
    print('{0:d} - compare_files: {1} ({2:d}) {3} ({4:d})'.format(test_info.test_number,
          os.path.basename(file_name1), len(lines1),
          os.path.basename(file_name2), len(lines2)))
    if len(lines1) == len(lines2):
        line_number = 1
        for line1, line2 in zip(lines1, lines2):
            num_line_errors = 0
            parts1 = line1.split()
            parts2 = line2.split()
            # print('  {0:d} - {1:d} - {2}'.format(line_number, len(parts1), line1))
            if len(parts1) == len(parts2):
                for part1, part2 in zip(parts1, parts2):
                    if part1 != part2:
                        num_line_errors += 1
            else:
                num_line_errors += 1
            if num_line_errors > 0:
                print('ERROR: {0:d} difference(s) on line {1:d}'.format(num_line_errors, line_number))
                test_info.num_errors += num_line_errors
            line_number += 1
    else:
        test_info.num_errors += 1
        print("ERROR: the files don't have the same number of lines")
    return test_info.num_errors - start_num_errors


# =============================================================================
# check_names
# =============================================================================
def check_names(test_info, hosts, line, host_name, domain_name):
    start_num_errors = test_info.num_errors
    test_info.test_number += 1
    print('{0:d} - check_names: {1} {2} {3!r}'.format(test_info.test_number,
          hosts.host_name, hosts.domain_name, line))
    if hosts.host_name != host_name:
        test_info.num_errors += 1
        print("ERROR: host_name should be '{0}'".format(host_name))
    if hosts.domain_name != domain_name:
        test_info.num_errors += 1
        print("ERROR: domain_name should be '{0}'".format(domain_name))
    full_name = host_name + '.' + domain_name
    if line.name != full_name:
        test_info.num_errors += 1
        print("ERROR: line name should be '{0}'".format(full_name))
    return test_info.num_errors - start_num_errors


# =============================================================================
# check_section
# =============================================================================
def check_section(test_info, section, options, section_name):
    start_num_errors = test_info.num_errors
    test_info.test_number += 1
    print('{0:d} - check_section: {1!r} {2} {3}'.format(test_info.test_number,
          section, section_name, options))
    if section is None:
        if section_name is not None:
            test_info.num_errors += 1
            print('ERROR: section should not be None')
        if options is not None:
            test_info.num_errors += 1
            print('ERROR: options should be None')
    else:
        if section_name is None:
            test_info.num_errors += 1
            print('ERROR: section should be None')
        elif section.name.lower() != section_name.lower():
            test_info.num_errors += 1
            print("ERROR: section name should be '{0}'".format(section_name))
        if options is None:
            test_info.num_errors += 1
            print('ERROR: options should not be None')
        elif not isinstance(options, list):
            test_info.num_errors += 1
            print('ERROR: options should be a list')
    return test_info.num_errors - start_num_errors


# =============================================================================
# check_option
# =============================================================================
def check_option(test_info, section, options, section_name, option_name, option_values):
    start_num_errors = test_info.num_errors
    test_info.test_number += 1
    print('{0:d} - check_option: {1!r} {2!r} {3} {4} {5}'.format(test_info.test_number,
          section, options, section_name, option_name, option_values))
    if section is None:
        if section_name is not None:
            test_info.num_errors += 1
            print('ERROR: section should not be None')
        if options is not None:
            test_info.num_errors += 1
            print('ERROR: options should be None')
    else:
        if section_name is None:
            test_info.num_errors += 1
            print('ERROR: section should be None')
        elif section.name.lower() != section_name.lower():
            test_info.num_errors += 1
            print("ERROR: section name should be '{0}'".format(section_name))
        if options is None:
            if option_name is not None:
                test_info.num_errors += 1
                print('ERROR: options should not be None')
        else:
            if option_name is None:
                test_info.num_errors += 1
                print('ERROR: options should be None')
            elif not isinstance(options, list):
                test_info.num_errors += 1
                print('ERROR: options should be a list')
            else:
                option_name = option_name.lower()
                for option in options:
                    if option.name.lower() != option_name:
                        test_info.num_errors += 1
                        print("ERROR: options names should all be '{0}'".format(option_name))
                if option_values is None:
                    option_values = []
                elif not isinstance(option_values, list) and not isinstance(option_values, tuple):
                    option_values = [option_values]
                if len(options) != len(option_values):
                    test_info.num_errors += 1
                    print("ERROR: expected {0} values, got {1}".format(len(option_values), len(options)))
                else:
                    for i in range(0, len(options)):
                        if options[i].value != option_values[i]:
                            test_info.num_errors += 1
                            print("ERROR: expected {0}, got {1}".format(option_values[i], options[i].value))
    return test_info.num_errors - start_num_errors


# =============================================================================
# check_str
# =============================================================================
def check_str(test_info, value, section_name, option_name, option_value):
    start_num_errors = test_info.num_errors
    test_info.test_number += 1
    print('{0:d} - check_str: {1} {2} {3} {4}'.format(test_info.test_number, value,
          section_name, option_name, option_value))
    if value is None:
        if option_value is not None:
            test_info.num_errors += 1
            print('ERROR: value should not be None')
    else:
        if option_value is None:
            test_info.num_errors += 1
            print('ERROR: value should be None')
        elif not isinstance(value, str):
            test_info.num_errors += 1
            print('ERROR: value is not a string')
        elif value != option_value:
            test_info.num_errors += 1
            print('ERROR: expected {0}, got {1}'.format(option_value, value))
    return test_info.num_errors - start_num_errors


# =============================================================================
# check_list
# =============================================================================
def check_list(test_info, value, section_name, option_name, option_value):
    start_num_errors = test_info.num_errors
    test_info.test_number += 1
    print('{0:d} - check_list: {1} {2} {3} {4}'.format(test_info.test_number, value,
          section_name, option_name, option_value))
    if value is None:
        if option_value is not None:
            test_info.num_errors += 1
            print('ERROR: value should not be None')
    else:
        if option_value is None:
            test_info.num_errors += 1
            print('ERROR: value should be None')
        elif not isinstance(value, list):
            test_info.num_errors += 1
            print('ERROR: value is not a list')
        else:
            if len(value) != len(option_value):
                test_info.num_errors += 1
                print("ERROR: expected {0} values, got {1}".format(len(option_value), len(value)))
            else:
                for i in range(0, len(value)):
                    if value[i] != option_value[i]:
                        test_info.num_errors += 1
                        print("ERROR: expected {0}, got {1}".format(option_value[i], value[i]))
    return test_info.num_errors - start_num_errors


# =============================================================================
# check_str_to_sec
# =============================================================================
def check_str_to_sec(test_info, s, expected_sec, expected_s='', default_time_unit=1):
    start_num_errors = test_info.num_errors
    test_info.test_number += 1
    print('{0:d} - check_str_to_sec: {1} {2} {3} {4}'.format(test_info.test_number, s, expected_sec, expected_s, default_time_unit))
    if expected_s == '':
        expected_s = s
    sec = IniFile.str_to_sec(s, default_time_unit)
    if sec != expected_sec:
        test_info.num_errors += 1
        print("ERROR: sec should be '{0}', got '{1}'".format(expected_sec, sec))
    new_s = IniFile.sec_to_str(sec)
    if new_s != expected_s:
        test_info.num_errors += 1
        print("ERROR: new s should be '{0}', got '{1}'".format(expected_s, new_s))
    return test_info.num_errors - start_num_errors


# =============================================================================
# check_sec_to_str
# =============================================================================
def check_sec_to_str(test_info, sec, expected_s):
    start_num_errors = test_info.num_errors
    test_info.test_number += 1
    print('{0:d} - check_sec_to_str: {1} {2}'.format(test_info.test_number, sec, expected_s))
    s = IniFile.sec_to_str(sec)
    if s != expected_s:
        test_info.num_errors += 1
        print("ERROR: s should be '{0}', got '{1}'".format(expected_s, s))
    new_sec = IniFile.str_to_sec(s)
    if new_sec != sec:
        test_info.num_errors += 1
        print("ERROR: new sec should be '{0}', got '{1}'".format(sec, new_sec))
    return test_info.num_errors - start_num_errors


# =============================================================================
# check_str_to_nb
# =============================================================================
def check_str_to_nb(test_info, s, expected_nb, expected_s=''):
    start_num_errors = test_info.num_errors
    test_info.test_number += 1
    print('{0:d} - check_str_to_nb: {1} {2} {3}'.format(test_info.test_number, s, expected_nb, expected_s))
    if expected_s == '':
        expected_s = s
    nb = IniFile.str_to_nb(s)
    if nb != expected_nb:
        test_info.num_errors += 1
        print("ERROR: nb should be '{0}', got '{1}'".format(expected_nb, nb))
    new_s = IniFile.nb_to_str(nb)
    if new_s != expected_s:
        test_info.num_errors += 1
        print("ERROR: new s should be '{0}', got '{1}'".format(expected_s, new_s))
    return test_info.num_errors - start_num_errors


# =============================================================================
# check_nb_to_str
# =============================================================================
def check_nb_to_str(test_info, nb, expected_s):
    start_num_errors = test_info.num_errors
    test_info.test_number += 1
    print('{0:d} - check_nb_to_str: {1} {2}'.format(test_info.test_number, nb, expected_s))
    s = IniFile.nb_to_str(nb)
    if s != expected_s:
        test_info.num_errors += 1
        print("ERROR: s should be '{0}', got '{1}'".format(expected_s, s))
    new_nb = IniFile.str_to_nb(s)
    if new_nb != nb:
        test_info.num_errors += 1
        print("ERROR: new nb should be '{0}', got '{1}'".format(nb, new_nb))
    return test_info.num_errors - start_num_errors


# =============================================================================
# check_str_to_bps
# =============================================================================
def check_str_to_bps(test_info, s, expected_bps, expected_s=''):
    start_num_errors = test_info.num_errors
    test_info.test_number += 1
    print('{0:d} - check_str_to_bps: {1} {2} {3}'.format(test_info.test_number, s, expected_bps, expected_s))
    if expected_s == '':
        expected_s = s
    bps = IniFile.str_to_bps(s)
    if bps != expected_bps:
        test_info.num_errors += 1
        print("ERROR: bps should be '{0}', got '{1}'".format(expected_bps, bps))
    new_s = IniFile.bps_to_str(bps)
    if new_s != expected_s:
        test_info.num_errors += 1
        print("ERROR: new s should be '{0}', got '{1}'".format(expected_s, new_s))
    return test_info.num_errors - start_num_errors


# =============================================================================
# check_bps_to_str
# =============================================================================
def check_bps_to_str(test_info, bps, expected_s):
    start_num_errors = test_info.num_errors
    test_info.test_number += 1
    print('{0:d} - check_bps_to_str: {1} {2}'.format(test_info.test_number, bps, expected_s))
    s = IniFile.bps_to_str(bps)
    if s != expected_s:
        test_info.num_errors += 1
        print("ERROR: s should be '{0}', got '{1}'".format(expected_s, s))
    new_bps = IniFile.str_to_bps(s)
    if new_bps != bps:
        test_info.num_errors += 1
        print("ERROR: new bps should be '{0}', got '{1}'".format(bps, new_bps))
    return test_info.num_errors - start_num_errors
