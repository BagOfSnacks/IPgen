import pathlib
import json

from IPgen.__main__ import random_ipv4_address, random_ipv6_address
from IPgen.util import is_ipv4_address, is_ipv6_address
from IPgen.FileSaver import TxtSaver, JSONSaver
from IPgen.const import TEST_JSON_FILENAME, TEST_TXT_FILENAME, JSON_LIST_ABBREVIATION



def path_test(tmp_path, filename: str):
    path = pathlib.Path(tmp_path)
    return path.joinpath(filename)


# ---- Text Files ---- #

def test_txt_file_is_saved_tmp(tmp_path):
    addresses = [random_ipv4_address() for _ in range(3)]
    path = path_test(tmp_path=tmp_path, filename=TEST_TXT_FILENAME)
    saver = TxtSaver(path, addresses)
    saver.save_to_file()
    assert saver.path.exists()

def test_txt_file_is_saved():
    addresses = [random_ipv4_address() for _ in range(3)]
    saver = TxtSaver(TEST_TXT_FILENAME, addresses)
    saver.save_to_file()
    assert saver.path.exists()

def test_contents_are_ipv4_addresses():
    with open(TEST_TXT_FILENAME + ".txt", "r") as f:
        content = f.readlines()
        valid = map(is_ipv4_address, content)
    assert all(valid) is True


def test_txt_file_is_saved_v6():
    addresses = [random_ipv6_address() for _ in range(3)]
    saver = TxtSaver(TEST_TXT_FILENAME, addresses)
    saver.save_to_file()
    assert saver.path.exists()


def test_contents_are_ipv6_addresses():
    with open(TEST_TXT_FILENAME + ".txt", "r") as f:
        content = f.readlines()
        valid = map(is_ipv6_address, content)
    assert all(valid) is True


# ---- JSON Files ---- #

def test_json_file_is_saved():
    addresses = [random_ipv4_address() for _ in range(3)]
    saver = JSONSaver(TEST_JSON_FILENAME, addresses)
    saver.save_to_file()
    assert saver.path.exists()


def test_json_contents_are_ipv4_addresses():
    with open(TEST_JSON_FILENAME + ".json", "r") as f:
        content = json.load(f)
        valid = map(is_ipv4_address, content[JSON_LIST_ABBREVIATION])
    assert all(valid) is True


def test_json_file_is_saved_v6():
    addresses = [random_ipv6_address() for _ in range(3)]
    saver = JSONSaver(TEST_JSON_FILENAME, addresses)
    saver.save_to_file()
    assert saver.path.exists()


def test_json_contents_are_ipv6_addresses():
    with open(TEST_JSON_FILENAME + ".json", "r") as f:
        content = json.load(f)
        valid = map(is_ipv6_address, content[JSON_LIST_ABBREVIATION])
    assert all(valid) is True
