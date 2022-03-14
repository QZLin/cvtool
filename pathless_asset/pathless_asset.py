import os


def png(name: str) -> str:
    """
    Return name end with `.png`
    """
    if name[-4:].lower() == '.png':
        return name
    return name + '.png'


def png_nex(name: str) -> str:
    if name[-4:].lower() == '.png':
        return name[:-4]
    return name


class PLAsset:
    def __init__(self, root, use_cache=False, rel_root=None, path_sep='/', strict_mode=False):
        self.root = root
        self.use_cache = use_cache
        self.rel_root = rel_root
        if os.sep == path_sep:
            path_sep = None
        self.sep = path_sep

        self.strict_mode = strict_mode

        self.cache = {}
        self.library = {}

        self.build_library(init=True)

    def fpath(self, name):
        if name in self.library.keys():
            return self.library[name]
        elif self.strict_mode:
            raise RuntimeError("PLAsset:%s not found" % name)
        else:
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
        for root, dirs, files in os.walk(self.root, topdown=False):
            for name in files:
                path = os.path.join(root, name)
                if self.rel_root:
                    path = os.path.relpath(path, self.root if self.rel_root is None else self.rel_root)
                if self.sep:
                    path = path.replace(os.sep, self.sep)
                # Duplicate Name Key
                if not init or name not in self.library.keys():
                    pass
                elif self.strict_mode:
                    raise RuntimeError("PLAsset:duplicate file name %s" % name)
                else:
                    print("Warn:duplicate file name %s for:\n\t%s\n\t%s" % (name, self.library[name], path))

                self.library[name] = path
        return self.library
