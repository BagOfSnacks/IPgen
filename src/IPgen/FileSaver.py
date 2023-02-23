from abc import ABC, abstractmethod


class FileSaver(ABC):
    def __init__(self, location: str, contents, **kwargs):
        self.location = location
        self.contents = contents
        self.save_to_file()

    @abstractmethod
    def save_to_file(self):
        pass


class TxtSaver(FileSaver):
    def save_to_file(self):
        with open(self.location, "w") as f:
            f.write(self.contents)
        print(self.location)

    def list_to_file(self):
        result = [str(x) + "\n" for x in self.contents]
        print(result)


class JSONSaver(FileSaver):
    def save_to_file(self):
        print(self.location)
