# No Path Assets
from os import walk
from os.path import join

import cv2.cv2


def png(name: str):
    if name[-4:].lower() == '.png':
        return name
    return name + '.png'


class NPAssets:
    def __init__(self, root):
        self.root = root

        self.cache = {}
        self.library = {}

        self.read_assets()

    def fpath(self, name, is_png=True):
        if is_png:
            name = png(name)
        if name in self.library.keys():
            return self.library[name]
        else:
            raise RuntimeError("%s not found" % name)

    def fpng(self, name, refresh_lib=False, refresh_cache=False, read_cache=True):
        if refresh_lib:
            self.read_assets()

        if refresh_cache:
            self.cache[name] = cv2.cv2.imread(self.library[png(name)])

        if read_cache:
            if name in self.cache.keys():
                pass
            else:
                self.cache[name] = cv2.cv2.imread(self.library[png(name)])
            return self.cache[name]

        return cv2.cv2.imread(self.library[png(name)])

    def read_assets(self, init=True):
        for root, dirs, files in walk(self.root, topdown=False):
            for name in files:
                if init and name in self.library.keys():
                    print("Warn: same file name %s" % name)
                    # raise RuntimeError("same file name %s" % name)
                self.library[name] = join(root, name)
        return self.library


if __name__ == "__main__":
    pass
