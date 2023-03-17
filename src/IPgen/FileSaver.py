"""Handles saving IP Addresses as files of .txt and .json extensions"""

import json
import pathlib

from abc import ABC, abstractmethod
from typing import Sequence


class FileSaver(ABC):
    """
    Abstract class that handles saving list of addresses to a file.
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
        with open(self.path, "w") as f:
            f.write(self.prepare_contents())

    def prepare_contents(self) -> str:
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
        with open(self.path, "w") as f:
            json.dump(self.content_to_json(), f, indent=4)

    def content_to_json(self):
        result = list(map(str, self.contents))
        d = {"ip_addresses": result}
        return d
