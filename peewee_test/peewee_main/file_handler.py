import os
import glob


# noinspection PyProtectedMember
class FileHandler(object):
    """
    File handler that safely opens up files for writing. This will in addition
    support creating subsequent versions if the file already exists.
    """

    def __init__(self, environment, file_suffix, version=False,
                 parent_dir='/sw/PLE/shared', prefix='bfx',
                 sub_dir='migrations', extension='.sql', file_type_suffix=None):
        """
        :param environment: Name of the environment that will be appended
                            to your file name.
                            Examples: your db name, project name etc
        :param file_suffix: Suffix that will be appended next to your
                            environment name. Generally your model name
        :param version:     Boolean to specify if your file needs version-ing
        :param parent_dir:  Parent directory in which the files will be stored
                            unless a sub directory is mentioned.
        :param sub_dir:     Sub directory under parent in which the files will
                            be stored.
        :param extension:   File extension. Either py or sql. Defaults to sql
        :param file_type_suffix: Type of the file if required will be appended
                                 to the file name.
                                 Examples: trigger, model etc.
        """

        self.environment = environment
        self.file_suffix = file_suffix
        self.version = version
        self.parent_dir = parent_dir
        self.sub_dir = sub_dir
        self.extension = extension
        self.file_type_suffix = file_type_suffix
        self.file_name = None
        self.handle = None
        self._pad_len = 5
        self.prefix = prefix

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.handle:
            self.handle.close()

    def _get_handle(self):
        """
        Opens up the file in write-append mode and
        returns the handler.
        """
        if self.file_name:
            self.handle = open(self.file_name, 'a')
            os.utime(self.file_name, None)
        return self.handle

    def _get_file_dir(self):
        """
        Generates and returns the file directory path.
        :return:
        """
        if self.sub_dir:
            self.parent_dir = '{}/{}'.format(self.parent_dir, self.sub_dir)
        if not os.path.exists(self.parent_dir):
            os.makedirs(self.parent_dir)
        return self.parent_dir

    def _get_version(self, current_version):
        """
        Generates and returns version number if specified
        """
        version = current_version + 1
        return str(version).zfill(self._pad_len)

    def get(self):
        """
        Creates and returns the file handler
        """
        self.parent_dir = self._get_file_dir()
        new_version = 0
        current_version = 0

        # Versions the file with 0 padded version numbers
        if self.version:
            files = glob.glob('{}/*{}'.format(self.parent_dir, self.extension))
            search_files = [
                fn for fn in files if
                '{file_suffix}_{file_type_suffix}'.format(
                    file_suffix=self.file_suffix, file_type_suffix=self.file_type_suffix)
                in fn
            ]
            if search_files:
                _file = max(search_files, key=os.path.getctime)
                current_version = int(_file.split('_')[-1].split('.')[0])

            new_version = self._get_version(current_version)

        file_path = '{file_directory}/'.format(file_directory=self.parent_dir)
        suffixes = '_'.join(name for name in [self.prefix, self.environment, self.file_suffix,
                                              self.file_type_suffix, new_version] if name)
        if suffixes[:-1] == '_':
            suffixes = suffixes[:-1]

        # noinspection PyTypeChecker
        self.file_name = file_path + suffixes + self.extension

        return self._get_handle()
