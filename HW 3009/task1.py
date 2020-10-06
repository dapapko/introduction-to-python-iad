import os


class FileIter:

    def __init__(self, root: str):
        self.files = []
        self.strs = []
        self.root = root
        self.fill()
        self.fill_str()

    def fill(self):
        for path, dirs, files in os.walk(self.root):
            for file in files:
                with open(os.path.join(path, file), 'r', encoding='utf-8') as f:
                    if (len(f.read())) > 140:
                        self.files.append(os.path.join(path, file))

    def fill_str(self):
        for f in self.files:
            with open(f, 'r', encoding='utf-8') as file:
                self.strs.extend(file.readlines())

    def __iter__(self):
        return iter(self.strs)


fi = FileIter(r"C:\Users\Данила\files")

for a in fi:
    print(a)