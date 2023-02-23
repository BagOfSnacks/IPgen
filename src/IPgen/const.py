import os
PATH = os.getcwd()

IP_RANGE_MIN = 0
IP_RANGE_MAX = 255
IP_v4_BYTES = 4
IP_v6_BYTES = 16

IP_v4_PATTERN = r'^(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$'