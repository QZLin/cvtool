import os.path
from os import walk
from os.path import join


def png(name: str):
    """
    Return name end with `.png`
    """
    if name[-4:].lower() == '.png':
        return name
    return name + '.png'


class PLAsset:
    def __init__(self, root, use_cache=False, relpath=False, relroot=None):
        self.root = root
        self.use_cache = use_cache
        self.relpath = relpath
        self.relroot = relroot

        self.cache = {}
        self.library = {}

        self.build_library(init=True)

    def fpath(self, name):
        # if is_png:
        #     name = png(name)
        if name in self.library.keys():
            return self.library[name]
        else:
            # raise RuntimeError("%s not found" % name)
            return None

    def fpng(self, name, refresh_lib=False, refresh_cache=False, read_cache=None):
        from cv2.cv2 import imread
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
                if self.relpath:
                    path = os.path.relpath(path, self.root if self.relroot is None else self.relroot)
                if init and name in self.library.keys():
                    print("Warn: same file name %s for:\n\t%s\n\t%s" % (name, self.library[name], path))
                    # raise RuntimeError("same file name %s" % name)
                self.library[name] = path
        return self.library
