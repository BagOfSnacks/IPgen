import json
import pathlib
from abc import ABC, abstractmethod


class FileSaver(ABC):
    extension = ""

    def __init__(self, path, contents, **kwargs):
        self.path = pathlib.Path(path)
        self.contents = contents
        self.path = self.path.with_suffix(self.extension)

    @abstractmethod
    def save_to_file(self):
        pass


class TxtSaver(FileSaver):
    def __init__(self, path, contents, **kwargs):
        self.extension = ".txt"
        super().__init__(path, contents, **kwargs)

    def save_to_file(self):
        with open(self.path, "w") as f:
            f.write(self.prepare_contents())

    def prepare_contents(self) -> str:
        result = ''.join([str(x) + "\n" for x in self.contents])
        return result.rstrip()


class JSONSaver(FileSaver):
    def __init__(self, path, contents, **kwargs):
        self.extension = ".json"
        super().__init__(path, contents, **kwargs)

    def save_to_file(self):
        with open(self.path, "w") as f:
            json.dump(self.content_to_json(), f, indent=4)

    def content_to_json(self):
        result = list(map(str, self.contents))
        d = {"ip_addresses": result}
        return d
