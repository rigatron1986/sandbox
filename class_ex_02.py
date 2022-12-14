class BassetData(object):
    def __init__(self, export_path=None, preview=None, extra_pb=None, name=None, basset=None):
        self.export_path = export_path
        self.preview = preview
        self.extra_pb = extra_pb
        self.name = name
        self.basset = basset


class BassetMayaData(BassetData):
    def __init__(self, maya_file, export_path):
        super(BassetMayaData, self).__init__(export_path=export_path)
        self.maya_path = maya_file


playblast_dir = "local/ppardiban/test"
value = "1"
maya_basset = BassetMayaData(playblast_dir, value)
maya_basset.basset = "this is a test"
maya_basset.name = "this is a name"

print(maya_basset.name)
print(maya_basset.extra_pb)
print(maya_basset)
