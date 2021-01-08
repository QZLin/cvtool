# No Path Assets
from os import walk
from os.path import join

from cv2.cv2 import imread


def png(name: str):
    """
    Return name end with .png
    """
    if name[-4:].lower() == '.png':
        return name
    return name + '.png'


class NPAssets:
    def __init__(self, root, use_cache=False):
        self.root = root
        self.use_cache = use_cache

        self.cache = {}
        self.library = {}

        self.build_library(init=True)

    def fpath(self, name, is_png=True):
        if is_png:
            name = png(name)
        if name in self.library.keys():
            return self.library[name]
        else:
            raise RuntimeError("%s not found" % name)

    def fpng(self, name, refresh_lib=False, refresh_cache=False, read_cache=None):
        # from cv2.cv2 import imread
        name = png(name)

        if refresh_lib:
            self.build_library()

        if refresh_cache:
            self.cache[name] = imread(self.library[name])

        if read_cache is None:
            read_cache = self.use_cache
        if read_cache:
            if name in self.cache.keys():
                pass
            else:
                self.cache[name] = imread(self.library[name])
            return self.cache[name]

        return imread(self.library[name])

    def build_library(self, init=False, rebuild=False):
        if rebuild:
            self.library = {}
        for root, dirs, files in walk(self.root, topdown=False):
            for name in files:
                path = join(root, name)
                if init and name in self.library.keys():
                    print("Warn: same file name %s for:\n\t%s\n\t%s" % (name, self.library[name], path))
                    # raise RuntimeError("same file name %s" % name)
                self.library[name] = path
        return self.library


if __name__ == "__main__":
    pass
