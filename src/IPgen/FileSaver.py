"""Handles saving IP Addresses as files of .txt and .json extensions"""

import json
import pathlib

from abc import ABC, abstractmethod
from typing import Sequence


class FileSaver(ABC):
    """
    Abstract class that handles saving list of IP addresses to a file.
    """
    extension = ""

    def __init__(self, path, contents: Sequence, **kwargs):
        self.path = pathlib.Path(path)
        self.contents = contents
        self.path = self.path.with_suffix(self.extension)

    @abstractmethod
    def save_to_file(self):
        pass


class TxtSaver(FileSaver):
    """
        Abstract class that handles saving list of addresses to a .txt file.

        Params:

            path: str or path-like
                Absolute / relative path to where a .txt file should be saved

            contents: Any
                List of IP Addresses to be saved

            **kwargs: keyword arguments
                Additional parameters
                Currently unused
    """

    def __init__(self, path, contents: Sequence, **kwargs):
        self.extension = ".txt"
        super().__init__(path, contents, **kwargs)

    def save_to_file(self):
        """
        Save a list of IP Addresses into a .txt file at target location
        """
        IP_adresses: str = self.prepare_contents()

        with open(self.path, "w", encoding='utf-8') as f:
            f.write(IP_adresses)

    def prepare_contents(self) -> str:
        """
        Transform list of IP Addresses into a properly formatted string
        """
        result = ''.join([str(x) + "\n" for x in self.contents])
        return result.rstrip()


class JSONSaver(FileSaver):
    """
        Abstract class that handles to-json format conversion and saving list of addresses to a .json file.

        Params:

            path: str or path-like
                Absolute / relative path to where a .json file should be saved

            contents: Any
                List of IP Addresses to be saved

            **kwargs: keyword arguments
                Additional parameters
                Currently unused
    """

    def __init__(self, path, contents: Sequence, **kwargs):
        self.extension = ".json"
        super().__init__(path, contents, **kwargs)

    def save_to_file(self):
        """
        Save list of IP Addresses into a .json file at target location
        """
        IP_addresses: dict = self.content_to_json()

        with open(self.path, "w", encoding='utf-8') as f:
            json.dump(IP_addresses, f, indent=5)

    def content_to_json(self) -> dict:
        """
        Convert list of IP Addresses into a Python dictionary
        """
        result = list(map(str, self.contents))
        d = {"ip_addresses": result}
        return d
