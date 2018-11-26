from .unit_file import UnitFile


# =============================================================================
# PathFile
# =============================================================================
class PathFile(UnitFile):

    def __init__(self, file_name):
        UnitFile.__init__(self, file_name)
        self.add_properties('path',
                            [['changed', 'l'],
                             ['directory_mode'],
                             ['directory_not_empty', 'l'],
                             ['exists', 'l'],
                             ['exists_glob', 'l'],
                             ['make_directory', 'b'],
                             ['modified', 'l'],
                             ['unit']])
