import os

from IPgen.__main__ import random_IPv4_Adress
from IPgen.util import is_IPv4_adress
from IPgen.FileSaver import TxtSaver, JSONSaver
from IPgen.const import PATH

def test_file_is_saved():
    addresses = [random_IPv4_Adress() for _ in range(0,3)]
    saver = TxtSaver(contents=addresses, filename="example")
    saver.save_to_file()
    assert saver.filename + saver.extension in os.listdir()

def test_contents_are_ipv4_addresses():
    with open("example.txt", "r") as f:
        content = f.readlines()
        valid = map(is_IPv4_adress, content)
    assert all(valid) is True