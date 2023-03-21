import os
PATH = os.getcwd()


# Project Metadata
PYTHON_VER = "3.11"
PYTEST_VER = "7.2.0"
PYTHON_VER_NOT_MATCHING = "Tests cannot be run.\n" f"Minimum required Python version: {PYTHON_VER}"
PYTEST_VER_NOT_MATCHING = "Tests cannot be run.\n" f"Minimum required Pytest module version: {PYTEST_VER}"

# IP Addresses
IP_v4_PATTERN = r'^(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$'
IP_v4_LENGTH = 4
IP_v4_RANGE_MIN = 0
IP_v4_RANGE_MAX = 255

IP_v6_PATTERN = r'^(([0-9ABCDEFabcdef]){1,4}:){7}([0-9ABCDEFabcdef]){1,4}$'
IP_v6_CHARS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
IP_v6_LENGTH = 8
IP_v6_RANGE_MIN = 0
IP_v6_RANGE_MAX = 65535

# Testing
TEST_TXT_FILENAME = "example"
TEST_JSON_FILENAME = TEST_TXT_FILENAME

# Saving to file
JSON_LIST_ABBREVIATION = "ip_addresses"
