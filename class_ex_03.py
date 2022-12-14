res = {"status": True,
       "output_path": "d:/test/asd.ma",
       "re_path_data": {"asset_group": True,
                        "image_plane": {},
                        "file_copy": True,
                        "re_path_asset":
                            {"status": True,
                             "assets": {
                                 "lion": {"status": True,
                                          "notes": True,
                                          "namespace": "namespace is proper",
                                          "re_path": "repath from W:/test.ma to d:/test.ma"}
                             }}}}


class ReprMixin:
    def __init__(self):
        pass

    def __repr__(self):
        s = self.__class__.__name__ + "("
        for k, v in self.__dict__.items():
            if not k.startswith("_"):
                s += "{}={}, ".format(k, v)
        s = s.rstrip(", ") + ")"
        return s


class RePathAssetData(ReprMixin):
    def __init__(self, asset_name, status, re_path, notes, name_space):
        ReprMixin.__init__(self)
        self.asset_name = asset_name
        self.status = status
        self.re_path = re_path
        self.notes = notes
        self.name_space = name_space


class RePathData(ReprMixin):
    def __init__(self, status=False, asset_group=False, file_copy=False, image_plane=None, assets=None):
        ReprMixin.__init__(self)
        if image_plane is None:
            image_plane = {}
        if assets is None:
            assets = {}
        self.status = status
        self.asset_group = asset_group
        self.file_copy = file_copy
        self.image_plane = image_plane
        self.assets = assets


class AllResult(ReprMixin):
    def __init__(self):
        ReprMixin.__init__(self)
        self.status = False
        self.output_path = ""
        self.re_path_assets = RePathData()

    def set_re_path_asset_grp(self, status):
        self.re_path_assets.asset_group = status

    def get_re_path_asset_grp(self):
        return self.re_path_assets.asset_group

    def set_re_path_status(self, status):
        self.re_path_assets.status = status

    def set_re_path_file_copy(self, status):
        self.re_path_assets.file_copy = status

    def set_re_path_image_plane(self, image_plane):
        self.re_path_assets.image_plane = image_plane

    @property
    def get_set_status(self):
        return self.re_path_assets.status

    @get_set_status.setter
    def get_set_status(self, status):
        self.re_path_assets.status = status


ref = AllResult()
ref.status = True
ref.output_path = "D:/test.ma"
ref.set_re_path_status(True)
ref.set_re_path_asset_grp(True)
ref.set_re_path_image_plane({})
print(ref.get_set_status)
ref.get_set_status = False
print(ref.get_set_status)

print(ref)
