import os
PATH = os.getcwd()

IP_v4_RANGE_MIN = 0
IP_v4_RANGE_MAX = 255
IP_v4_BYTES = 4
IP_v6_BYTES = 16

IP_v4_PATTERN = r'^(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$'

# Testing
TEST_TXT_FILE = "example"
TEST_JSON_FILE = TEST_TXT_FILE

# Saving to file
JSON_LIST_ABBREVIATION = "ip_addresses"
