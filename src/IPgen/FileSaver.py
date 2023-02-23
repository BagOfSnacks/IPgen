import json
from abc import ABC, abstractmethod

from .const import PATH


class FileSaver(ABC):
    def __init__(self, filename: str, contents, **kwargs):
        self.filename = filename
        self.contents = contents
        self.extension = ""

        print(PATH)

    @abstractmethod
    def save_to_file(self):
        pass

    def get_loc(self):
        return self.filename + self.extension


class TxtSaver(FileSaver):
    def __init__(self, filename: str, contents, **kwargs):
        super().__init__(filename, contents, **kwargs)

        self.extension = ".txt"

    def save_to_file(self):
        with open(self.get_loc(), "w") as f:
            f.write(self.prepare_contents())

    def prepare_contents(self) -> str:
        result = ''.join([str(x) + "\n" for x in self.contents])
        return result.rstrip()


class JSONSaver(FileSaver):
    def __init__(self, filename: str, contents, **kwargs):
        super().__init__(filename, contents, **kwargs)

        self.extension = ".json"

    def save_to_file(self):
        with open(self.get_loc(), "w") as f:
            print(self.content_to_json())
            json.dump(self.content_to_json(), f, indent=4)

    def content_to_json(self):
        result = list(map(str, self.contents))
        d = {"ip_addresses": result}
        return d
